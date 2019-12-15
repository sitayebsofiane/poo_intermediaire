from voiture import Voiture
from RenaultClio import RenaultClio
from bus import Bus
c=RenaultClio()
print(c.get_number_doors())
c.set_color("noire")
print("colors",c.get_color())
v=Voiture("49-fs-75","red")
b=Bus("14-sq-59","yellow")
v.number_dors=3
b.number_floors=5
print(v.number_dors)
print(b.number_floors)