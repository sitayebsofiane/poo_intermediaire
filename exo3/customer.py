from exo3.person import Person
from exo3.produit import Produit

class Client(Person):

    def __init__(self,nom,prenom,age):
        Person.__init__(self,nom,prenom,age)
        self.__panier=list()
        self.__total=0

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self,value):
        self.__total+=value

    def __add__(self, produit):
        self.__panier.append(produit)
        self.total=produit.prix

    def __repr__(self):
        return Person.__repr__(self)+" il a acheté ces produits {} ".format(self.__panier)

