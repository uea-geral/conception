from datetime import datetime
from json import loads

from flask import Flask, request
from flask_cors import CORS
from use_cases.extract_requirements import ExtractRequirementsUseCase
from use_cases.extract_requirements_file import ExtractRequirementsFileUseCase
from use_cases.generate_code import GenerateCodeUseCase

app = Flask(__name__)
CORS(app, origins=['*'])

@app.get("/")
def about():
    return {
        'title': 'Conception API',
        'version': '1.0',
        'now_is': datetime.strftime(datetime.now(), format="%d/%m/%Y %H:%M:%S")
    }

@app.post("/requirements/file/upload")
def extract_requirements():
    file = request.files['file']
    extract_requirements_use_case = ExtractRequirementsFileUseCase()
    requirements = extract_requirements_use_case.execute(file)
    return {
        'file': file.filename,
        'requirements': requirements
    }

@app.post("/requirements/prompt")
def extract_requirements_prompt():
    prompt = loads(request.data)['prompt']
    extract_requirements_use_case = ExtractRequirementsUseCase()
    requirements = extract_requirements_use_case.execute(prompt)
    print(requirements)
    return {
        'requirements': requirements
    }

@app.post("/requirements/generate/code")
def generate_code():
    requirements = loads(request.data)['requirements']
    last_code = loads(request.data)['past']
    generate_code_use_case = GenerateCodeUseCase()
    code = generate_code_use_case.execute(requirements, last_code)
    return {
        'code':code
    }