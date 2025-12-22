import sys
import os

print(f"Python Executable: {sys.executable}")
print(f"Current Working Directory: {os.getcwd()}")
print("System Path:")
for p in sys.path:
    print(f"  {p}")

try:
    print("Checking imports...")
    import streamlit
    print(f"Streamlit: OK ({streamlit.__file__})")
    import langchain_openai
    print(f"LangChain OpenAI: OK ({langchain_openai.__file__})")
    from analyzer import analyze_strategy
    print("Analyzer Module: OK")
    print("All critical imports passed.")
except ImportError as e:
    print(f"CRITICAL ERROR: {e}")
except Exception as e:
    print(f"ERROR: {e}")
