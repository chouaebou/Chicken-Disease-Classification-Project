import sys
from src.logging.logger import logging
from src.exception.exception import CustomException
from config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.fn_get_data_ingestion_config()    
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.fn_download_file()
        data_ingestion.fn_extract_zip_file()
   
     
STAGE_NAME = "Data Ingestion stage"
     
if __name__ == '__main__':
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        
        object = DataIngestionTrainingPipeline()
        object.main()
        
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx======")
    except Exception as e:
        raise CustomException(e, sys)