# 작업 목록: Global Intelligence MVP (GIM)

- [ ] **프로젝트 설정 및 환경 구성**
    - [ ] 프로젝트 디렉터리 구조 생성 (`/src`, `/data`, `/tests`)
    - [ ] Git 저장소 초기화
    - [ ] `requirements.txt` 생성 (`streamlit`, `newsapi-python`, `langchain`, `openai`, `pandas`, `plotly`)
    - [ ] 가상 환경 설정 및 의존성 설치
    - [ ] `.env` 파일 생성 (NewsAPI, OpenAI API 키)

- [ ] **Part 1: 데이터 수집 모듈 (`collector.py`)**
    - [ ] `NewsCollector` 클래스 구현
    - [ ] NewsAPI 연동하여 키워드 기반 기사 수집 기능 구현
    - [ ] API 제한 도달 시 대체 메커니즘(예: 모의 데이터 또는 RSS) 구현
    - [ ] 데이터 수집 모듈 단위 테스트 작성

- [ ] **Part 2: 전략 분석 엔진 (`analyzer.py`)**
    - [ ] LangChain 및 OpenAI (또는 Ollama) 연동 설정
    - [ ] SWOT/PEST 분석을 위한 프롬프트 템플릿 설계
    - [ ] 텍스트 처리 및 인사이트 생성을 위한 `analyze_news` 함수 구현
    - [ ] 샘플 텍스트 데이터를 사용한 분석기 테스트

- [ ] **Part 3: 웹 대시보드 (`app.py`)**
    - [ ] Streamlit 앱 기본 레이아웃 초기화
    - [ ] 설정(API 키 등)을 위한 사이드바 생성
    - [ ] "산업/키워드" 입력을 위한 메인 입력창 구현
    - [ ] 버튼 클릭 시 `collector.py`와 연동하여 데이터 수집
    - [ ] `analyzer.py`와 연동하여 수집된 데이터로 리포트 생성
    - [ ] 결과 표시:
        - [ ] 마크다운 리포트 (SWOT 분석)
        - [ ] 수집된 기사 데이터 테이블
        - [ ] 차트 (소스별 분포, 타임라인)

- [ ] **Part 4: 검증 및 다듬기**
    - [ ] 실제 키워드(예: "HBM")를 사용한 엔드투엔드 테스트 수행
    - [ ] 로딩 상태 및 오류 처리 (UI 피드백)
    - [ ] 비즈니스 인사이트 품질 향상을 위한 프롬프트 개선
    - [ ] `README.md` 작성 (사용법 포함)
