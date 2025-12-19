import subprocess
import sys

def run_fastapi():
    return subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "app.main:app",
            "--host", "0.0.0.0",
            "--port", "8000",
            "--reload"
        ]
    )

def run_streamlit():
    return subprocess.Popen(
        [
            "streamlit",
            "run",
            "streamlit_app/app.py",
            "--server.port", "8501",
            "--server.address", "0.0.0.0"
        ]
    )

if __name__ == "__main__":
    print("🚀 Starting FastAPI and Streamlit...")
    api = run_fastapi()
    ui = run_streamlit()

    api.wait()
    ui.wait()
