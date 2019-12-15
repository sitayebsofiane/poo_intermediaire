class Person:

    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age

    def __repr__(self):
        return "nom: ({}) prenom: ({}) age: ({})".format(self.nom, self.prenom, self.age)