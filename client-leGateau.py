#!/usr/bin/env python3

from lib.Network import *

# Affiche les échanges avec le serveur (false pour désactiver)
debug_mode (True)

print ("""Bienvenue dans cette introduction à AppoLab !

AppoLab est un serveur d'exercices algorithmiques que vous allez devoir 
utiliser pour vos APPs. Je vais vous guider pas à pas pour que vous 
puissiez vous débrouiller tout·e seul·e.""")

attendre()

print ("""
Le client va maintenant tenter de se connecter automatiquement au serveur 
AppoLab. Il vous faut bien entendu pour cela une connection internet.
(En cas d'erreur, éditez le fichier python et modifiez la ligne 
'connexion' comme indiqué dans le commentaire.)""")
attendre()

# En cas de problème, essayer sur le port 443 en utilisant à la place la ligne 
# ci-dessous
# connexion ("im2ag-sncf.u-ga.fr", 443)
connexion ()

print ("""
Si tout va bien, vous devez avoir reçu le message de bienvenue d'AppoLab. Si 
non, arrêtez ce programme (avec Ctrl-C) et demandez de l'aide à un·e 
enseignant·e.""")

attendre()

print ("""
Comme indiqué, commencez par vous loguer avec l'identifiant et le mot de 
passe qui vous ont été fournis. Entrez les au clavier ainsi : 
login toto 12345678""")

while True:
    attendre_message()
    login = "login DABeard 1634"
    if login == "":
        print ("Là il faut taper au clavier bande de feignasses !")
        continue

    reponse = envoyerRecevoir(login)

    if "Veuillez d'abord" in reponse:
        print ("Vous devez utiliser la commande 'login'")

    elif "incorrect" in reponse:
        print ("Vu avez du vous tromper dans vos identifiants, réessayez...")

    elif "Bienvenue" in reponse:
        break


print ("""
Bravo, vous venez de vous identifier auprès du serveur !
Comme vous pouvez le voir ce programme trace tout ce que vous envoyez au 
serveur sur les lignes commençant par <<<envoi<<<, et tout ce que répond le 
serveur sur des lignes commençant par >>>recu >>>.""")

attendre()

print ("""
Vous êtes maintenant prêt·e à lancer le premier exercice qui se nomme 'tutoriel'.
Lancez le grâce à la commande 'load' ainsi :
load tutoriel""")

while True:
    attendre_message()
    load = "load leGateau"
    if load == "":
        print ("Là il faut taper au clavier bande de feignasses !")
        continue

    reponse = envoyerRecevoir(load)
    break

print ("""
Voilà, vous venez de lancer votre premier exercice...
Suivez les consignes de l'exercice maintenant.""")

attendre_message()
message='depart'
reponse = envoyerRecevoir(message)
i=1
while True:
    attendre_message()
    reponse = list(reponse)
    n = len(reponse)
    message = ""
    i+=1
    if i < 50 :
        message = reponse[n-6] + reponse[n-5] + reponse[n-4] + reponse[n-3] + reponse[n-2]
        reponse = envoyerRecevoir(message)
    else :
        message = reponse[n-19] + reponse[n-18] + reponse[n-17] + reponse[n-16] + reponse[n-15]
        reponse = envoyerRecevoir(message)
        break


attendre()
print ("Au revoir.")
deconnexion()
