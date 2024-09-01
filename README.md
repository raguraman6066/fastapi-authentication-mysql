Fastapi

Set environment
-cd path/to/your/project_name
-python3 -m venv my_env_name

Activate 
-source my_env_name/bin/activate

Install
-pip install fastapi
-pip install "uvicorn[standard]"


Run server
-uvicorn main:app --reload
