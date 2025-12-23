import streamlit as st
import pandas as pd
import json
import os
from dotenv import load_dotenv
import plotly.graph_objects as go
import plotly.express as px
from collector import fetch_industry_news
from analyzer import analyze_strategy

# Page Config (Must be first)
st.set_page_config(
    page_title="Project DEEP SCAN",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    st.markdown("""
    <style>
        /* Import Premium Fonts */
        @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
        
        /* Global Font Enforcement - Safe Mode */
        .stApp, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label, div.stMarkdown {
            font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Malgun Gothic', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', sans-serif !important;
        }

        /* Material Icons Protection */
        .material-icons, span[class*="material"], i {
            font-family: 'Material Icons' !important;
        }

        /* Main Background */
        .stApp {
            background: #f8fafc;
            color: #0f172a;
        }
        
        /* Typography - Aggressively Reduced Sizes for Report Headers */
        h1 { font-size: 1.8rem !important; font-weight: 700 !important; margin-bottom: 0.8rem !important; }
        h2 { font-size: 1.5rem !important; font-weight: 600 !important; margin-top: 1.2rem !important; }
        h3 { font-size: 1.25rem !important; font-weight: 600 !important; }
        p, div { font-size: 0.95rem; line-height: 1.6; }
        
        /* Hide Streamlit Elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* Hero Section */
        .hero-container {
            padding: 3rem 2rem;
            text-align: center;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            border-radius: 20px;
            color: white;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px -10px rgba(0,0,0,0.3);
        }
        .hero-title {
            font-size: 2.5rem !important; /* Kept large for Hero only */
            font-weight: 800;
            background: linear-gradient(to right, #4ade80, #3b82f6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        .hero-subtitle {
            font-size: 1.1rem;
            color: #e2e8f0;
            margin-bottom: 1.5rem;
        }

        /* Card Styles */
        .feature-card {
            background: white;
            padding: 1.5rem;
            border-radius: 16px;
            border: 1px solid #e2e8f0;
            transition: all 0.3s ease;
            cursor: pointer;
            height: 100%;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
            border-color: #3b82f6;
        }
    </style>
    """, unsafe_allow_html=True)

# --- Graph Functions (Premium Aesthetic) ---
def render_sentiment_gauge(score):
    # Premium Colors
    if score >= 50: 
        bar_color = "#10b981" # Emerald-500
        bg_color = "#dcfce7" # Emerald-100
    elif score <= -50: 
        bar_color = "#f43f5e" # Rose-500
        bg_color = "#ffe4e6" # Rose-100
    else: 
        bar_color = "#64748b" # Slate-500
        bg_color = "#f1f5f9" # Slate-100

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Market Sentiment (시장 심리)", 'font': {'size': 15, 'color': "#475569", 'family': "Pretendard"}},
        number = {'font': {'size': 40, 'color': "#1e293b", 'family': "Pretendard"}},
        gauge = {
            'axis': {'range': [-100, 100], 'tickwidth': 1, 'tickcolor': "#94a3b8"},
            'bar': {'color': bar_color, 'thickness': 0.75}, # Thicker colored bar
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
                {'range': [-100, 100], 'color': "#f8fafc"} # Subtle subtle background
            ],
            'threshold': {
                'line': {'color': "#0f172a", 'width': 3},
                'thickness': 0.8,
                'value': score
            }
        }
    ))
    fig.update_layout(height=250, margin=dict(l=30, r=30, t=50, b=10), paper_bgcolor="rgba(0,0,0,0)", font={'family': "Pretendard"})
    return fig

def render_bias_gauge(score):
    # 0 (Neutral) -> 100 (Biased)
    # Gradient-like perception using steps
    # Good (Low Bias): Green, Bad (High Bias): Red
    
    if score <= 30: bar_color = "#22c55e"
    elif score <= 70: bar_color = "#f59e0b"
    else: bar_color = "#ef4444"

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Media Bias (편향성 지수)", 'font': {'size': 15, 'color': "#475569", 'family': "Pretendard"}},
        number = {'font': {'size': 40, 'color': "#1e293b", 'family': "Pretendard"}, 'suffix': "%"},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#94a3b8"},
            'bar': {'color': bar_color, 'thickness': 0.75},
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
                {'range': [0, 100], 'color': "#f8fafc"}
            ],
            'threshold': {'line': {'color': "#0f172a", 'width': 3}, 'thickness': 0.8, 'value': score}
        }
    ))
    fig.update_layout(height=250, margin=dict(l=30, r=30, t=50, b=10), paper_bgcolor="rgba(0,0,0,0)", font={'family': "Pretendard"})
    return fig

def render_sentiment_breakdown(pos, neg):
    # Modern stacked bar with rounded aesthetic via layout
    fig = go.Figure()
    
    # Positive
    fig.add_trace(go.Bar(
        y=[''], x=[pos], 
        name='Positive', 
        orientation='h', 
        marker=dict(color='#10b981', line=dict(width=0)), # Emerald
        text=[f"😊 긍정 {pos}%"], 
        textposition='inside', 
        insidetextanchor='middle',
        textfont=dict(color='white', family="Pretendard", size=14)
    ))
    
    # Negative
    fig.add_trace(go.Bar(
        y=[''], x=[neg], 
        name='Negative', 
        orientation='h', 
        marker=dict(color='#f43f5e', line=dict(width=0)), # Rose
        text=[f"😟 부정 {neg}%"], 
        textposition='inside', 
        insidetextanchor='middle',
        textfont=dict(color='white', family="Pretendard", size=14)
    ))
    
    fig.update_layout(
        barmode='stack', 
        height=100, 
        margin=dict(l=0, r=0, t=30, b=10),
        xaxis=dict(showgrid=False, showticklabels=False, range=[0, 100], fixedrange=True),
        yaxis=dict(showgrid=False, showticklabels=False, fixedrange=True),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title={'text': "긍정 vs 부정 요인 비율 (Sentiment Ratio)", 'font': {'size': 14, 'color': '#64748b'}, 'x': 0.5}
    )
    return fig

def render_daily_trend(df):
    if df.empty or 'publishedAt' not in df.columns: return None
    try:
        df['date'] = pd.to_datetime(df['publishedAt'], errors='coerce').dt.date
        df = df.dropna(subset=['date'])
        daily_counts = df['date'].value_counts().sort_index().reset_index()
        daily_counts.columns = ['Date', 'Count']
        if daily_counts.empty: return None
        fig = px.bar(daily_counts, x='Date', y='Count', title="📅 일별 키워드 언급량 추이", labels={'Count': '기사 수', 'Date': '날짜'}, color_discrete_sequence=['#10b981'])
        fig.update_layout(xaxis_title=None, yaxis_title=None, plot_bgcolor='white', hovermode="x unified", height=250, margin=dict(l=20, r=20, t=40, b=30))
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=True, gridcolor='#f1f5f9')
        return fig
    except: return None

# --- Main Logic ---
if __name__ == "__main__":
    load_dotenv()
    load_css()
    
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'Home'
        
    # Top Navigation
    with st.container():
        col_brand, col_nav1, col_nav2, col_nav3 = st.columns([6, 1.5, 1.5, 1.5])
        with col_brand: st.markdown("### 🚀 Project DEEP SCAN")
        with col_nav1:
            if st.button("🏠 Home", use_container_width=True):
                st.session_state['current_page'] = 'Home'
                st.rerun()
        with col_nav2:
            if st.button("🌅 Daily Briefing", use_container_width=True):
                st.session_state['current_page'] = 'Daily'
                st.rerun()
        with col_nav3:
            if st.button("🔍 Corporate", use_container_width=True): # Renamed to Corporate
                st.session_state['current_page'] = 'Search'
                st.rerun()
    st.markdown("---")

    # API Keys
    default_news_key = os.getenv("NEWS_API_KEY", "")
    default_groq_key = os.getenv("GROQ_API_KEY", "")
    keys_missing = not default_news_key or not default_groq_key
    with st.expander("🔑 API Key Settings", expanded=keys_missing):
        col_k1, col_k2 = st.columns(2)
        with col_k1: news_api_key = st.text_input("NewsAPI Key", value=default_news_key, type="password")
        with col_k2: groq_api_key = st.text_input("Groq API Key", value=default_groq_key, type="password")

    # Content
    if st.session_state['current_page'] == 'Home':
        st.markdown("""
        <div class="hero-container">
            <div class="hero-title">Project DEEP SCAN</div>
            <div class="hero-subtitle">
                삼성 그룹 전략기획 담당자를 위한<br>AI 기반 글로벌 마켓 인텔리전스 플랫폼
            </div>
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="feature-card">
                <h3>🌅 Daily Briefing</h3>
                <p>글로벌 유망 기술 및 경제 동향 브리핑</p>
                <ul><li>전 세계 Tech & Macro 이슈 자동 수집</li><li>Sentiment & Bias 분석</li></ul>
            </div>""", unsafe_allow_html=True)
            if st.button("Daily Briefing 시작 ➔", key="btn_d_h", type="primary", use_container_width=True):
                st.session_state['current_page'] = 'Daily'
                st.rerun()
        with col2:
            st.markdown("""
            <div class="feature-card">
                <h3>🏢 Corporate Analysis</h3>
                <p>삼성 계열사별 맞춤형 심층 분석</p>
                <ul><li>삼성전자, SDI, SDS 등 계열사 선택</li><li>맞춤형 키워드 자동 설정</li></ul>
            </div>""", unsafe_allow_html=True)
            if st.button("계열사 분석 시작 ➔", key="btn_s_h", type="primary", use_container_width=True):
                st.session_state['current_page'] = 'Search'
                st.rerun()
                
    else:
        target_query = ""
        is_ready = False
        
        if st.session_state['current_page'] == 'Daily':
            st.header("🌅 Daily Global Briefing")
            st.caption("AI, 반도체, EV, 글로벌 경제 동향 요약")
            if st.button("오늘의 리포트 생성", type="primary"):
                target_query = "AI technology OR semiconductor trend OR global economy market"
                is_ready = True
                
        elif st.session_state['current_page'] == 'Search':
            st.header("🏢 삼성 계열사 심층 분석 (Corporate Deep Dive)")
            
            # --- New Affiliate Selector Logic ---
            search_type = st.radio("검색 방식 선택", ["🏢 주요 계열사 선택", "✍️ 키워드 직접 입력"], horizontal=True)
            
            if search_type == "🏢 주요 계열사 선택":
                affiliates = [
                    "삼성전자 (Samsung Electronics) + HBM", 
                    "삼성전자 (Samsung Electronics) + 파운드리", 
                    "삼성SDI (Battery)", 
                    "삼성SDS (Cloud/AI)", 
                    "삼성전기 (MLCC)", 
                    "삼성디스플레이 (OLED)", 
                    "삼성물산 (Trading/Construction)", 
                    "삼성바이오로직스 (CDMO)"
                ]
                selected_affiliate = st.selectbox("분석 대상 계열사", affiliates)
                
                # Logic to map selection to query
                if "삼성전자" in selected_affiliate and "HBM" in selected_affiliate:
                    target_query = "Samsung Electronics HBM memory"
                elif "파운드리" in selected_affiliate:
                    target_query = "Samsung Electronics Foundry 3nm"
                elif "SDS" in selected_affiliate:
                    target_query = "Samsung SDS AI Cloud"
                elif "SDI" in selected_affiliate:
                    target_query = "Samsung SDI battery EV"
                elif "전기" in selected_affiliate:
                    target_query = "Samsung Electro-Mechanics MLCC"
                elif "디스플레이" in selected_affiliate:
                    target_query = "Samsung Display OLED"
                elif "바이오" in selected_affiliate:
                    target_query = "Samsung Biologics CDMO"
                else:
                    target_query = "Samsung C&T" # Default fallback for C&T

            else: # Manual Input
                user_query = st.text_input("분석할 키워드 입력 (예: 엔비디아, TSMC, 자율주행)", "HBM 반도체")
                target_query = user_query
            
            st.info(f"💡 현재 분석 키워드: **{target_query}**")
            
            if st.button("계열사 심층 리포트 생성", type="primary"):
                is_ready = True

        if is_ready:
            if not news_api_key or not groq_api_key: st.error("🚨 API Key가 필요합니다.")
            else:
                report = None
                df = pd.DataFrame()
                with st.status("🔍 데이터 분석 중...", expanded=True) as status:
                    status.write("🌐 글로벌 뉴스 수집 중...")
                    df = fetch_industry_news(target_query, news_api_key)
                    if not df.empty:
                        status.write("✅ AI 전략 분석 중...")
                        full_text = "\n".join([f"- {row['title']}: {row['description']}" for index, row in df.iterrows()])
                        report = analyze_strategy(full_text, groq_api_key)
                        status.update(label="완료!", state="complete", expanded=False)
                    else: status.update(label="데이터 없음", state="error")
                
                if report and not df.empty:
                    try:
                        if "[[JSON_START]]" in report:
                            text_part = report.split("[[JSON_START]]")[0]
                            json_part = report.split("[[JSON_START]]")[1].split("[[JSON_END]]")[0]
                            score_data = json.loads(json_part)
                        else: text_part, score_data = report, {}
                    except: text_part, score_data = report, {}

                    tab1, tab2, tab3 = st.tabs(["📑 전략 리포트", "🎯 감성 & 편향성", "📰 원문 기사 (Source Data)"])
                    
                    with tab1: 
                        st.markdown(text_part)
                        st.markdown("---")
                        st.info("ℹ️ 이 리포트의 근거가 된 뉴스 원문은 상단 **'📰 원문 기사 (Source Data)'** 탭에서 확인하실 수 있습니다.")
                    
                    with tab2:
                        c1, c2 = st.columns(2)
                        with c1: st.plotly_chart(render_sentiment_gauge(score_data.get("sentiment_score", 0)), use_container_width=True)
                        with c2: st.plotly_chart(render_bias_gauge(score_data.get("bias_score", 0)), use_container_width=True)
                        st.plotly_chart(render_sentiment_breakdown(score_data.get("positivity_ratio", 50), score_data.get("negativity_ratio", 50)), use_container_width=True)
                        
                        ec1, ec2 = st.columns(2)
                        with ec1:
                            st.success("✅ Positive Drivers")
                            for i in score_data.get("positive_drivers", []): st.markdown(f"- {i}")
                        with ec2:
                            st.error("⚠️ Negative Risks")
                            for i in score_data.get("negative_risks", []): st.markdown(f"- {i}")
                    
                    with tab3:
                        st.subheader("📊 Trend Analysis")
                        ft = render_daily_trend(df)
                        if ft: st.plotly_chart(ft, use_container_width=True)
                        st.dataframe(df[['title', 'source', 'publishedAt', 'url']].head(30), column_config={"url": st.column_config.LinkColumn("Link")}, hide_index=True, use_container_width=True)
