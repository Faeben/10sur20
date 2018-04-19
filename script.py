#Exercice 1 écrire un programme qui affiche 500 fois "je dois faire des sauvegardes réguliéres de mes fichiets"

'''
def exo1():
    i = 0
    while i <= 500:
        print("je dois faire des sauvegardes réguliéres de mes fichiers")
        i = i + 1

exo1()


def exo1bis():
    for i in range(500):
        print("je dois faire des sauvegardes réguliéres de mes fichiers")

exo1bis()
'''

#Exercice 2 écrire un programme qui affiche tous les nombres impairs entre 0 et 1000, par ordre croissant: "1 3 5 7 ... 995 997 999"

'''
def exo2():
    i = 1
    while i < 999:
        i = i + 2
        print(i)

exo2()
'''

#03 Écrire un programme qui affiche la table de multiplication par 13

'''
def exo3():
    nbr = 13
    i = 0
    for i in range(10):
        i = i + 1
        somme = nbr * i
        print(nbr, "*", i, "=", somme )

exo3()
'''

#04 Écrire un programme qui demande un mot à l’utilisateur et qui affiche à l’écran le nombre de lettres de ce mot.

'''
def exo4():
    print(len(input("dis moi un mot")))

exo4()
'''

#05 Ecrire un programme qui demande un nombre entier à l’utilisateur. L’ordinateur affiche ensuite le message "Ce nombre est pair" ou "Ce nombre est impair" selon le cas.

'''
def exo5():
    nbr = int(input("Donne moi un nombre"))
    if nbr %2 == 0:
        print("¨Pair")
    else:
        print("Impair")

exo5()
'''

#06 Ecrire un programme qui demande un nombre compris entre 10 et 20, jusqu’à ce que la réponse convienne. En cas de réponse supérieure à 20, on fera apparaître un message : « Plus petit ! », et inversement, « Plus grand ! » si le nombre est inférieur à 10.

'''
def exo6():
    nbr = int(input("Donne moi un nombre entre 10 et 20"))
    while(nbr< 10 or nbr > 20):
        if nbr < 10:
            print("Plus grand !")
        elif nbr > 20:
            print("Plus petit !")
        nbr = int(input("Donne moi un nombre entre 10 et 20"))
    print("Nice !")

exo6()
'''

#07 Ecrire un programme qui demande un nombre de départ, et qui ensuite affiche les dix nombres suivants. Par exemple, si l'utilisateur entre le nombre 17, le programme affichera les nombres de 18 à 27.

'''
def exo7():
    nbr = int(input("Donne moi un nombre"))
    for i in range(10):
        nbr = nbr + 1
        print(nbr)


exo7()
'''

#08 Ecrire un programme qui demande un nombre de départ, et qui ensuite écrit la table de multiplication de ce nombre.

'''
def exo8():
    nbr = int(input("Donne moi un nombre"))
    i = 0
    for i in range(10):
        i = i + 1
        somme = nbr * i
        print(nbr, "*", i, "=", somme)

exo8()
'''

'''
def exo9():
    nbr = int(input("Donne moi un chiffre"))
    count = 0
    for i in range(nbr + 1):
        count = i + count
    print(count)

exo9()
'''

'''
def exo10():
    nbr = int(input("TA KEL AGE WSH"))
    if nbr == 6 or nbr == 7:
        print ("Bébé Zoulou")
    elif nbr == 8 or nbr == 9:
        print ("Enfant Zoulou")
    elif nbr == 10 or nbr == 11:
        print ("Moyen Zoulou")
    elif nbr >= 12:
        print ("Zoulou apprentit")
    else:
        print ("Trop petit Zoulou")

exo10()
'''

'''
def exo11():
    nbr = int(input("Combien as tu d'articles?"))
    euro = int(input("Combien coutent t'ils à l'unité?"))
    prixht = nbr*euro
    tva = prixht * 1.20
    print("Nombre d'articles:", nbr)
    print("Prix HT :", nbr*euro)
    print("Prix TTC :", tva)

exo11()
'''



def exo100():
    nbr = int(input("Combien as tu d'articles?"))
    dif = int(input("As tu des articles différents?"))
    if dif ==

    elif dif ==
        euro = int(input("Combien coutent t'ils à l'unité?"))
        prixht = nbr * euro
        tva = prixht * 1.20
        print("Nombre d'articles:", nbr)
        print("Prix HT :", nbr * euro)
        print("Prix TTC :", tva)

   

exo100()

