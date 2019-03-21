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

    def getValeur(self) :
        if self.valeur != None :
            return self.valeur
        else :
            return "None"

    def getSuivant(self) :
        if self.suivant != None :
            return self.suivant
        else :
            return "None"

class Sequence:
    """
    Implantation d'une séquence à base de listes chaînées.
    À l'initialisation, une chaîne de caractère est donnée.

    Contient un seul champ:
    * tete: référence sur la première cellule de la liste
      (ou None si la liste est vide)
    """
    """
    def __init__(self):
        self.tete = None
    """

    def __init__(self, list_cel = None):
        if list_cel == None :
            self.tete = None
        else :
            cel = Cellule("")
            i = 0
            for e in list_cel :
                if i == 0 :
                    cel.valeur = e
                    self.tete = cel
                else :
                    suivant = Cellule(e)
                    cel.suivant = suivant
                    cel = suivant

                i += 1

    def afficheReste(self, debut) :
        """ Affiche les valeurs de la chaine
            a partir de debut"""
        chaine = ""
        
        cel = debut
        while cel != None:
            chaine += cel.valeur
            cel = cel.suivant
    
    def setTete(self, cel) :
        """ Definit une nouvelle tete à la sequence """
        self.tete = cel

    def getTete(self) :
        """ Definit une nouvelle tete à la sequence """
        return self.tete.valeur
        
    def getString(self, sep = ""):
        """ Retourne le contenu de la séquence sous
            forme de string"""
        chaine = ""
        
        cel = self.tete
        while cel != None:
            chaine += str((cel.valeur)) + sep
            cel = cel.suivant
        if sep != "" :
            chaine.rsplit(sep) #pourquoi ne fonctionne pas ? Mystère !
        return chaine

    def insertion_tete(self, n):
        """ Insert une nouvelle cellule en tete de
            la sequence """
  
        new_cel = Cellule(n)
        new_cel.suivant = self.tete

        self.tete = new_cel

    def insertCellule(self, debut, suivante, chaine):
        """ Insere des cellules entre precedente et suivante
            chaine contient les valeurs des cellules à inserer """
        suite = ""
        if suivante == None :
            suite = "None"
        else :
            suite = suivante.valeur

        chaine = traiteImbrication(chaine)

        commandes = chaine.split(" ")
        purgeListe(commandes, "")

        longueur = len(commandes)

        if longueur > 0 :
            i = 0
            precedente = None
            while i < longueur :
                cel = Cellule(commandes[i])
                if i == 0 :
                    debut.suivant = cel
                else :
                    precedente.suivant = cel
                    
                if i + 1 == longueur :
                    cel.suivant = suivante
                    
                precedente = cel
                i +=1
        
    def inversion(self):
        """ Inverse la chaine de la sequence """
        cel = self.tete
        prec = self.tete
        suivant = cel.suivant

        while cel != None : 
            suivant = cel.suivant
            if cel == self.tete :
                cel.suivant = None
                prec = cel
            else :
                cel.suivant = prec
                prec = cel         
                if suivant == None :
                    self.tete = cel
            cel = suivant

    def retire_tete(self):
        """ Supprime la tête de la sequence"""
        tete = self.tete
        
        if tete == None :
            return None
        
        valeur = tete.valeur
        suivant = tete.suivant
        self.tete = suivant
        
        return valeur

    def getTaille(self) :
        """ retourne la taille de la sequence """
        taille = 0

        cel = self.tete
        while cel != None:
            taille += 1
            cel = cel.suivant

        return taille
    
def traiteImbrication(texte) :
    """ insere des espaces dans texte pour séparer
        les différentes commandes de Curiosity
        retourne le texte traité"""

    texte = texte.replace(" ", "")
    
    ouvertures = 0
    new_texte = ""
    
    i = 0
    for c in texte :
        if c == "{" :
            if ouvertures == 0:
                new_texte += (" ")
                i += 1

            new_texte += c   
            ouvertures += 1
            
        elif c == "}" :
            new_texte += c
            ouvertures -= 1
            if ouvertures == 0:
                new_texte += (" ")
                i += 1

        elif isValidExecuteur(c) and ouvertures == 0:
                new_texte += (" ") + c + " "
                i += 2

        else :
            new_texte += c
        i += 1

    return new_texte

def conversion (texte):
    """
    Convertit le programme donne sous forme de texte en une sequence.
    Cette fonction doit renvoyer une Sequence.
    """

    #texte = texte.replace(" ", "")
    
    new_texte = traiteImbrication(texte)

    liste = new_texte.split(" ")

    purgeListe(liste, "")

    instructions = Sequence(liste)

    return instructions        
            
def strToList(chaine) :
    """ mets tous les caracs d'une chaine dans une liste """
    liste = []

    for c in chaine :
        liste.append(c)

    return liste
        
def isInt(c) :
    """ test si c est un int """
    try :
        int(c)
        return True 
    except :
        return False
    
def isValidOperator(c) :
    """ teste si c est un operateur autorisé """
    if c != None and c in ["+","-","*"] :
        return True 
    else :
        return False

def isValidLetter(c) :
    """ teste si c est une lettre autorisée """
    valides = ["A","G","D","P","M","C","{","}","?", "!","X", "B", "R", "I"]
    if c != None and c in valides :
        return True 
    else :
        return False

def isValidExecuteur(c) :
    """ teste si c est un symbole ou une lettre d'execution """
    valides = ["?", "!","X", "B", "R", "I"]
    if c != None and c in valides :
        return True 
    else :
        return False

def purgeListe(liste, chaine) :
    """ Supprime tous les elements d'une liste
        qui sont egaux à la chaine """
    i = 0
    while i < len(liste) :
        if liste[i] == chaine :
            liste.pop(i)
        i +=1

def calcule(liste, operateur) :
    """ Retourne le resultat sous forme de string de l'operation demandee """

    resultat = int(liste[0])
    deuxieme = 0

    try :
        deuxieme = int(liste[1])
    except :
        return resultat

    if operateur == "+" :
        resultat += deuxieme
    elif operateur == "-" :
        resultat -= deuxieme
    elif operateur == "*" :
        resultat *= deuxieme

    return resultat
