# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:19:57 2024

@author: SWRM
"""

from setuptools import find_packages,setup
from typing import List

'''
find_packages is used to look through you project's folder
for valid packages, which are folder that have
__init__.py
'''

HYPEN_E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
            

setup(
      name="guided mlproject",
      version="0.0.1",
      author="Simbarashe Mutyambizi",
      author_email="simbarashewilliammutyambizi@gmail.com",
      packages=find_packages(),
      install_requires=get_requirements("requirements.txt")
      
      
      
      
      )