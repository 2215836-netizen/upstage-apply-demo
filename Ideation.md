삼성글로벌리서치(SGR)의 데이터 분석가는 단순히 데이터를 만지는 사람이 아니라, **"데이터를 전략적 자산으로 변환하는 사람"**이어야 합니다.

이를 위해 로컬 환경에서 **2~3일 내에 완성**할 수 있으면서도, 면접에서 강력한 임팩트를 줄 수 있는 **[지능형 글로벌 산업 인사이트 엔진]** MVP 프로젝트를 제안합니다.

---

## 🛠️ 프로젝트명: Global Intelligence MVP (GIM)

**목표:** 특정 산업(예: 반도체, AI, 모빌리티)의 글로벌 뉴스와 리포트를 수집하여, 경영진이 즉시 참고할 수 있는 **'전략적 기회와 위협 보고서'**를 자동 생성하는 로컬 대시보드.

### 1. 기술 스택 (로컬 구현 최적화)

* **UI/Frontend:** `Streamlit` (파이썬만으로 웹 대시보드 구현)
* **Data Acquisition:** `NewsAPI` 또는 `Google News RSS` (무료/로컬 크롤링)
* **Analysis Engine:** `LangChain` + `OpenAI API` (또는 로컬 LLM인 `Ollama`)
* **Data Processing:** `Pandas`, `Matplotlib`/`Plotly` (시각화)

---

### 2. MVP 핵심 기능 및 코드 구조

#### **Step 1: 글로벌 뉴스 데이터 수집 (Data Collector)**

특정 키워드(예: "HBM Semiconductor", "Samsung Electronics Strategy")를 기반으로 최신 데이터를 가져옵니다.

```python
# collector.py
import requests
import pandas as pd

def fetch_industry_news(query):
    # 실제 프로젝트에선 NewsAPI 등을 사용 (무료 키 사용 가능)
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey=YOUR_API_KEY"
    response = requests.get(url).json()
    articles = response.get('articles', [])
    
    data = []
    for art in articles[:10]: # MVP이므로 상위 10개만
        data.append({
            'title': art['title'],
            'description': art['description'],
            'source': art['source']['name'],
            'publishedAt': art['publishedAt']
        })
    return pd.DataFrame(data)

```

#### **Step 2: LLM 기반 전략 분석 (Strategic Analyzer)**

수집된 텍스트를 단순 요약하는 게 아니라, **SGR이 사용하는 프레임워크(SWOT 또는 PEST)**로 재구성합니다.

```python
# analyzer.py
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

def analyze_strategy(news_text):
    template = """
    당신은 삼성글로벌리서치의 수석 전략 분석가입니다. 
    다음 뉴스 데이터를 바탕으로 '삼성전자'가 주목해야 할 전략적 인사이트를 작성하세요.
    
    1. Opportunity (기회 요인)
    2. Threat (위협 요인)
    3. Strategic Recommendation (단기/장기 대응 전략)
    
    뉴스 데이터: {news_content}
    """
    # ... LangChain 실행 로직 ...

```

#### **Step 3: 로컬 웹 대시보드 (Streamlit UI)**

사용자가 키워드를 입력하면 실시간으로 분석 결과와 차트를 보여줍니다.

```python
# app.py
import streamlit as st
from collector import fetch_industry_news
from analyzer import analyze_strategy

st.title("🚀 Global Industry Strategic Intelligence")

target_industry = st.text_input("분석할 산업/키워드를 입력하세요:", "HBM Semiconductor")

if st.button("분석 시작"):
    with st.spinner('글로벌 트렌드 분석 중...'):
        # 1. 뉴스 수집
        df = fetch_industry_news(target_industry)
        st.write(f"최신 뉴스 {len(df)}건 확보")
        
        # 2. 리포트 생성 (LLM 연동)
        full_text = " ".join(df['description'].fillna(''))
        report = analyze_strategy(full_text)
        
        # 3. 결과 출력
        st.subheader("📋 전략 분석 리포트")
        st.markdown(report)
        
        # 4. 시각화 (예: 뉴스 소스별 비중 등)
        st.bar_chart(df['source'].value_counts())

```

---

### 3. SGR 지원 시 이 프로젝트를 '어필'하는 방법

면접관에게 이 MVP를 설명할 때 다음과 같은 **'비즈니스 로직'**을 강조하세요:

1. **"정보의 가공":** "단순히 뉴스를 보여주는 것이 아니라, 텍스트 마이닝과 LLM을 결합하여 **경영진이 읽기 편한 전략적 프레임워크(SWOT)**로 변환하는 데 집중했습니다."
2. **"실시간 대응":** "정기 리포트가 나오기 전, 글로벌 이슈가 발생했을 때 **데이터 기반의 초동 대응 시나리오**를 짜기 위한 툴로 기획했습니다."
3. **"확장성":** "현재는 뉴스 데이터만 활용하지만, 향후 **삼성의 내부 지표(재무 데이터, 공시자료)**를 결합하면 훨씬 정교한 인과관계 분석이 가능하도록 설계했습니다."

---

### 4. 다음 단계 제안

이 로컬 MVP를 실제로 실행해 보시려면, **가장 먼저 관심 있는 산업군(예: 반도체, 이차전지 등)** 하나를 정해야 합니다.

* 어떤 산업군을 주제로 잡아볼까요? 주제를 정해주시면 그 산업에 특화된 **'전략 분석 프롬프트'**를 더 정교하게 짜드릴 수 있습니다.
* 혹은 이 코드에서 사용할 **무료 API 키 발급 방법**이나 **로컬 환경 설정 방법**이 궁금하신가요?