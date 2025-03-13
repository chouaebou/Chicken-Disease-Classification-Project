import os
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s]: %(message)s"
)

list_of_files = [
    ".github/worflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/exception/__init__.py",
    "src/exception/exception.py",
    "src/logging/__init__.py",
    "src/logging/logger.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/pipeline/__init__.py",
    "src/entity/__init__.py",
    "src/constants/__init__.py",
    "logs",
    "raw_files",
    "artifacts",
    "templates/index.html",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    print(filedir, ' : ', filename)
    if filename == ".gitkeep":
        os.makedirs(".github/worflows/.gitkeep", exist_ok=True)
    else:       
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir} for the file {filename}")        
        
        if ((not os.path.exists(filepath) or (os.path.getsize(filepath == 0))) and (Path(filename).suffix)):
            with open(filepath, "w") as f:
                pass
                logging.info(f"Creating file: {filepath}")
                
        elif (not os.path.exists(filepath) and (not Path(filename).suffix)):            
            os.makedirs(filename, exist_ok=True)
            logging.info(f'Creating empty directory: {filename}')
        
        else:
            logging.info(f"{filename} is already exist.")