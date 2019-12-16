from exo2.voiture import Voiture
from exo1.RenaultClio import RenaultClio
from exo2.bus import Bus
from exo3.produit import Produit
from exo3.customer import Client
from exo3.employe import Employe
from exo3.person import Person


""" creation de l'employé"""
employe=Employe("turk","nicolas",34)
print(employe)
employe.statut="manager"
print(employe)
employe=Employe("kamel","aniche",44)
print(employe)
employe.statut="manager"
print(employe)






"""affichage"""
print(employe>="cadre")
