class Produit:

    def __init__(self,nom,prix):
        self.nom=nom
        self.prix=prix
    def __repr__(self):
        return "nom: ({}) prix: ({} €)".format(self.nom, self.prix)