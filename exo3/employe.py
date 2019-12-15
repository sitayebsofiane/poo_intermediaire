from exo3.person import Person
class Employe(Person):

    def __init__(self,nom,prenom,age):
        Person.__init__(self,nom,prenom,age)
        self.__statut="employé"

    @property
    def statut(self):
        return self.__statut
    @statut.setter
    def statut(self,statut):
        if statut in ["employé","technicien","manager","cadre"]:
            self.__statut=statut
        else:
            raise ValueError("le statut {} n'existe pas".format(statut))

    def __ge__(self, statut):
        if self.statut=="cadre":return True
        elif self.statut=="manager" and statut != "cadre":return True
        elif self.statut=="technicien" and statut != "cadre" and statut != "manager" :return True
        elif self.statut==statut:return True
        else:return False


    def __repr__(self):
        return "nom: ({}) prenom: ({}) age: ({}) sont statut {}".format(self.nom, self.prenom, self.age,self.__statut)