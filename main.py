from Network_security.components.data_ingestion import DataIngestion
from Network_security.components.data_validation import DataValidation
from Network_security.components.data_transformation import DataTransformation
from Network_security.exception.exception import NetworkSecurityException
from Network_security.logging.logger import logging
from Network_security.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from Network_security.entity.config_entity import TrainingPipelineConfig

 

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)

        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)

        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        logging.info("Initiate the data Tranformation")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("data Transformation Completed")
        print(data_transformation_artifact)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)