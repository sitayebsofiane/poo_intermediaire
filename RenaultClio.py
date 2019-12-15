class RenaultClio:

    doors=[3,5]
    colors={"noire":"213800058","blanc":"213800059","violet":"213800060","rouge":"213800061","marron":"213800062"}
    price=range(8000,30001)

    def __init__(self):
        self.__number_doors=None
        self.__color_number=None
        self.__color=None

    def get_number_doors(self):
        return self.__number_doors

    def set_number_doors(self,new_number_doors):
        if new_number_doors in RenaultClio.doors:
            self.__number_doors=new_number_doors

    def get_color_number(self):
        return self.__color_number

    def set_color_number(self,new_number_doors):
        if new_number_doors in RenaultClio.colors.values():
            self.__color_number=new_number_doors

    def get_color(self):
        return self.__color

    def set_color(self,new_color):
        if new_color in RenaultClio.colors:
            self.__color=new_color



