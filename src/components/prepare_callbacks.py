import os
import time
import tensorflow as tf
from src.entity.config_entity import _PrepareCallbacksConfig


class PrepareCallback:
    def __init__(self, config: _PrepareCallbacksConfig):
        self.config = config        
        
    @property
    def fn_create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)    
    
    @property
    def fn_create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )        
        
    def fn_get_tb_ckpt_callbacks(self):
        return [
            self.fn_create_tb_callbacks,
            self.fn_create_ckpt_callbacks
        ]