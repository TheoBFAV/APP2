from listes import *
from curiosity import *


def stop():
    input('Appuyer sur entrée pour continuer...')

def interprete (cur, prog, debug=False):

    # !!!!!! Je squizze prog pour tests !!!!
    #prog = Sequence()
    #chaine = "A 1M{DA8M{GGAAAD}{AG}?}"

    if debug:
        stop()

# Version temporaire a remplacer par
#   - une lecture des commandes dans la liste chainee
# suivie par
#   - une interpretation des commandes lues (partie fournie)

    
    #instructions = prog.getString()
    print ("INSTRUCTIONS = " ,prog.getString())
    
    debug = True
    #
    if debug:
        stop()
    # pour les commandes de prog lues en sequence:
    direction   = {"0" : "sur place"
                ,"1" : "devant lui"
                ,"2" : "devant lui à droite"
                ,"3" : "à droite"
                ,"4" : "derrière lui à droite"
                ,"5" : "derrière lui"
                ,"6" : "derrière lui à gauche"
                ,"7" : "à gauche"
                ,"8" : "devant lui à gauche"}
    
    prel        = {"0" : "rien"
                ,"1" : "une marque"
                ,"2" : "d'eau"
                ,"3" : "de pierre"}
    
    #Je dois réinterpreter chaque commande comme un bloc
    pile = Sequence()
    
    j = 1
    data = prog.tete
    while data != None :    
        liste = strToList(data.valeur)
        commandes = Sequence(liste)

        
        mesures = []
        cel = commandes.tete
        i = 1
        precedente = None
        while cel != None:
            if isValidLetter(cel.valeur[0]) :
                letter = cel.valeur[0]
                if len(cel.valeur) > 1:
                    restant = cel.valeur[1:len(cel.valeur)]
                    commandes.insertCellule(cel, data.suivant, restant)
                                     
                #----- DEPLACEMENTS -----
                if letter == 'A':
                    cur.avance()
                elif letter == 'G':
                    cur.gauche()
                elif letter == 'D':
                    cur.droite()        
                #----- MARQUE -- P ---
                elif letter == 'P':
                    instruction = pile.retire_tete()
                    if instruction == "0" :
                        cur.pose(False)
                    if instruction != "0" :
                        cur.pose(True)
                #----- MESURE -- M ---
                elif letter == 'M':
                    instruction = pile.retire_tete()
                    mesure = (cur.mesure(int(instruction)))
                    pile.insertion_tete(str(mesure))
                #----- CLONAGE -- C ---
                elif letter == 'C':
                    pile.insertion_tete(pile.getTete())
                #----- GROUPES DE COMMANDE {} -----
                elif letter == '{':
                    chaine = "A"
                    pile.insertion_tete(data.valeur)
                    #J'insere ma fin avant de breaker
                    i+=1
                    precedente = cel
                    cel = cel.suivant
                    #TESTS
                    valeur = "Pas de valeur"
                    if pile.tete != None :
                        valeur = pile.getString(",")
                    #-----
                    break
                elif letter == '}':
                    assert cel.valeur == '}'
                #----- EXECUTION -- ? -----
                elif letter == '?':
                    #Je recupere b, V, F dans l'ordre inverse
                    f = str(pile.retire_tete())
                    v = str(pile.retire_tete())
                    b = pile.retire_tete()

                    if isInt(b) and int(b) == 0:
                        #insérer f dans commandes
                        f = f[1:len(f)-1]
                        prog.insertCellule(data, data.suivant, f)
                        prog.afficheReste(data.suivant)
                        
                    elif b == None :
                        assert b == None
                    else :
                        #insérer v dans commandes
                        v = v[1:len(v)-1]
                        prog.insertCellule(data, data.suivant, v)
                        prog.afficheReste(data.suivant)
                #----- ECHANGE -- X ---
                elif letter == 'X':
                    premier = pile.retire_tete()
                    deuxieme = pile.retire_tete()
                    pile.insertion_tete(premier)
                    pile.insertion_tete(deuxieme)
                #----- EXECUTION IMMEDIATE -- ! ---
                elif letter == '!':
                    go = pile.retire_tete()
                    go = go[1:len(go)-1]
                    prog.insertCellule(data, data.suivant, go)
                #----- REBELLION ! -- B ---
                elif letter == 'B':
                    """  exécute cmd, décrémente n sans enlever B de la routine si n > 0.
                        Sinon enlève cmd et n de la pile, et B de la routine """
                    n = int(pile.tete.valeur)
                    if n > 0 :
                        pile.tete.valeur = int(pile.tete.valeur) -1
                        go = pile.tete.suivant.valeur
                        go = go[1:len(go)-1]
                        prog.insertCellule(data, data.suivant, "B")
                        prog.insertCellule(data, data.suivant, go)
                    else :     
                        pile.retire_tete()
                        pile.retire_tete()
                        
                #----- DANSE -- R ---
                elif letter == 'R':
                    """ effectue une « rotation » de x pas vers la gauche des n éléments
                        en haut de la pile : le haut de la pile """
                    x = int(pile.retire_tete())
                    n = int(pile.retire_tete())

                    attente = []

                    i = 0
                    while i < n :
                        attente.append(pile.retire_tete())
                        i += 1

                    i = 0
                    while i < x :
                        dernier = attente[n -1]
                        attente.pop(n - 1)
                        attente.insert(0, dernier)
                        i += 1

                    attente.reverse()

                    for e in attente :
                        pile.insertion_tete(e)
                        
                #----- BENNAGE de TETE -- I ---
                elif letter == 'I':
                    pile.retire_tete()
                    
            #----- EMPLISSAGE DE LA PILE -----        
            elif isInt(cel.valeur[0]) :
                pile.insertion_tete(cel.valeur[0])
                if len(cel.valeur) > 1:
                    restant = cel.valeur[1:len(cel.valeur)]
                    commandes.insertCellule(cel, data.suivant, restant)
            #----- CALCUL NPI VIDAGE DE LA PILE-----          
            elif isValidOperator(cel.valeur) :
                liste = []
                liste.append(pile.retire_tete())
                liste.append(pile.retire_tete())
                liste.reverse()
                
                res = calcule(liste, cel.valeur)
                npi = Cellule(res)

                npi.suivant = pile.tete
                pile.setTete(npi)
                
            else :
                print(" !!! ATTENTION !!! Caractere inconnu")
                print("====== " ,cel.valeur ,"=======")
                print("==============================")
            #---TESTS---
            valeur = "Pas de valeur"
            if pile.tete != None :
                valeur = pile.getString(",")

            print("Pile = " ,pile.getString(" "))
            #---Actions de fin de boucle---
            i+=1
            precedente = cel
            cel = cel.suivant
        #---Actions de fin de boucle---
        j += 1
        data = data.suivant


