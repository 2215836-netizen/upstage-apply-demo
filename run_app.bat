@echo off
chcp 65001 > nul
cd /d "%~dp0"

echo ========================================================
echo 🚀 Project DEEP SCAN 실행 중...
echo (SGR AI Strategy Team)
echo ========================================================
echo.

:: 1. 가상환경(venv) 위치 찾기 (상위 폴더 or 현재 폴더)
set VENV_PATH=..\venv
if exist "venv" set VENV_PATH=venv

if not exist "%VENV_PATH%" (
    echo [ERROR] 가상환경(venv)을 찾을 수 없습니다.
    echo 프로젝트 폴더 구조를 확인해 주세요.
    pause
    exit
)

echo 2. 애플리케이션을 시작합니다...
echo (브라우저가 자동으로 열릴 때까지 잠시만 기다려 주세요.)
echo.

:: activate 스크립트 없이, 가상환경의 Python을 직접 실행 (보안 오류 해결)
"%VENV_PATH%\Scripts\python" -m streamlit run app.py

pause
