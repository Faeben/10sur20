Exo01
'''
def exo01():
	i=0
	while i <= 500:
		print "Je dois faire des sauvegardes régulières de mes fichiers."
		i = i + 1
'''

Exo02
'''	
Exo 2 
def exo02():
	for i in range(0,1000):
		if i % 2 != 0:
			print i
'''

Exo03
'''
def exo03():
	i=0
	while i <= 10:
		print i*13
		i=i+1
'''

Exo04
'''
def exo04():
	mot=raw_input("Merci de saisir un mot : ")
	print len(mot)
'''

Exo05
'''
def exo05():
	nombre=int(raw_input("Merci de saisir un nombre entier : "))
	if nombre % 2 != 0:
		print "Votre nombre est impair."
	else:
		print "Votre nombre est pair."
'''

Exo06
'''
def exo06():
	nombre1=int(raw_input("Entrez un nombre entre 10 et 20 :"))
	if nombre1 < 10:
		print "Plus grand!!"
		exo06()
	if nombre1 > 20:
		print "Plus petit!!"
		exo06()
	print "ok"
'''

Exo07
'''
def exo07():
	user_input = int(raw_input("Entrez un nombre entier: "))
	print range(int(user_input)+1, int(user_input)+11)

def exo08():
	nb = int(raw_input("Entrez un nombre entier :"))
	for i in range(1,11):
		print i , "*", nb , "=", i*nb
'''

Exo09
'''
def exo09():
	nombre=int(raw_input("entrer votre nombre"))
	liste=[]
	for i in range(0,nombre+1,1):
		liste.append(i)
	print sum(liste)
'''

Exo10
'''
def exo10():
	nombre=int(raw_input("entrer votre nombre : "))
	if nombre >= 6 and nombre <= 7:
		print "Vous etes poussin !"
	elif nombre >= 8 and nombre <= 9:
		print "Vous etes pupille !"
	elif nombre >= 10 and nombre <= 11:
		print "Vous etes minime !"
	elif nombre > 12:
		print "Vous etes Cadet !"
'''

Exo 11
'''
def exo11():
	i=0
	nbreArticle=int(raw_input("Combien avez-vous d'articles ? "))
	tableau=[]
	while i!=nbreArticle:
		i+=1
		prixHT=float(raw_input("Combien coûte l'article ? "))
		tableau.append(prixHT)

	ttc=1.20
	total=sum(tableau)

	print("Nombre d'articles : ", nbreArticle)
	print(tableau)
	print("Prix HT : ", total)
	print("Prix TTC : ", ttc*total)
'''