
import sys
from src.logging.logger import logging
from src.exception.exception import CustomException
from config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion


STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()    
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
        
# if __name__ == '__main__':
#     try:
#         logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        
#         object = DataIngestionTrainingPipeline()
#         object.main()
        
#         logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx======")
#     except Exception as e:
#         raise CustomException(e, sys)