from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

def analyze_strategy(news_text, api_key, model_choice=None):
    """
    Analyzes the news text using Groq (Llama 3) to generate a strategic report.
    """
    if not api_key:
        return "⚠️ Groq API Key is missing. Please enter it in the sidebar."
    
    if not news_text or len(news_text) < 50:
        return "⚠️ 분석할 데이터가 부족합니다."

    try:
        # Initialize LLM (Groq Llama 3.3 is the new flagship)
        llm = ChatGroq(
            model_name="llama-3.3-70b-versatile", # Latest stable model
            groq_api_key=api_key,
            temperature=0.7
        )

        template = """
        당신은 삼성글로벌리서치(SGR)의 **'SGR 드림팀'**입니다. 
        세 명의 전문가(Persona)가 모여 토론한 뒤, 최종 전략 리포트를 작성하는 역할을 맡았습니다.

        ---
        **[토론 참여자]**
        1. **👨‍💼 거시경제 전문가 (Macro Economist)**: 금리, 환율, 지정학적 리스크, 글로벌 경제 흐름 분석.
        2. **🧑‍💻 산업 기술 전문가 (Tech Specialist)**: 반도체/AI 기술 트렌드, 경쟁사(TSMC, Intel 등) 기술 격차 분석.
        3. **🕵️ 전략 컨설턴트 (Strategy Consultant)**: 위 두 분석을 종합하여, 삼성전자가 당장 실행해야 할 **구체적 Action Plan** 도출.

        ---
        **[입력 뉴스 데이터]**:
        {news_content}
        ---

        위 뉴스 데이터를 바탕으로, 세 전문가의 관점을 통합하여 **SGR 스타일의 전략 리포트**를 작성하세요.
        반드시 **한국어**로 작성해야 하며, 아래 포맷을 엄격히 준수하세요:

        # 📑 SGR 드림팀 전략 리포트: [주제 키워드]

        ## 1. 🌐 거시경제 및 시장 환경 (Macro View)
        > *"숲을 먼저 봅니다." - 거시경제 전문가*
        - (환율, 금리, 국가 간 정책 갈등 등 거시적 관점에서의 기회/위협 요인 분석)

        ## 2. 🔬 산업 및 기술 딥다이브 (Tech Dive)
        > *"기술 디테일에 악마가 있습니다." - 산업 기술 전문가*
        - (경쟁사 기술 동향, 수율 문제, 차세대 패키징 등 기술적 관점의 심층 분석)

        ## 3. 🚀 SGR 전략 제언 (Action Plan)
        > *"그래서, 당장 무엇을 해야 합니까?" - 전략 컨설턴트*
        - **Short-term (1년 내)**: (구체적인 실행 과제, 예: 장비 수급, 특정 고객사 타겟팅)
        - **Long-term (3년 후)**: (R&D 방향성, M&A 필요성 등)

        ## ⚡ Executive Summary (한 줄 요약)
        (바쁜 임원진을 위한 1문장 핵심 결론)

        ---
        ## ⚡ Executive Summary (한 줄 요약)
        (바쁜 임원진을 위한 1문장 핵심 결론)

        ---
        **[분석 기준 (Analysis Criteria)]**
        1. **Sentiment Score (-100 ~ 100)**: 시장의 감성 (Market Sentiment)
           - -100 ~ -50: 매우 부정적 (Bearish)
           - -49 ~ 49: 중립 (Neutral)
           - 50 ~ 100: 매우 긍정적 (Bullish)
        
        2. **Breakdown (긍정 vs 부정 비중)**
           - 기사 내용 전체를 100으로 봤을 때, 긍정적 뉘앙스와 부정적 뉘앙스의 비율
        
        3. **Bias Score (0~100)**: 기사의 편향성 (Media Bias)
           - 0~30: 매우 중립적/객관적 (Fact-based)
           - 31~70: 다소 편향됨 (Opinionated)
           - 71~100: 매우 편향됨/선동적 (Highly Biased)

        ---
        **[System Instruction: Output JSON Data]**
        리포트 작성이 끝난 후, 반드시 맨 마지막 줄에 아래 형식으로 **JSON 데이터 하나만** 추가하세요.
        이 데이터는 시각화에 사용됩니다.
        
        [[JSON_START]]
        {{
            "sentiment_score": 75,
            "sentiment_label": "Bullish (강세)",
            "positivity_ratio": 80,
            "negativity_ratio": 20,
            "bias_score": 25,
            "bias_label": "Neutral (중립적)",
            "summary_reason": "AI 반도체 수요 폭증으로 인한 실적 개선 기대감 반영.",
            "positive_drivers": [
                "엔비디아 H200 주문량 3배 증가",
                "삼성전자의 3나노 수율 개선 소식",
                "미국 등 주요국의 반도체 지원금 확대"
            ],
            "negative_risks": [
                "지정학적 리스크로 인한 공급망 불안",
                "원자재 가격 상승 압박"
            ]
        }}
        [[JSON_END]]
        """
        
        prompt = PromptTemplate(
            input_variables=["news_content"],
            template=template,
        )
        
        formatted_prompt = prompt.format(news_content=news_text[:15000]) # Groq handles large context well
        response = llm.invoke(formatted_prompt).content
        
        return response

    except Exception as e:
        return f"❌ 분석 중 오류가 발생했습니다:\n{str(e)}\n\n(Tip: 사용 가능한 모델을 찾는데 실패했을 수 있습니다.)"
