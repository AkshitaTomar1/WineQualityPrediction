import os
from src.WineQualityPrediction import logger
from src.WineQualityPrediction.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config


    ##you can add ifferent data transformation techniques such as Scaler,PCA and all
    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_path)

        # spliting the data into training and test sets
        train,test=train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)