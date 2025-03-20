import sys
from src.logging.logger import logging
from src.components.training import Training
from src.components.evaluation import Evaluation
from src.exception.exception import CustomException
from config.configuration import ConfigurationManager


class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        val_config = config.fn_get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.fn_evaluation()
        evaluation.fn_save_score()


STAGE_NAME = "Evaluation stage"

if __name__ == '__main__':
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        
        object = EvaluationPipeline()
        object.main()
        
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx======")
    except Exception as e:
        raise CustomException(e, sys)