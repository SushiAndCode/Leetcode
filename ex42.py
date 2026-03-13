import numpy as np

class Student():
    def __init__(self,name: str, surname: str, grades: list):

        self.name = name
        self.surname = surname
        self.grades = grades

    def Average(self):
        return np.mean(self.grades) 
        

        