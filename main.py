#!/usr/bin/env python3

from interprete import *
from curiosity import *
import sys


# Arguments en dur sous l'éditeur Idle
if 'idlelib.rpc' in sys.modules:
    sys.argv.append ('tests/rotations.test')


    
def help():
    print ("Usage: ", sys.argv[0], " [-d] [-carte <n>] <fichier>")
    print ()
    print ("Options:")
    print ("\t-d\t\tmode debug")
    print ("\t-carte <n>\tUtiliser la carte <n> du fichier de test")
    print ("\t-ascii\tNe pas ouvrir de fenetre graphique")
    exit(1)

if len(sys.argv) < 2:
    help()


debug = False
ascii_mode = False
numero_carte = -1

arg = 1
while arg < len(sys.argv):
    if sys.argv[arg] == '-h':
        help()

    if sys.argv[arg] == '-d':
        debug = True
        arg += 1
        continue

    if sys.argv[arg] == '-carte':
        numero_carte = int(sys.argv[arg+1])
        arg += 2
        continue

    if sys.argv[arg] == '-ascii':
        ascii_mode = True
        arg += 1
        continue

    fichier = sys.argv[arg]
    print (fichier)
    f = open(fichier, 'r')
    arg += 1


# Une intance du robot Curiosity
cur = Curiosity(ascii_mode)


def launch(prog, carte, carte_num):
    """
    Lance l'interprétation du programme <prog> sur la carte <carte>.
    """

    if (prog != "" and carte != []) and \
       (numero_carte == -1 or numero_carte == carte_num):

        print ("Lancement du test...")
        print ("\tProgramme: ", prog)
        print ("\tCarte: ", "\n\t\t".join(carte))

        cur.reset (carte)
        try:
            prog_seq = conversion(prog)
            interprete (cur, prog_seq, debug)
        except CibleAtteinte:
            pass

        cur.attendre ()
        cur.affiche_carte_ascii ()
        if cur.succes ():
            print ("****************************************")
            print ("Carte ", carte_num, " passée avec succès")
            print ("****************************************")
        else:
            print ("****************************************")
            print ("Échec sur la carte ", carte_num)
            print ("****************************************")
            exit (1)


prog = ""
carte = []
carte_num = -1

# Lecture du fichier de test ligne par ligne

in_prog = None

for line in f:
    line = line.strip()
    if len(line) == 0:  # ligne vide
        continue
    if line[0] == '#':     # commentaire
        continue

    if line.startswith ('Pile'):
        continue # TODO: check stack content

    if line.startswith ('Programme'):
        # on lance le programme précédent sur la 
        # carte en cours, avant de démarrer un 
        # nouveau programme
        launch(prog, carte, carte_num)

        prog = ""
        carte = []
        in_prog = True
        continue

    if line.startswith ('Map'):
        launch(prog, carte, carte_num)

        carte_num = int(line[4])
        carte = []
        in_prog = False
        continue

    if in_prog == None:
        print ("Erreur:", line)
        continue

    if in_prog:
        prog += line
    else:
        carte.append (line)

# lance le dernier test
launch(prog, carte, carte_num)
