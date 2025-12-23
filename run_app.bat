@echo off
chcp 65001 > nul
cd /d "%~dp0"

echo ========================================================
echo 🚀 Project DEEP SCAN (Auto-Repair Mode)
echo ========================================================
echo.

:: 1. 가상환경 경로 감지
set VENV_PATH=..\venv
if exist "venv" set VENV_PATH=venv

echo [CHECK] 가상환경 위치: %VENV_PATH%

if not exist "%VENV_PATH%" (
    echo [ERROR] 가상환경을 찾을 수 없습니다.
    pause
    exit
)

:: 2. 필수 라이브러리 자동 설치/점검 (Self-Healing)
echo.
echo [INFO] 필수 라이브러리를 점검하고 설치합니다...
echo (시간이 조금 걸릴 수 있습니다. 잠시만 기다려주세요.)
"%VENV_PATH%\Scripts\pip.exe" install -r requirements.txt

:: 3. 앱 실행
echo.
echo [INFO] 모든 준비 완료! 앱을 실행합니다...
"%VENV_PATH%\Scripts\python.exe" -m streamlit run app.py

pause
