import sys
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.pipeline.stage_03_training import ModelTrainingPipeline
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


# Data ingestion stage
STAGE_NAME = "Data ingestion stage"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx======")
except Exception as e:
    raise CustomException(e, sys)

# Prepare base model stage
STAGE_NAME = "Prepare base model"
try:
    logging.info("***************************************")
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx======")
except Exception as e:
    raise CustomException(e, sys)

# Training stage
STAGE_NAME = "Training"
try:
    logging.info("***************************************")
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    
    prepare_base_model = ModelTrainingPipeline()
    prepare_base_model.main()
    
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx======")
except Exception as e:
    raise CustomException(e, sys)