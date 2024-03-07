import os 
from pathlib import Path 

project_name = 'visa_approval'

list_of_files = [
    f"{project_name}/__ini__.py",

    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",

    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongodb_connector.py",
    # f"{project_name}/configuration/model.yaml",
    # f"{project_name}/configuration/schema.yaml",

    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/usvisa_data.py",


    f"{project_name}/constant/__init__.py",

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",

    f"{project_name}/exception/__init__.py",

    f"{project_name}/logger/__init__.py",

    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/pipeline/train_pipeline.py",
    
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    'app.py',
    'requirements.txt',
    'Dockerfile',
    '.dockerignore',
    'demo.py',
    'setup.py',
    'notebook/eda.ipynb',
    'config/model.yaml',
    'config/schema.yaml'
]


for filepath in list_of_files:
    file=Path(filepath)
    filedir, filename = os.path.split(file)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        print(f"creating file at; {file}")
        with open(file, 'w') as f:
            pass 
    else:
        print(f"file is alreay present at; {file}")




