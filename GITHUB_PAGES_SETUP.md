# GitHub Pages 배포 가이드

## ✅ 완료된 작업
1. `presentation.md`를 **reveal.js** 기반 HTML 프레젠테이션으로 변환했습니다.
2. `docs/index.html` 파일을 생성하고 GitHub에 푸시했습니다.

## 🚀 GitHub Pages 활성화 방법

### 1단계: GitHub 저장소 설정 페이지로 이동
1. 웹 브라우저에서 GitHub 저장소로 이동합니다:
   ```
   https://github.com/2215836-netizen/upstage-apply-demo
   ```

2. 상단 메뉴에서 **Settings** (⚙️ 설정) 탭을 클릭합니다.

### 2단계: GitHub Pages 설정
1. 왼쪽 사이드바에서 **Pages**를 클릭합니다.

2. **Source** 섹션에서:
   - **Branch**: `main` 선택
   - **Folder**: `/docs` 선택
   - **Save** 버튼 클릭

### 3단계: 배포 확인 (약 1-2분 소요)
1. 페이지 상단에 다음과 같은 메시지가 표시됩니다:
   ```
   Your site is ready to be published at https://2215836-netizen.github.io/upstage-apply-demo/
   ```

2. 몇 분 후 다음 URL로 접속하면 프레젠테이션을 볼 수 있습니다:
   ```
   https://2215836-netizen.github.io/upstage-apply-demo/
   ```

## 📖 프레젠테이션 사용 방법
- **화살표 키** (← →): 슬라이드 이동
- **스페이스바**: 다음 슬라이드
- **ESC**: 슬라이드 전체 보기
- **F**: 전체 화면 모드

## 🔄 프레젠테이션 업데이트 방법
`docs/index.html` 파일을 수정한 후:
```powershell
git add docs/index.html
git commit -m "Update presentation"
git push origin main
```

약 1-2분 후 변경사항이 자동으로 반영됩니다.

## 💡 참고사항
- reveal.js를 사용하여 전문적인 슬라이드 프레젠테이션을 구현했습니다.
- 모바일/태블릿에서도 정상적으로 작동합니다.
- 인터넷 연결이 필요합니다 (reveal.js CDN 사용).
