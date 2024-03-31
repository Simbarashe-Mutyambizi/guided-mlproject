# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:38:57 2024

@author: SWRM
"""
import os
import sys
from dataclasses import dataclass

#models
from catboost import CatBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBRegressor

#external functionss
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models


#create a file to store the model
@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
        
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting train and test data in our model trainer")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1])
            
            models={"Linear Regression":LinearRegression(),
                    "CatBoostRegressor":CatBoostRegressor(verbose=False),
                    "KNN":KNeighborsClassifier(),
                    "XGBoost":XGBRegressor()}
            
            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)
            
            #get the best mode score
            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]
            
            if best_model_score <0.6:
                raise CustomException("No best model better than 0.6")
            
            logging.info("Best model found")
            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
                )
            
            predicted=best_model.predict(X_test)
            r2_scores=r2_score(y_test,predicted)
            return r2_scores
            #return best_model_name
        except Exception as e:
            raise CustomException(e,sys)
     
