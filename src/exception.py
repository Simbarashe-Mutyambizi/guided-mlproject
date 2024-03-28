# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:43:19 2024

@author: SWRM
"""

import sys  

#this is a global function to be used in the class below
def error_message_detail(error,error_detail:sys):
    #so error_detail will have the error message and information
    #the exc_tb will have the important details of the error like filename,line and message
    _,_,exc_tb=error_detail.exc_info()
    #extract the file with the error
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python file [{0}] line number [{1}] error message being [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    
    
    return error_message
##we are inheriting from the Exception class that gets created automatically when an error occurs
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message