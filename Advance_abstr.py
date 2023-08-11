from abc import ABC, abstractclassmethod

class Calculations:
    @staticmethod
    @abstractclassmethod
    def mean(self):
        pass
    
    @staticmethod
    @abstractclassmethod
    def median(self):
        pass

    @staticmethod
    @abstractclassmethod
    def mode(self):
        pass