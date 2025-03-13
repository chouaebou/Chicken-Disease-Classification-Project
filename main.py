import sys
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


logging.info("Welcome to my custom log")

STAGE_NAME = "Data Ingestion stage"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    
    object = DataIngestionTrainingPipeline()
    object.main()
    
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx======")
except Exception as e:
    raise CustomException(e, sys)