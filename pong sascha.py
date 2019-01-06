########Importations
from tkinter import *
from pygame import mixer
mixer.init(44100, -16, 15, 2048)
########Variables
fenetre = Tk()
fenetre.title("Pong Game by Sascha Sallès")
hauteur = 500
largeur = 725
can = Canvas(fenetre,height = hauteur, width = largeur)
fond1 = can.create_rectangle(0,0,largeur,hauteur, fill = "black")
xballe = 314
yballe = 228
dx_pas = 9
dy_pas = 9
xrectangle = 0
yrectangle = 210
yrectangle2 = 210
rect_pas = 	60
xrectangle2 = largeur - 17
balle = can.create_oval(xballe, yballe, xballe + 40, yballe + 40, fill="black", outline = "white")
raquet = can.create_rectangle(xrectangle,yrectangle,xrectangle + 20,yrectangle + 100, fill="red")
raquet2 = can.create_rectangle(xrectangle2,yrectangle2,xrectangle2 + 20,yrectangle2 + 100, fill="blue")
textegauche = can.create_text(largeur/4,20, text="Rouge : ", font=("Helvetica", 21), fill='red')
textedroite = can.create_text((largeur * 3/4),20, text="Bleu : ", font=("Helvetica", 21), fill='blue')
compteurdroite = 0
compteurgauche = 0
affichage = can.create_text(largeur/2, hauteur/2, text = "P   NG", font =("Avenir Next", 60),fill = "white")
instructions = can.create_text(largeur/2, hauteur/3, text = "Pour le joueur Rouge : appuyez sur TAB pour monter et sur Shift Gauche pour descendre.", font = ("Avenir Next", 14), fill = "red")
instructions2 = can.create_text(largeur/2, hauteur/4, text = "Pour le joueur Bleu : appuyez sur ↑ pour monter et ↓ pour descendre. Vous pouvez aussi utiliser la souris", font = ("Avenir Next", 14), fill = "light blue")
instructions3 = can.create_text(largeur/2, hauteur/1.4, text = "Une interface FootBall est disponible ainsi que BasketBall", font = ("Avenir Next", 14), fill = "light blue")
son1 = mixer.Sound("1.wav")
son2 = mixer.Sound("2.wav")

########Fonctions
	
def raquettesouris(event):
	global yrectangle
	global haut
	haut = (event.y)
	yrectangle = haut
	if yrectangle < 3:
		yrectangle = 3
	if yrectangle + 100 > 500:
		yrectangle = 400
	can.coords(raquet2,largeur - 20, yrectangle, largeur, yrectangle + 100)

	
def anim():
	can.delete(affichage)
	can.delete(instructions)
	can.delete(instructions2)
	can.delete(instructions3)
	global xballe
	global dx_pas
	global yballe
	global dy_pas
	global compteurdroite
	global compteurgauche
	xballe += dx_pas
	yballe += dy_pas
	if yballe < 0 or yballe > 460 :
		dy_pas = -dy_pas
	if xballe > 685 or xballe < 0:
		dx_pas = -dx_pas			
	if xballe <= 0:
		compteurgauche += 1
		can.itemconfig(textedroite,text="Bleu : " + str(compteurgauche))
	if xballe + 40 > largeur:
		compteurdroite += 1
		can.itemconfig(textegauche,text="Rouge : " + str(compteurdroite))
		if compteurdroite == 10:
				can.delete(textedroite)
				dx_pas = 0
				dy_pas = 0
				can.create_text(largeur/4,40, text = "Joueur Rouge à gagné !", font =("Avenir Next", 20),fill = 'yellow')
	can.coords(balle,xballe, yballe, xballe + 40, yballe + 40)
	lignemilieu = can.create_line(largeur/2,0,largeur/2,hauteur, fill =  "white",dash = (2, 2))
	if compteurdroite == 10:
		can.delete(textedroite)
		dx_pas = 0
		dy_pas = 0
		xballe = 10
		yballe = 10
		can.create_text(largeur/4,40, text = "Joueur Rouge à gagné !", font =("Avenir Next", 20),fill = 'yellow')
		
				
	elif compteurgauche == 10:	
		can.delete(textegauche)
		dx_pas = 0
		dy_pas = 0
		xballe = 10
		yballe = 10
		can.create_text((largeur * 3/4),40, text="Joueur Bleu à gagné !", font=("Helvetica", 21), fill='yellow')
	fenetre.after(20, anim)
	
def bas(event):
	global yrectangle
	yrectangle += rect_pas
	if yrectangle < 2:
		yrectangle = 2
	elif yrectangle > (hauteur-2) - rect_pas:
		yrectangle -= rect_pas
	else:
		can.coords(raquet, xrectangle,yrectangle,xrectangle + 20,yrectangle + 100)
		
def haut(event):
	global yrectangle
	yrectangle -= rect_pas
	if yrectangle < 2:
		yrectangle = 2
	else:
		can.coords(raquet, xrectangle,yrectangle,xrectangle + 20,yrectangle + 100)
				
def bas2(event):
	global yrectangle2
	yrectangle2 += rect_pas
	if yrectangle2 < 2:
		yrectangle2 = 2
	elif yrectangle2 > (hauteur-2) - rect_pas:
		yrectangle2 -= rect_pas
	else:
		can.coords(raquet2, xrectangle2,yrectangle2,xrectangle2 + 20,yrectangle2 + 100)	
			
def haut2(event):
	global yrectangle2
	yrectangle2 -= rect_pas
	if yrectangle2 < 2:
		yrectangle2 = 2
	else:
		can.coords(raquet2, xrectangle2,yrectangle2,xrectangle2 + 20,yrectangle2 + 100)	
		
		
def collision():
	global dx_pas
	if (largeur - 20 <= xballe + 40 <= largeur) and (yrectangle <= yballe <= yrectangle + 120):
		dx_pas = -dx_pas
		son1.play()
		
	if (3 <= xballe <= 23) and (yrectangle2 <= yballe <= yrectangle2 + 120):
		dx_pas = -dx_pas
		son2.play()
	fenetre.after(20, collision)

def terrainfoot():
	largeurG = 0
	largeurD = 705
	while largeurG < 20:
		can.create_line(largeurG,120,largeurG,380, fill = "white", dash = (2,2))
		largeurG += 2
	while largeurD < 725:
		can.create_line(largeurD,120,largeurD,380, fill = "white", dash = (2,2))
		largeurD += 2
	can.itemconfig(balle, dash = (2,2), outline = "blue")
	can.create_oval(300,190,300+125,190+125, fill = "#bae397",outline = "white")
	can.create_oval(360,250,366,256, fill = "white",outline = "black")
	can.create_line(0,75,150,75, fill = "white")
	can.create_line(0,425,150,425, fill = "white")
	can.create_line(150,75,150,425, fill = "white")
	can.create_line(575,75,575,425, fill = "white")
	can.create_line(575,75,725,75, fill = "white")
	can.create_line(575,425,725,425, fill = "white")
	can.itemconfigure(fond1, fill="#bae397")

def terrainbasket():
	can.itemconfig(balle, dash = (2,2), fill = "orange")
	can.create_oval(300,190,300+125,190+125, fill = "#E2B996",outline = "white")
	can.create_oval(360,250,366,256, fill = "white",outline = "black")
	can.create_line(0,75,150,75, fill = "white")
	can.create_line(0,425,150,425, fill = "white")
	can.create_line(150,75,150,425, fill = "white")
	can.create_line(575,75,575,425, fill = "white")
	can.create_line(575,75,725,75, fill = "white")
	can.create_line(575,425,725,425, fill = "white")
	can.itemconfigure(fond1, fill="#E2B996")

def difficile():
	global dx_pas
	global dy_pas
	dx_pas = 14
	dy_pas = 14
	
def facile():
	global dx_pas
	global dy_pas
	dx_pas = 4
	dy_pas = 4
	
def Intermediaire():
	global dx_pas
	global dy_pas
	dx_pas = 9
	dy_pas = 9
		
def stopGame():
	global dx_pas
	global dy_pas
	dx_pas = 0
	dy_pas = 0

		

########Main


fenetre.bind("<Down>", bas2) 
fenetre.bind("<Up>", haut2)
fenetre.bind("<Shift_L>", bas) 
fenetre.bind("<Tab>", haut) 
can.bind("<Motion>", raquettesouris)
boutonDifficile = Button(text = "Mode Expert",state=ACTIVE,command = difficile)
boutonIntermediaire = Button(text = "Mode Intermédiaire",state=ACTIVE, command = Intermediaire)
boutonFacile= Button(text = "Mode Facile",state=ACTIVE, command = facile)
boutonFoot = Button(text = "Interface FootBall",state=ACTIVE, command = terrainfoot)
boutonBasket = Button(text = "Interface Basket",state=ACTIVE, command = terrainbasket)
Lancer = Button(text = "Lancer le Jeu", command = anim)
boutonStop = Button(text = "Stopper le Jeu", command = stopGame)
boutonBasket.grid(row=1,column=6)
boutonStop.grid(row=1,column=1)
Lancer.grid(row=1,column=0)
boutonDifficile.grid(row=1,column=4)
boutonIntermediaire.grid(row=1,column=3)
boutonFacile.grid(row=1,column=2)
boutonFoot.grid(row=1,column=5)
collision()
can.grid(row=0,column=0,columnspan=8)


fenetre.mainloop()