from exo2.vehicule import Vehicule
class Voiture(Vehicule):


    def __init__(self,immatriculation,color):
        Vehicule.__init__(self,immatriculation,color)
        self.__number_dors=None
    @property
    def number_dors(self):
        return self.__number_dors
    @number_dors.setter
    def number_dors(self,new_value):
        if new_value in [3,4,5]:
            self.__number_dors=new_value
        else:
            raise ValueError("le nombre de porte doit etre 3,4 ou 5")

