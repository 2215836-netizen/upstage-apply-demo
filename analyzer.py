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

    # Model Priority List (Fallback Strategy)
    # 1. Flagship (Best Quality)
    # 2. Previous Flagship (Good Quality)
    # 3. Fast/Light (Best Availability)
    models_to_try = [
        "llama-3.3-70b-versatile", 
        "llama-3.1-70b-versatile", 
        "llama-3.1-8b-instant",
        "mixtral-8x7b-32768"
    ]

    for model_name in models_to_try:
        try:
            # Initialize LLM with current model selection
            llm = ChatGroq(
                model_name=model_name,
                groq_api_key=api_key,
                temperature=0.7
            )
            
            # Reduce context size for fallback models to save tokens/speed
            current_context_limit = 15000
            if "8b" in model_name:
                current_context_limit = 10000

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

            위 뉴스 데이터를 바탕으로, 세 전문가의 관점을 통합하여 **SGR 스타일의 심층 전략 리포트**를 작성하세요.
            **단순 요약이 아닌, 깊이 있는 통찰과 구체적인 데이터를 포함해야 합니다.**
            **각 섹션은 충분히 길고 상세하게 작성하세요 (최소 A4 2장 분량의 깊이).**
            반드시 **한국어**로 작성하며, 아래 포맷을 엄격히 준수하세요:

            # 📑 SGR 드림팀 전략 리포트: [주제 키워드]

            ## 1. 🌐 거시경제 및 시장 환경 (Macro View)
            > *"숲을 먼저 봅니다." - 거시경제 전문가*
            - **글로벌 경제 흐름**: 금리, 환율, 유가 등 주요 거시 지표가 해당 산업에 미치는 영향을 상세히 서술하세요.
            - **지정학적 리스크**: 미중 갈등, 공급망 이슈 등 대외 변수를 구체적으로 분석하세요.
            - **시장 기회와 위협**: 거시적 관점에서 삼성에게 다가오는 기회(Opportunity)와 위협(Threat)을 명확히 정의하세요.

            ## 2. 🔬 산업 및 기술 딥다이브 (Tech Dive)
            > *"기술 디테일에 악마가 있습니다." - 산업 기술 전문가*
            - **경쟁사 동향 분석**: TSMC, Intel, SK하이닉스 등 경쟁사의 최근 행보와 기술 격차를 상세히 비교 분석하세요.
            - **기술 트렌드 심층 분석**: HBM, GAA, Advanced Packaging 등 핵심 기술의 현황과 전망을 구체적인 수치/스펙과 함께 서술하세요.
            - **수율 및 생산 이슈**: 현재 제기되고 있는 기술적 난제와 해결 방안을 전문가적 시각에서 진단하세요.

            ## 3. 🚀 SGR 전략 제언 (Action Plan)
            > *"그래서, 당장 무엇을 해야 합니까?" - 전략 컨설턴트*
            - **Short-term Action (1년 내)**: 당장 실행해야 할 구체적인 과제 (예: 특정 장비 조기 도입, 고객사 다변화 전략)를 3가지 이상 제안하세요.
            - **Mid-to-Long-term Strategy (3년 후)**: 미래 시장 선점을 위한 중장기 로드맵 (예: 차세대 R&D 투자, M&A 타겟)을 제시하세요.
            - **Risk Management**: 예상되는 시나리오별 대응 전략(Contingency Plan)을 포함하세요.

            ## ⚡ Executive Summary (경영진 브리핑)
            (바쁜 임원진을 위한 3문장 이내의 핵심 결론 요약)

            ## 📚 주요 참조 원문 (Key Source Lists)
            - (본 리포트 작성에 결정적인 근거가 된 기사 제목과 출처를 3~5개 나열하세요. 예: *"Samsung's 3nm strategy shift" - TechCrunch*)

            ---

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
            
            # Adjust context window based on model capability
            formatted_prompt = prompt.format(news_content=news_text[:current_context_limit])
            
            print(f"🤖 Trying model: {model_name}...")
            response = llm.invoke(formatted_prompt).content
            
            # If successful, return immediately
            return response

        except Exception as e:
            error_msg = str(e)
            print(f"❌ Model {model_name} failed: {error_msg}")
            
            # Check specifically for Rate Limit (429) to try next model
            if "429" in error_msg or "Rate limit" in error_msg:
                continue
            # For other errors, also try next model just in case (optional, but safe)
            continue

    return "❌ 모든 AI 모델이 응답하지 않습니다. 잠시 후 다시 시도해주세요. (All models failed due to rate limits or errors)."
