# Product Requirements Document (PRD): Global Intelligence MVP (GIM)

## 1. 프로젝트 개요 (Project Overview)
**프로젝트명:** Global Intelligence MVP (GIM)  
**목표:** 특정 산업(예: 반도체, AI, 모빌리티)의 글로벌 뉴스와 리포트를 수집하여, 경영진이 즉시 참고할 수 있는 **'전략적 기회와 위협 보고서'**를 자동 생성하는 로컬 대시보드 개발.  
**핵심 가치:** 
- 단순 데이터 수집을 넘어, 데이터를 **전략적 자산**으로 변환.
- 글로벌 이슈 발생 시 정기 리포트 발행 전 **초동 대응 시나리오** 수립 지원.

---

## 2. 사용자 정의 (User Personas)
* **Primary User:** 삼성글로벌리서치(SGR) 전략 분석가 및 경영진
* **User Needs:** 
    * 방대한 글로벌 뉴스 중 핵심 정보만 빠르게 파악하고 싶음.
    * 단순 요약이 아닌, SWOT/PEST 등 경영 프레임워크에 기반한 인사이트가 필요함.
    * 보안 문제 없이 로컬 환경에서도 구동 가능한 가벼운 툴을 선호함.

---

## 3. 핵심 기능 (Key Features)

### 3.1. 글로벌 뉴스 데이터 수집 (Data Collector)
* **기능:** 사용자가 입력한 특정 키워드(예: "HBM Semiconductor", "Samsung Electronics Strategy")를 기반으로 최신 글로벌 뉴스 데이터를 실시간으로 수집.
* **데이터 소스:** NewsAPI 또는 Google News RSS.
* **수집 항목:** 제목, 본문 요약, 출처, 게시일 등.

### 3.2. LLM 기반 전략 분석 (Strategic Analyzer)
* **기능:** 수집된 텍스트 데이터를 LLM(Large Language Model)을 통해 분석하여 전략적 인사이트 도출.
* **분석 프레임워크:** 
    * **Opportunity (기회 요인):** 시장 성장성, 새로운 기술 트렌드 등.
    * **Threat (위협 요인):** 경쟁사 동향, 규제 리스크 등.
    * **Strategic Recommendation (대응 전략):** 단기 및 장기적인 전략 제언.
* **기술 엔진:** LangChain + OpenAI API (또는 로컬 LLM인 Ollama).

### 3.3. 로컬 웹 대시보드 (Streamlit UI)
* **기능:** 
    * 사용자 친화적인 웹 인터페이스 제공.
    * 분석 진행 상황 로딩 인디케이터.
    * 최종 리포트 마크다운 렌더링.
    * 뉴스 소스별 비중 등 기본 시각화 차트 제공.

---

## 4. 기술 스택 (Technical Stack)
* **UI/Frontend:** `Streamlit` (Python 기반 웹 대시보드)
* **Data Acquisition:** `NewsAPI` (REST API), `Requests`
* **Analysis Engine:** `LangChain`, `OpenAI API` / `Ollama`
* **Data Processing & Visualization:** `Pandas`, `Matplotlib` / `Plotly`

---

## 5. 유저 플로우 (User Flow)
1. 사용자가 Streamlit 웹 대시보드에 접속한다.
2. 분석하고 싶은 '산업 키워드'를 입력창에 넣는다 (예: "Solid-state Battery").
3. '분석 시작' 버튼을 클릭한다.
4. (백그라운드) 시스템이 뉴스 데이터를 수집한다.
5. (백그라운드) LangChain이 수집된 데이터를 바탕으로 SWOT/PEST 분석 프롬프트를 실행한다.
6. 화면에 '전략 분석 리포트'와 '소스별 통계 차트'가 출력된다.

---

## 6. 성공 지표 (Success Metrics)
* **속도:** 키워드 입력 후 리포트 생성까지 1분 이내 완료.
* **품질:** 생성된 리포트가 단순 요약을 넘어 '전략적 제언'을 포함하는지 여부.
* **안정성:** 로컬 환경에서 에러 없이 구동 가능.

---

## 7. 향후 로드맵 (Future Roadmap)
* **Phase 1 (MVP):** 뉴스 데이터 기반 SWOT 분석 기능 구현.
* **Phase 2:** 삼성 내부 지표(재무 데이터, 공시 자료) 연동을 통한 인과관계 분석 고도화.
* **Phase 3:** 사용자 피드백을 반영한 커스텀 프롬프트 튜닝 및 UI 개선.
