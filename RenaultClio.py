class RenaultClio:

    doors=[3,5]
    colors={"noire":"213800058","blanc":"213800059","violet":"213800060","rouge":"213800061","marron":"213800062"}
    price=range(8000,30001)

    def __init__(self):
        self._number_doors=None
        self._color_number=None
        self._color=None

    def get_number_doors(self):
        return self._number_doors

    def set_number_doors(self,new_number_doors):
        if new_number_doors in RenaultClio.doors:
            self._number_doors=new_number_doors



