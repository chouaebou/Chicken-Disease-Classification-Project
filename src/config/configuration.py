from pathlib import Path
from src.constants import *
from src.utils.common import fn_read_yaml, fn_create_directories, fn_get_size
from src.entity.config_entity import (_DataIngestionConfig, 
                                      _PrepareBaseModelConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH):
        
        self.config = fn_read_yaml(config_filepath)
        self.params = fn_read_yaml(params_filepath)      
        
        fn_create_directories([self.config.artifacts_root])
        
    def fn_get_data_ingestion_config(self) -> _DataIngestionConfig:
        config = self.config.data_ingestion 
        
        fn_create_directories([config.root_dir])
        
        data_ingestion_config = _DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config
    
    def fn_get_prepare_base_model_config(self) -> _PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        fn_create_directories([config.root_dir])
        
        prepare_base_model_config = _PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )
        
        return prepare_base_model_config