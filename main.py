from exo2.voiture import Voiture
from exo1.RenaultClio import RenaultClio
from exo2.bus import Bus
from exo3.produit import Produit
from exo3.customer import Client
from exo3.employe import Employe
"""
c=RenaultClio()
print(c.get_number_doors())
c.set_color("noire")
print("colors",c.get_color())
v=Voiture("49-fs-75","red")
b=Bus("14-sq-59","yellow")
v.number_dors=3
b.number_floors=1
print(v.number_dors)
print(b.number_floors)
"""
"""
exercise three

"""
""" creation de produit et du client"""
product=Produit("tomate",1.2)
customer=Client("harlein","bruno",40)
""" creation de l'employé"""
employe=Employe("turk","nicolas",34)
print(employe)
""" ajout d'un produit au panier"""
customer + product
"""affichage"""
print(customer.total)
employe.statut="manager"
print(employe>="technicien")
print(customer)