#!/usr/bin/python
#Jan Horbowicz
import os
import random

#klasa kart
class karta():
	#konstruktor
	def __init__(self,kolor,figura):
		self.kolor = kolor
		self.figura = figura
	kolory = ['trefl','karo','pik','kier']
	figury = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'walet':2,'dama':3,'krol':4,'as':11}
	@staticmethod
	def NowaTalia():
		allcards,c=[],0
		for a in karta.figury.keys():
			for b in karta.kolory:
				allcards.append(karta(b,a))
				c=c+1 
		return allcards

#klasa graczy
class gracz():
	def __init__(self, Imie, Nazwisko, karty_w_reku):
		self.Imie = Imie
		self.Nazwisko = Nazwisko
		self.karty_w_reku = karty_w_reku
	CardNumb = 51
	def dobierz_karte(self,talia):
		nr=random.randrange(0,gracz.CardNumb)
		self.karty_w_reku.append(talia[nr])
		talia.remove(talia[nr])
		gracz.CardNumb-=1
	def sprawdz_wynik(self,kolejka):
		suma=0
		if kolejka == 0:
			return 0
		for i in range(0,kolejka):
			suma+=karta.figury[str(self.karty_w_reku[i].figura)]
		return suma

#gra
talia=karta.NowaTalia()
gracz1=gracz('PC 1','',[],)
gracz2=gracz(raw_input('Podaj imie '),raw_input('Podaj Nazwisko '),[])
os.system('clear')
print "Gracz 1:", gracz1.Imie, gracz1.Nazwisko, gracz1.karty_w_reku
print "Gracz 2:", gracz2.Imie, gracz2.Nazwisko, gracz2.karty_w_reku
raw_input("Wcisnij przycisk by kontynuowac")

kolejka,s1,s2,tOff,check,points1,points2=1,0,0,0,'aniDaniP',0,0
while (tOff!=1):
    if s1 == 0:
        gracz1.dobierz_karte(talia)
        points1=gracz1.sprawdz_wynik(kolejka)
        if points1 >=21:
	        s1=1
    if s2 == 0:
        gracz2.dobierz_karte(talia)
        points2=gracz2.sprawdz_wynik(kolejka)
        os.system('clear')
        print "Wylosowano karte: ", gracz2.karty_w_reku[kolejka-1].kolor, gracz2.karty_w_reku[kolejka-1].figura
        while check!='d' and check!='p':
			print "[d]obierz nastepna karte \n[p]as \n[s]prawdz wynik"
			check=raw_input("wcisnij odpowiedni przycik, by wybrac co zrobic ")
			if check == 'd':
			    s2=0
			elif check == 's':
				os.system('clear')
				print points2
			elif check == 'p':
				s2 = 1
			else:
				print "niepoprawny klawisz, sprobuj jeszcze raz..."
				os.system('clear')
    kolejka+=1
    check="aniDaniP"
    os.system('clear')
    if s1 == 1 and s2 == 1:
		tOff=1
os.system('clear')
#kto blizej 21 ten wygrywa, remis gdy tyle samo punktow lub oboje przekrocza 21pkt
print "gracz1: ",points1,"\ngracz2: ",points2
if (21-points1 < 21-points2 or points2>21)and points1<=21:
	print 'PRZEGRANA!!! Nastepnym razem sie uda!'
elif 21-points1 == 21-points2 or (points1>21 and points2>21):
	print 'REMIS!!!'
elif (21-points1 > 21-points2 or points1>21) and points2<=21:
	print 'ZWYCIESTWO!!! Gratulacje!'
