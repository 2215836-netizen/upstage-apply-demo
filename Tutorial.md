# AI를 활용한 프로젝트 빌딩 및 관리 튜토리얼

이 문서는 **Global Intelligence MVP (GIM)** 프로젝트를 구축하는 과정에서 사용된 **AI 프롬프트**와 **워크플로우**를 정리한 튜토리얼입니다. 아이에이션부터 GitHub 프로젝트 관리까지의 전 과정을 다룹니다.

---

## 🚀 1단계: 아이디어 구체화 및 PRD 작성 (Ideation to PRD)

가장 먼저 모호한 아이디어를 구체적인 제품 요구사항 정의서(PRD)로 변환합니다.

### 💡 Prompt
> **"@[Ideation.md] 의 내용으로 프로젝트 PRD를 작성해줘"**

### ✅ Action & Result
*   AI가 `Ideation.md`의 핵심 내용(목표, 기술 스택, 시나리오)을 분석.
*   **PRD.md** 자동 생성:
    *   프로젝트 개요 및 사용자 정의
    *   핵심 기능 (데이터 수집, 분석 엔진, 대시보드)
    *   기술 스택 및 유저 플로우
    *   성공 지표 및 로드맵

---

## 📋 2단계: 실행 가능한 태스크 수립 (Task Breakdown)

PRD를 바탕으로 실제 개발에 필요한 작업 목록을 도출합니다.

### 💡 Prompt
> **"@[PRD.md] 작업내용을 태스크로 만들어줘"**

### ✅ Action & Result
*   AI가 PRD의 기능을 구현 단위로 분해.
*   **task.md** 생성:
    *   프로젝트 셋업 / 데이터 수집기 / 분석 엔진 / 웹 대시보드 / 검증 등으로 구조화.
    *   각 파트별 상세 체크리스트 작성.

---

## 🌏 3단계: 로컬라이제이션 (Localization)

필요에 따라 문서의 언어를 변경하여 커뮤니케이션 효율을 높입니다.

### 💡 Prompt
> **"앞으로 문서나 커뮤니케이션은 한국어로 해줘."**

### ✅ Action & Result
*   **task.md** 등 주요 문서의 내용을 영문에서 국문으로 번역 및 업데이트.
*   이후 모든 대화와 결과물을 한국어로 제공.

---

## 🐙 4단계: GitHub 리포지토리 구축 (Hosting)

로컬 프로젝트를 GitHub 원격 저장소에 호스팅하고 버전 관리를 시작합니다.

### 💡 Prompt
> **"이 프로젝트를 github에 호스팅해줘. 퍼블릭 리포지토리로 만들어줘"**

### ✅ Action & Result
1.  **GitHub CLI 설치/로그인 점검**: `winget install GitHub.cli` 및 `gh auth login` 가이드.
2.  **프로젝트 구조화**: `Global-Intelligence-MVP` 폴더 생성 및 파일 이동.
3.  **Git 초기화 및 푸시**:
    *   `git init`, `git add`, `git commit`.
    *   `gh repo create` (또는 기존 리포지토리 연동).
    *   `git push -u origin main`으로 코드 업로드 완료.

---

## 🎫 5단계: 이슈 트래킹 자동화 (Issue Management)

작성된 태스크 리스트를 실제 GitHub 이슈로 등록하여 프로젝트 관리를 자동화합니다.

### 💡 Prompt
> **"태스크의 항목들을 깃헙 이슈로 등록해줘. 이슈에는 작업 배경, 작업 내용, 인수 조건이 포함 되어야 해."**

### ✅ Action & Result
*   `task.md`의 각 섹션을 파싱.
*   **GitHub Issue 생성**:
    *   제목: `task.md`의 섹션명 (예: [GIM] Part 1: 데이터 수집 모듈)
    *   본문: 작업 배경, 상세 작업 내용(체크리스트), 인수 조건(Acceptance Criteria) 자동 작성.
    *   `gh issue create` 명령어를 통해 리포지토리에 즉시 등록됨.

---

## ✨ 결론 (Conclusion)

이 튜토리얼은 **"문서 기반의 AI 협업"**이 얼마나 강력한지 보여줍니다.
단 몇 번의 프롬프트만으로 **[기획(PRD) -> 계획(Task) -> 구축(Repo) -> 관리(Issue)]**의 전체 개발 사이클을 셋업할 수 있었습니다.
