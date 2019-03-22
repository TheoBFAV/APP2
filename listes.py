"""
Listes chaînées / Linked lists
"""


class Cellule:
    """
    Classe des cellules pour les listes chaînées.
    Chaque cellule contient deux champs:
    * valeur: stocke l'élément
    * suivant: référence vers la prochaine cellule (ou None)
    """

    def __init__(self, val):
        self.valeur = val
        self.suivant = None

    def libere(self):
        self.valeur = '_'


class Sequence:
    """
    Implantation d'une séquence à base de listes chaînées.
    À l'initialisation, une chaîne de caractère est donnée.

    Contient un seul champ:
    * tete: référence sur la première cellule de la liste
      (ou None si la liste est vide)
    """

    def __init__(self):
        self.tete = None

    def insertion_tete(self, n):
        cel = Cellule(n)
        cel.suivant = self.tete
        self.tete = cel

    def insertion_queue(self, n):
        queue = Cellule(n)
        cel = self.tete
        if self.tete == None :
            self.insertion_tete(n)
        else :
            while cel.suivant != None :
                cel = cel.suivant
            cel.suivant = queue

    def afficher(self):
        cel = self.tete
        while cel != None:
            print(cel.valeur, end=" ")
            cel = cel.suivant

    def getStr(self) :
        cel = self.tete
        commande = ""
        while cel != None :
            commande = commande + str(cel.valeur)
            cel = cel.suivant
        return commande

    def inPile(self, pile) :
        cel = self.tete
        cel_suivante = cel.suivant
        n = cel.valeur
        pile.insertion_queue(n)
        self.tete = cel_suivante
            

def conversion (texte):
    """
    Convertit le programme donne sous forme de texte en une sequence.

    !!! A FAIRE !!!

    Cette fonction doit renvoyer une Sequence.

    """
    seq = Sequence()
    texte.replace(" ","")
    texte.replace("\n","")
    for i in texte:
        seq.insertion_queue(i)

    return seq


testtext =     \
"{ 0M          \
  { G 0P }     \
  { D 1P }     \
  ? A          \
}              \
{ XC 32R !C! } \
C!"



#________________________________________________Tests______________________________________________
#
## Décommentez pour tester
#test_seq = conversion (testtext)
#print(test_seq)
#test_seq.afficher()
#print()
#print(test_seq.getStr())

""" seq = Sequence()
seq.insertion_tete(2)
seq.insertion_tete(6)
seq.insertion_tete(9)
seq.insertion_tete(4)
seq.insertion_tete(8)
seq.insertion_tete(5)
seq.insertion_tete(4)
seq.afficher()

print()

Pile = Sequence()
Pile.afficher()
print()

seq.inPile(Pile)
seq.afficher()
print()
Pile.afficher()
print()

seq.inPile(Pile)
seq.afficher()
print()
Pile.afficher()
print()

seq.inPile(Pile)
seq.afficher()
print()
Pile.afficher()
print()

seq.inPile(Pile)
seq.afficher()
print()
Pile.afficher() """




