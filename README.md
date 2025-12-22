# 🚀 Project DEEP SCAN
### **"전 세계 뉴스를 꿰뚫는 AI의 시선, 24시간 깨어있는 SGR의 전략실"**

> **"From Noise to Signal"** — 정보의 홍수 속에서 **0.1%의 '진짜' 기회**만 건져 올립니다.

---

## 📋 프로젝트 개요 (Overview)

**Project DEEP SCAN**은 방대한 글로벌 뉴스 데이터를 실시간으로 수집하고, **LLM(Large Language Model)** 에이전트가 이를 분석하여 **경영진을 위한 '전략 리포트(Executive Report)'**를 자동으로 생성해주는 인텔리전스 시스템입니다.

삼성글로벌리서치(SGR)와 같은 전략 조직에서 **자료 조사 시간을 획기적(10배)으로 단축**하고, 단순 정보 취합이 아닌 **'전략적 의사결정'**에 집중할 수 있도록 돕습니다.

## ✨ 핵심 기능 (Key Features)

### 1. 🔍 Data Collector (지능형 수집)
- 사용자가 지정한 키워드(예: `HBM`, `Solid-state Battery`)와 관련된 최신 **글로벌 뉴스**를 실시간으로 트래킹합니다.
- 광고성 기사나 단순 중복 기사를 필터링합니다.

### 2. 🧠 Strategic Analyzer (심층 분석)
- **OpenAI GPT-4** 레벨의 추론 능력을 활용하여 단순 요약이 아닌 **SWOT 분석**을 수행합니다.
- **Opportunity(기회)**: 시장의 변화 속에서 기업이 취할 수 있는 전략적 기회 포착
- **Threat(위협)**: 경쟁사 동향, 규제 변화 등 잠재적 리스크 조기 감지

### 3. 📊 Executive Dashboard (원페이지 리포트)
- **Streamlit** 기반의 직관적인 대시보드 UI를 제공합니다.
- 복잡한 설정 없이 **"키워드 입력 ➡ 원클릭 리포트 생성"**의 간결한 유저 플로우(User Flow)를 가집니다.

---

## 🛠️ 기술 스택 (Tech Stack)

| Layer | Component | Description |
| :--- | :--- | :--- |
| **Frontend** | `Streamlit` | Python 기반의 반응형 웹 대시보드 구축 |
| **Logic** | `LangChain` | LLM 워크플로우 오케스트레이션 및 프롬프트 관리 |
| **AI Model** | `OpenAI API` | GPT-3.5/4 모델을 활용한 고도화된 텍스트 분석 |
| **Data Source** | `NewsAPI` | 글로벌 80,000+ 소스의 실시간 뉴스 데이터 파이프라인 |

---

## 🚀 빠른 실행 (Quick Start)

이 프로젝트는 **Windows/Mac 로컬 환경**에서 즉시 실행 가능하도록 설계되었습니다.

### 1. 간편 실행 (Windows 추천)
프로젝트 폴더 내의 **`run_app.bat`** 파일을 더블 클릭하세요! (자동으로 가상환경을 잡고 실행됩니다.)

### 2. 수동 실행
```bash
# 1. 가상환경 활성화 (Windows)
.\venv\Scripts\activate

# 2. 필수 라이브러리 설치 (최초 1회)
pip install -r requirements.txt

# 3. 앱 실행
streamlit run app.py
```

---

## 📂 프로젝트 구조 (Structure)
```
Project-DEEP-SCAN/
├── 📄 app.py           # [Main] Streamlit 대시보드 엔트리포인트
├── 📄 collector.py     # [Data] 뉴스 수집 및 전처리 모듈
├── 📄 analyzer.py      # [AI] LangChain 기반 전략 분석 엔진
├── 📄 run_app.bat      # [Util] 원클릭 실행 스크립트
├── 📄 requirements.txt # [Env] 프로젝트 의존성 목록
└── 📄 presentation.md  # [Doc] 기획안 및 발표 자료 (MARP)
```

---

## 👨‍💻 만든 사람 (Author)

**SGR Data Analyst (지원자)**
- "Data-driven Decision Making을 넘어, **AI-driven Strategy**를 지향합니다."
