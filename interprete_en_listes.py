from listes import *
from curiosity import *

def isChiffre(c):
    if c == '0' or c == '1' or c =='2' or c == '3' or c == '4' or c =='5' or c == '6' or c == '7' or c =='8' or c == '9':
        return True
    else :
        return False

def stop():
    input('Appuyer sur entrée pour continuer...')

def interprete (cur, prog, debug=False):


    if debug:
        stop()

# Version temporaire a remplacer par
#   - une lecture des commandes dans la liste chainee
# suivie par
#   - une interpretation des commandes lues (partie fournie)
    print('Prog : ')
    prog.afficher()
    debug = True
    #
    if debug:
        stop()
    # pour les commandes de prog lues en sequence:
    liste_prog = list(prog.getStr())
    pile = list()
    while len(liste_prog)!= 0 :  # condition de boucle a remplacer
        c = liste_prog[0]
        if c == 'A':
            cur.avance()
            liste_prog.remove(c)
        elif c == ' ' :
            liste_prog.remove(c)
        elif c == 'G':
            cur.gauche()
            liste_prog.remove(c)
        elif c == 'D':
            cur.droite()
            liste_prog.remove(c)
        elif isChiffre(c) == True :
            pile.append(c)
            liste_prog.remove(c)
        elif c == '+' or c == '-' or c == '*':
            if len(pile) < 2 :
                print("Erreur : pas assez d'éléments dans la pile")
            else :
                n = len(pile) -1
                pile_1 = pile[n-1]
                pile_2 = pile[n]
                if c == '+' :
                    pile[n-1] = int(pile_1) + int(pile_2)
                elif c == '-' :
                    pile[n-1] = int(pile_1) - int(pile_2)
                elif c == '*' :
                    pile[n-1] = int(pile_1) * int(pile_2)
                pile.pop(n)
            liste_prog.remove(c)
        elif c == 'P' :
            n = len(pile)-1
            cur.pose(int(pile[n]))
            pile.pop(n)
            liste_prog.remove(c)
        elif c == 'M' :
            n = len(pile)-1
            mes = cur.mesure(int(pile[n]))
            pile[n] = mes
            liste_prog.remove(c)
        elif c == '{' :
            commande = ""
            commande = commande + c
            i = liste_prog.index(c)
            liste_prog.remove(c)
            ouvertures = 1
            while ouvertures > 0 :
                if liste_prog[i] == '{' :
                    ouvertures += 1
                elif liste_prog[i] == '}' :
                    ouvertures += -1
                pop = liste_prog.pop(i)
                commande = commande + pop
            pile.append(commande)
        elif c == '}' :
            liste_prog.pop(liste_prog.index(c))
        elif c == '?' :
            liste_prog.remove(c)
            n = len(pile) -  1
            if pile[n-2] != 0 and pile[n-2] != '0':
                commande = list(pile.pop(n-1))
                n = len(pile) -  1
                pile.pop(n)
                n = len(pile) -  1
                pile.pop(n)
                l_c = len(commande) -1
                for i in range(l_c-1,0,-1) :
                    liste_prog.insert(0,commande[i])
            else :
                commande = list(pile.pop(n))
                n = len(pile) -  1
                pile.pop(n)
                n = len(pile) -  1
                pile.pop(n)
                l_c = len(commande) -1
                for i in range(l_c-1,0,-1) :
                    liste_prog.insert(0,commande[i])
        elif c == 'X' :
            n = len(pile)-1
            pile_1 = pile[n-1]
            pile[n-1] = pile[n]
            pile[n] = pile_1
            liste_prog.remove(c)
        elif c == '!' :
            liste_prog.remove(c)
            n = len(pile)-1
            pop = pile.pop(n)
            pop = list(pop)
            if pop[0]!= '{' :
                liste_prog.insert(0,pop)
            else :
                l_pop = len(pop) -1
                for i in range(l_pop-1,0,-1) :
                    liste_prog.insert(0,pop[i])
        elif c == 'B' :
            n = len(pile)-1
            if int(pile[n]) >0 :
                cmd = pile[n-1]
                cmd = list(cmd)
                if cmd[0] != '{' :
                    liste_prog.insert(0,cmd)
                else :
                    l_cmd = len(cmd)-1
                    for i in range(l_cmd-1,0,-1):
                        liste_prog.insert(0,cmd[i])
                pile[n]= int(pile[n])-1
            else :
                pile.pop(n)
                pile.pop(n-1)
                liste_prog.remove(c)
        elif c == 'R' :
            l=len(pile)-1
            x = int(pile.pop(l))
            n = int(pile.pop(l-1))
            liste_prog.remove(c)
            l=len(pile)
            while x > 0 :
                a_n = pile.pop(l-n)
                pile.append(a_n)
                x += -1
        elif c == 'C' :
            liste_prog.remove(c)
            n = len(pile)-1
            pile.append(pile[n])
        elif c== 'I' :
            liste_prog.remove(c)
            n = len(pile)-1
            pile.pop(n)
        else :
            print("Erreur : caractère inconnu : ", c)
            liste_prog.remove(c)
        print('Pile : ', pile)
        print()
        print('Prog : ', liste_prog)
        print()
    print('Pile : ', pile)
    print()
    print('Prog : ', " ".join(liste_prog))
    print()

""" prog= Sequence()
prog.insertion_queue('2')
prog.insertion_queue('3')
prog.insertion_queue('*')
prog.insertion_queue('3')
prog.insertion_queue('4')
prog.insertion_queue('+')
prog.insertion_queue('*')
interprete(prog) """

