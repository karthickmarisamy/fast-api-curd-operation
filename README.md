# fast-api-curd-operation
FastApi python CURD operation with mysql

# Create an env
    conda create -p venv python==3.7
# Activate env
    conda activate fastapi-curd-mysql/venv
# Deactivate env
    conda deactivate
# Installation
   
## Direct installation
    pip install fastapi uvicorn pydantic mysql-connector-python
    
## Using requirements.txt

    pip install -r requirements.txt
## Run the application
    uvicorn main:app --reload