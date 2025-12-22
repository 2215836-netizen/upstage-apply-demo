from langchain_openai import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

def analyze_strategy(news_text, api_key):
    """
    Analyzes the news text using OpenAI to generate a strategic report (SWOT/PEST).
    """
    if not api_key:
        return "⚠️ OpenAI API Key is missing. Please enter it in the sidebar."
    
    if not news_text or len(news_text) < 50:
        return "⚠️ 분석할 데이터가 부족합니다."

    try:
        # Initialize LLM
        llm = ChatOpenAI(
            temperature=0.7, 
            model_name="gpt-3.5-turbo", 
            openai_api_key=api_key
        )

        template = """
        당신은 글로벌 리서치 펌의 수석 전략가(CSO)입니다.
        삼성글로벌리서치(SGR) 경영진을 위해, 아래 뉴스 요약본을 바탕으로 심층적인 '전략 인사이트 리포트'를 작성하세요.
        
        반드시 **한국어**로 작성해야 하며, 다음 형식을 따르세요:
        
        # 📑 전략적 인사이트 리포트
        
        ## 1. Executive Summary (요약)
        (현재 시장 상황을 3문장 이내로 핵심만 요약)
        
        ## 2. 주요 기회 요인 (Opportunities)
        - (뉴스 데이터에 기반한 구체적인 기회 요인 나열)
        
        ## 3. 잠재적 위협 (Threats)
        - (경쟁사 동향, 규제, 기술적 위협 등)
        
        ## 4. 전략적 제언 (Recommendations)
        - **단기 전략**: (즉시 실행 가능한 조치)
        - **장기 전략**: (미래 방향성 제안)
        
        ---
        **참고 뉴스 데이터 (News Context)**:
        {news_content}
        """
        
        prompt = PromptTemplate(
            input_variables=["news_content"],
            template=template,
        )
        
        # In a newer LangChain version this might be LLMChain, but simplest way:
        formatted_prompt = prompt.format(news_content=news_text[:10000]) # simple truncation to avoid token limits
        response = llm.predict(formatted_prompt)
        
        return response

    except Exception as e:
        return f"분석 중 오류 발생: {str(e)}"
