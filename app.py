import streamlit as st
import pandas as pd
import json
import plotly.graph_objects as go
from collector import fetch_industry_news
from analyzer import analyze_strategy

# Page Config
st.set_page_config(
    page_title="Project DEEP SCAN",
    page_icon="🚀",
    layout="wide"
)

# Sidebar for Settings
st.sidebar.header("🚀 Project DEEP SCAN")
st.sidebar.caption("SGR AI Strategy Team")
st.sidebar.markdown("---")
news_api_key = st.sidebar.text_input("NewsAPI 키", type="password")
groq_api_key = st.sidebar.text_input("Groq API 키", type="password")

st.sidebar.markdown("---")
st.sidebar.caption("※ Groq은 자동으로 'Llama 3' 모델을 사용합니다.")

st.sidebar.markdown("---")
st.sidebar.info(
    "API 키 발급처:\n"
    "- [NewsAPI](https://newsapi.org)\n"
    "- [Groq Cloud (Free)](https://console.groq.com/keys)"
)

# Main Content
st.title("🚀 Project: DEEP SCAN")
st.markdown("""
### **"전 세계 뉴스를 꿰뚫는 AI의 시선, 24시간 깨어있는 SGR의 전략실"**
정보의 홍수 속에서 **0.1%의 '진짜' 기회**만 건져 올립니다.
""")

query = st.text_input("관심 산업 또는 주제 입력 (예: 'HBM 반도체', '테슬라 전략')", "HBM 반도체")

if st.button("전략 리포트 생성", type="primary"):
    if not news_api_key or not groq_api_key:
        st.error("사이드바에서 API 키를 먼저 입력해주세요.")
    else:
        # 1. Fetch Data
        # 1. Fetch & Analyze
        report = None
        df = pd.DataFrame()
        
        with st.status("글로벌 뉴스 수집 중... (NewsAPI)", expanded=True) as status:
            df = fetch_industry_news(query, news_api_key)
            
            if not df.empty:
                status.write(f"✅ 관련 기사 {len(df)}건 수집 완료.")
                
                # Show Data Preview
                st.subheader("📰 뉴스 데이터 미리보기")
                st.dataframe(df[['title', 'source', 'publishedAt']].head(5))
                
                # 2. Analyze
                status.write("🧠 SGR 드림팀(거시경제/기술/전략)이 토론 중입니다... (Groq)")
                
                # Combine descriptions for analysis
                full_text = "\n".join([f"- {row['title']}: {row['description']}" for index, row in df.iterrows()])
                
                report = analyze_strategy(full_text, groq_api_key)
                
                status.update(label="분석 완료!", state="complete", expanded=False)
            else:
                status.update(label="데이터 없음", state="error")
        
        # 3. Render Report & Visualization (Outside Status Box)
        if report and not df.empty:
            
            # --- Parsig JSON Logic ---
            try:
                # 1. Split Text vs JSON
                if "[[JSON_START]]" in report:
                    text_part = report.split("[[JSON_START]]")[0]
                    json_part = report.split("[[JSON_START]]")[1].split("[[JSON_END]]")[0]
                    score_data = json.loads(json_part)
                else:
                    text_part = report
                    score_data = {"risk_score": 50, "impact_score": 50} # Default
            except:
                text_part = report
                score_data = {"risk_score": 50, "impact_score": 50}

            # --- 2x2 Matrix Visualization ---
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.divider()
                st.markdown(text_part)

            with col2:
                st.divider()
                st.subheader("🎯 Risk Matrix")
                
                risk = score_data.get("risk_score", 50)
                impact = score_data.get("impact_score", 50)
                
                fig = go.Figure()

                # Background Quadrants
                fig.add_shape(type="rect", x0=0, y0=0, x1=50, y1=50, fillcolor="#E8F5E9", layer="below", line_width=0) # Green
                fig.add_shape(type="rect", x0=50, y0=0, x1=100, y1=50, fillcolor="#FFF3E0", layer="below", line_width=0) # Yellow
                fig.add_shape(type="rect", x0=0, y0=50, x1=50, y1=100, fillcolor="#FFF3E0", layer="below", line_width=0) # Yellow
                fig.add_shape(type="rect", x0=50, y0=50, x1=100, y1=100, fillcolor="#FFEBEE", layer="below", line_width=0) # Red

                # Data Point
                fig.add_trace(go.Scatter(
                    x=[risk], y=[impact],
                    mode='markers+text',
                    text=['THIS ISSUE'],
                    textposition="top center",
                    marker=dict(size=20, color='red', symbol='star')
                ))

                fig.update_layout(
                    xaxis=dict(title="Risk Probability (위험도)", range=[0, 100], showgrid=False),
                    yaxis=dict(title="Strategic Impact (영향도)", range=[0, 100], showgrid=False),
                    width=300, height=300,
                    margin=dict(l=20, r=20, t=20, b=20),
                    showlegend=False
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                st.caption(f"**Risk**: {risk} / **Impact**: {impact}")
                
                # Show Rationale
                if "reason" in score_data:
                    st.info(f"💡 **판단 근거**: {score_data['reason']}")
                else:
                    st.info("우상단(Red)일수록 즉각적인 대응이 필요한 'Critical' 이슈입니다.")

            
            # 4. Visualization (Source Distribution)
            st.divider()
            st.subheader("📊 뉴스 출처 분포")
            if 'source' in df.columns:
                source_counts = df['source'].value_counts()
                st.bar_chart(source_counts)

            # 5. Reference Table
            st.divider()
            st.subheader("🔗 참고 뉴스 출처 (References)")
            st.dataframe(
                df[['publishedAt', 'source', 'title', 'url']],
                column_config={
                    "url": st.column_config.LinkColumn("링크", display_text="기사 보기"),
                    "publishedAt": "발행일",
                    "title": "제목",
                    "source": "출처"
                },
                hide_index=True,
                use_container_width=True
            )
        
        elif df.empty:
            st.warning("해당 키워드에 대한 최신 뉴스가 없습니다. 키워드를 변경해보세요.")

# Footer
st.markdown("---")
st.caption("Global Intelligence MVP | Built for SGR")
