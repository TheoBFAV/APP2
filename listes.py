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
        self.valeur='_'


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

    def afficher(self):
        cel = self.tete
        while cel != None:
            print(cel.valeur, end=" ")
            cel = cel.suivant

    
    def insertion_queue(self, n):
    
        cel=Cellule(n)
        x=self.tete
        
        if x==None:
            
            self.tete=cel
            
        else:
        
            while x.suivant!=None:
            
                x=x.suivant
        
            x.suivant=cel

    def insertion_tete(self, n):
    
        cel=Cellule(n)
        cel.suivant=self.tete
        self.tete=cel

        

def conversion (texte):
    """
    Convertit le programme donne sous forme de texte en une sequence.

    !!! A FAIRE !!!

    Cette fonction doit renvoyer une Sequence.

    """

    seq=Sequence()

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

#
## Décommentez pour tester
test_seq = conversion (testtext)
print (test_seq)

