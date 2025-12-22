---
marp: true
theme: gaia
class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

# Global Intelligence MVP (GIM)
## 데이터를 전략적 자산으로 변환하다

---

## 📋 1. 프로젝트 개요 (Overview)

**"글로벌 산업 인사이트 엔진"**

*   **목표**: 반도체, AI 등 주요 산업의 글로벌 뉴스를 수집하여 **'전략적 기회와 위협 보고서'** 자동 생성
*   **핵심 가치**:
    *   단순 정보 수집을 넘어 **전략적 자산**화
    *   이슈 발생 시 **신속한 초동 대응** 시나리오 수립 지원

---

## 👥 2. 타겟 사용자 (User Persona)

**삼성글로벌리서치(SGR) 전략 분석가 & 경영진**

*   **Pain Point**:
    *   매일 쏟아지는 방대한 글로벌 뉴스
    *   단순 요약이 아닌 **비즈니스 인사이트** 필요
*   **Needs**:
    *   핵심 정보의 **빠른 파악**
    *   SWOT/PEST 프레임워크 기반의 **구조화된 보고서**
    *   보안 걱정 없는 **로컬 환경**

---

## 🔑 3. 핵심 기능 (Key Features)

### 1) Data Collector (데이터 수집)
*   특정 키워드(예: "HBM", "Solid-state Battery") 기반 실시간 뉴스 수집
*   NewsAPI / Google News RSS 활용

### 2) Strategic Analyzer (전략 분석)
*   **LLM 기반 분석**: 단순 요약 ❌ ➡ **SWOT 분석** ⭕
*   **인사이트 도출**: 기회(Opportunity) 및 위협(Threat) 요인 식별, 단기/장기 대응 전략 제언

---

## 💻 4. 기술 스택 (Tech Stack)

| 구분 | 기술 | 비고 |
| :--- | :--- | :--- |
| **Frontend** | `Streamlit` | Python 기반 빠른 대시보드 구축 |
| **Data** | `NewsAPI`, `Requests` | 실시간 데이터 수집 |
| **AI Engine** | `LangChain`, `OpenAI` | LLM 기반 텍스트 분석 및 추론 |
| **Analysis** | `Pandas`, `Plotly` | 데이터 가공 및 시각화 |

---

## 🔄 5. 유저 플로우 (User Flow)

1.  **접속**: Streamlit 웹 대시보드 실행
2.  **입력**: 분석할 '산업 키워드' 입력 (예: AI Semiconductor)
3.  **실행**: '분석 시작' 버튼 클릭
4.  **처리** (Background):
    *   뉴스 데이터 실시간 수집
    *   LangChain + LLM 전략 분석 프롬프트 실행
5.  **결과**: **전략 리포트** 및 소스별 통계 차트 확인

---

## 📊 6. 성공 지표 (Metrics)

*   **속도 (Speed)**: 키워드 입력 후 리포트 생성까지 **1분 이내**
*   **품질 (Quality)**: 단순 요약을 넘어 **'전략적 제언'** 포함 여부
*   **안정성 (Stability)**: 로컬 환경에서 에러 없는 구동

---

## 🗺️ 7. 향후 로드맵 (Roadmap)

*   **Phase 1 (MVP)** ✅
    *   뉴스 데이터 기반 SWOT 분석 기능 구현
*   **Phase 2** 🔜
    *   삼성 내부 지표(재무, 공시) 연동 및 인과관계 분석
*   **Phase 3** 🚀
    *   사용자 피드백 기반 커스텀 프롬프트 튜닝

---

# 감사합니다
## Q & A

---

## 📖 부록: 용어 설명 (Glossary)

*   **MVP (Minimum Viable Product)**: 핵심 기능만 갖춘 초기 모델
*   **SWOT 분석**: 강점/약점/기회/위협을 파악하는 경영 전략 프레임워크
*   **LLM (Large Language Model)**: 인간처럼 텍스트를 이해/생성하는 거대 AI 모델
*   **Streamlit**: Python만으로 빠르게 웹 대시보드를 만드는 라이브러리
*   **NewsAPI**: 전 세계 뉴스 기사를 실시간으로 가져오는 데이터 소스
