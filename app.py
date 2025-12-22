import streamlit as st
import pandas as pd
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
st.sidebar.title("설정 (Configuration)")
news_api_key = st.sidebar.text_input("NewsAPI 키", type="password")
openai_api_key = st.sidebar.text_input("OpenAI API 키", type="password")

st.sidebar.markdown("---")
st.sidebar.info(
    "API 키 발급처:\n"
    "- [NewsAPI](https://newsapi.org)\n"
    "- [OpenAI](https://platform.openai.com)"
)

# Main Content
st.title("🚀 Project: DEEP SCAN")
st.markdown("""
### **"전 세계 뉴스를 꿰뚫는 AI의 시선, 24시간 깨어있는 SGR의 전략실"**
정보의 홍수 속에서 **0.1%의 '진짜' 기회**만 건져 올립니다.
""")

query = st.text_input("관심 산업 또는 주제 입력 (예: 'HBM 반도체', '테슬라 전략')", "HBM 반도체")

if st.button("전략 리포트 생성", type="primary"):
    if not news_api_key or not openai_api_key:
        st.error("사이드바에서 API 키를 먼저 입력해주세요.")
    else:
        # 1. Fetch Data
        with st.status("글로벌 뉴스 수집 중... (NewsAPI)", expanded=True) as status:
            df = fetch_industry_news(query, news_api_key)
            
            if not df.empty:
                status.write(f"✅ 관련 기사 {len(df)}건 수집 완료.")
                
                # Show Data Preview
                st.subheader("📰 뉴스 데이터 미리보기")
                st.dataframe(df[['title', 'source', 'publishedAt']].head(5))
                
                # 2. Analyze
                status.write("🧠 AI 전략 분석 중... (OpenAI)")
                
                # Combine descriptions for analysis
                full_text = "\n".join([f"- {row['title']}: {row['description']}" for index, row in df.iterrows()])
                
                report = analyze_strategy(full_text, openai_api_key)
                
                status.update(label="분석 완료!", state="complete", expanded=False)
                
                # 3. Render Report
                st.divider()
                st.markdown(report)
                
                # 4. Visualization (Source Distribution)
                st.divider()
                st.subheader("📊 뉴스 출처 분포")
                if 'source' in df.columns:
                    source_counts = df['source'].value_counts()
                    st.bar_chart(source_counts)
                
            else:
                status.update(label="데이터 없음", state="error")
                st.warning("해당 키워드에 대한 최신 뉴스가 없습니다. 키워드를 변경해보세요.")

# Footer
st.markdown("---")
st.caption("Global Intelligence MVP | Built for SGR")
