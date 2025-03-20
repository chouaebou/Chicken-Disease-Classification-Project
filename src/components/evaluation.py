import tensorflow as tf
from pathlib import Path
from src.utils.common import fn_save_json
from src.entity.config_entity import _EvaluationConfig


class Evaluation:
    def __init__(self, config: _EvaluationConfig):
        self.config = config
        
    def fn_valid_generator(self):
        datagenerator_kwargs = dict(
            rescale=1./255,
            validation_split=0.30
        )
        
        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )
        
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )
        
    @staticmethod
    def fn_load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def fn_evaluation(self):
        model = self.fn_load_model(self.config.path_of_model)
        self.fn_valid_generator()
        self.score = model.evaluate(self.valid_generator)
        
    def fn_save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        fn_save_json(path=Path("scores.json"), data=scores)