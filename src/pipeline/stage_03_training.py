from src.logging.logger import logging
from src.components.training import Training
from src.exception.exception import CustomException
from config.configuration import ConfigurationManager
from src.components.prepare_callbacks import PrepareCallback
from src.components.prepare_base_model import PrepareBaseModel


STAGE_NAME = "Training stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.fn_get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.fn_get_tb_ckpt_callbacks()
        
        training_config = config.fn_get_training_config()
        training = Training(config=training_config)
        training.fn_get_base_model()
        training.fn_train_valid_generator()
        training.train(
            callback_list=callback_list
        )
            

# if __name__ == '__main__':
#     try:
#         logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        
#         object = TrainingPipeline()
#         object.main()
        
#         logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx======")
#     except Exception as e:
#         raise CustomException(e, sys)