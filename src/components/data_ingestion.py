# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:37:06 2024

@author: SWRM
"""

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


#the first class with create the paths to the three
# we use this @dataclass when we just create variables without functions
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifacts","train.csv")
    test_data_path: str=os.path.join("artifacts","test.csv")
    raw_data_path: str=os.path.join("artifacts","data.csv")
    
class DataIngestion:
    def __init__(self):
        #created object to the first class
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered into the data ingestion operation")
        try:
            df=pd.read_csv("C:/Users/SWRM/Music/Projects/guided mlproject/data folder/StudentsPerformance.csv")
            logging.info("The data has been read to a dataset")
            
            #make the folder artifacts
            #os.path.dirname() gets the folder name in the path
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("Starting the train test split of our raw data")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("The ingestion has been completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                
                )
            
            
        except Exception as e:
            raise CustomException(e,sys)
            
        
    