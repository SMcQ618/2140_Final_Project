from abc import ABC, abstractclassmethod
#needed to make an abstract class to make it easier

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
