
import sys
from src.logging.logger import logging
from src.exception.exception import CustomException
from config.configuration import ConfigurationManager
from src.components.prepare_base_model import PrepareBaseModel


STAGE_NAME = "Data Ingestion stage"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.fn_get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.fn_get_base_model()
        prepare_base_model.fn_update_base_model()
        
        
# if __name__ == '__main__':
#     try:
#         logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        
#         object = PrepareBaseModelTrainingPipeline()
#         object.main()
        
#         logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx======")
#     except Exception as e:
#         raise CustomException(e, sys)