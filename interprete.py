from listes import *
from curiosity import *


def stop():
    input('Appuyer sur entrée pour continuer...')

def interprete (cur, prog, debug=False):


    if debug:
        stop()
        
    pile=[]
    routine=Sequence()
    routine=prog
    ouverture=0
    c=prog.tete.valeur
        

# Version temporaire a remplacer par
#   - une lecture des commandes dans la liste chainee
# suivie par
#   - une interpretation des commandes lues (partie fournie)

    debug = True
    #
    if debug:
        stop()
    # pour les commandes de prog lues en sequence:
    while True:

        if c == 'A':
            cur.avance()
            
        elif c == 'G':
            cur.gauche()
            
        elif c == 'D':
            cur.droite()
            
        elif c=='-':

            l=len(pile)

            pile[l-2]=pile[l-2]-pile[l-1]

            pile.pop()

        elif c=='+':
            
            l=len(pile)

            pile[l-2]=pile[l-2]+pile[l-1]

            pile.pop()

            

        elif c=='*':

            l=len(pile)

            pile[l-2]=pile[l-2]*pile[l-1]

            pile.pop()
            

        elif c.isdigit():
                
            nouveau_chiffre=int(c)

            pile.append(nouveau_chiffre)

        elif c=='M':

            l=len(pile)
            valeur_sortie=cur.mesure(pile[l-1])
            pile[l-1]=valeur_sortie
            

        elif c=='P':
            
            l=len(pile)
            
            if pile[l-1]!=0:
                
                booleen=True

            else:

                booleen=False
                
            cur.pose(booleen)

            pile.pop()

        elif c=='C':

            l=len(pile)
            pile.append(pile[l-1])

        elif c=="{":
            
            a=""

            ouverture+=1
            
            while ouverture>0 :
                
                routine.tete=routine.tete.suivant

                a=a+routine.tete.valeur

                check_1=list(a)

                if check_1[len(check_1)-1]=="}":

                    ouverture-=1

                if check_1[len(check_1)-1]=="{":

                    ouverture+=1

            cmd=""

            for i in range(len(check_1)):

                cmd=cmd+check_1[i]

            pile.append(c+cmd)

            c=routine.tete.valeur

            continue

        elif c=="?":

            l=len(pile)

            if pile[l-3] != 0:

                routine.tete=routine.tete.suivant

                routine.insertion_tete(pile[l-2])
                
                   
            else:

                routine.tete=routine.tete.suivant

                routine.insertion_tete(pile[l-1])

            if l>3:
                

                for k in range(l-3, l):

                    pile.pop()

            else:

                pile=[]

            commande=list(routine.tete.valeur)

            routine.tete=routine.tete.suivant

            if len(commande)>1 :

                for k in range(len(commande)-2, 0, -1):

                    routine.insertion_tete(commande[k])

                c = routine.tete.valeur

                    

            else:

                c=routine.tete.valeur

            continue

        elif c== "X":

            a=pile[len(pile)-2]
            pile[len(pile)-2]=pile[len(pile)-1]
            pile[len(pile)-1]=a

        elif c=="!":

            routine.tete=routine.tete.suivant

            commande=list(pile.pop(len(pile)-1))

            if len(commande)>1:

                for k in range(len(commande)-2, 0, -1):

                    routine.insertion_tete(commande[k])

            c=routine.tete.valeur

            continue

        elif c=="I":

            pile.pop()

        elif c=="B":

            k=pile[len(pile)-1]

            if k>0:

                a=pile.pop()

                pile.append(a-1)

                commande=list(pile[len(pile)-2])

                if len(commande)>1:

                    for k in range(len(commande)-2, 0, -1):

                        routine.insertion_tete(commande[k])

                    c=routine.tete.valeur

                else:
                    c=routine.tete.valeur


                continue

            if k==0:

                pile.pop()
                pile.pop()
                routine.tete=routine.tete.suivant
                c=routine.tete.valeur
                
                continue

        elif c=="R":

            x=pile.pop()

            n=pile.pop()

            petite_pile=[]

            for k in range(n):

                petite_pile.append(pile.pop())

            petite_pile.reverse()

            for i in range (x):
                    
                petite_pile.append(petite_pile.pop(0))
                
            for k in range(len(petite_pile)):

                pile.append(petite_pile[k])

        prog.tete=routine.tete

        if routine.tete.suivant==None and routine.tete !=None:
            c=routine.tete.valeur
            
            continue

        elif routine.tete==None :
            
            break

        else:

            routine.tete=routine.tete.suivant

            c=prog.tete.valeur



