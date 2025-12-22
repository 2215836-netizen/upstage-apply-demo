# 🚀 Global Intelligence MVP (GIM)

**"데이터를 전략적 자산으로"**

Global Intelligence MVP(GIM)는 특정 산업(예: 반도체, AI, 모빌리티)의 글로벌 뉴스를 실시간으로 수집하고, LLM을 활용해 **전략적 기회와 위협(SWOT)**을 자동으로 분석해주는 로컬 대시보드입니다.

---

## 🎯 프로젝트 목표
경영진과 전략 분석가가 방대한 뉴스 데이터 속에서 **핵심 인사이트**를 즉시 파악하고, 글로벌 이슈에 대한 **초동 대응 시나리오**를 신속하게 수립할 수 있도록 지원합니다.

## ✨ 핵심 기능
1.  **실시간 뉴스 기사 수집**: 사용자가 입력한 키워드(예: "HBM", "Solid-state Battery") 관련 최신 글로벌 뉴스 수집 (NewsAPI 등 활용).
2.  **AI 기반 전략 분석**: LLM(OpenAI/Ollama)을 통해 수집된 뉴스를 분석하고, **Opportunity(기회)**와 **Threat(위협)** 중심의 전략 리포트 생성.
3.  **대시보드 시각화**: Streamlit 기반의 직관적인 UI로 분석 결과 및 뉴스 소스별 통계 차트 제공.

## 🛠️ 기술 스택
*   **Language**: Python 3.9+
*   **UI/Web**: Streamlit
*   **Data Acquisition**: NewsAPI, Requests
*   **AI/LLM**: LangChain, OpenAI API (or Local LLM)
*   **Data Analysis**: Pandas, Plotly/Matplotlib

## 🚀 시작하기 (Getting Started)

### 1. 필수 조건 (Prerequisites)
*   Python 3.9 이상
*   OpenAI API Key (또는 로컬 LLM 환경)
*   NewsAPI Key

### 2. 설치 (Installation)
```bash
# 저장소 클론
git clone https://github.com/2215836-netizen/upstage-apply-demo.git
cd upstage-apply-demo/Global-Intelligence-MVP

# 가상환경 생성 및 활성화 (선택 사항)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 패키지 설치
pip install -r requirements.txt
```

### 3. 환경 설정 (Configuration)
프로젝트 루트에 `.env` 파일을 생성하고 API 키를 입력하세요.
```env
OPENAI_API_KEY=your_openai_api_key
NEWS_API_KEY=your_newsapi_key
```

### 4. 실행 (Usage)
```bash
streamlit run app.py
```
브라우저가 열리면 사이드바에 API 키를 입력하거나 설정을 확인한 후, 분석하고 싶은 **키워드**를 입력하여 분석을 시작하세요.

## 📂 프로젝트 구조
```
Global-Intelligence-MVP/
├── src/                # 소스 코드 디렉터리
│   ├── collector.py    # 뉴스 데이터 수집 모듈
│   ├── analyzer.py     # LLM 전략 분석 엔진
│   └── app.py          # Streamlit 메인 애플리케이션
├── data/               # 데이터 저장소 (임시)
├── tests/              # 테스트 코드
├── .env                # 환경 변수 (API Key 등 - gitignore)
├── requirements.txt    # 의존성 목록
└── README.md           # 프로젝트 문서
```

## 🤝 기여 (Contribution)
이 프로젝트는 삼성글로벌리서치(SGR) 지원을 위한 MVP 프로젝트입니다. 아이디어나 개선 사항은 Issue를 통해 제안해 주세요.

---
© 2024 Global Intelligence MVP Team.
