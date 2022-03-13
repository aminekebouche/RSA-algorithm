from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random

import datetime 




# Test de la primalite de p et q 
def liste_non_multiple(n, l):
    return [i for i in l if i%n!=0]

def eratosthene(nb):
    entiers=[]
    premiers= []
    [entiers.append(i) for i in range(2,nb+1)]
    while len(entiers)!=0:
        # sauvegarder le premier element de la liste entiers.
        premiers.append(entiers[0])
        # déterminer tous les entiers qui ne sont multiples de celui qui sauvegardé.
        entiers= liste_non_multiple(entiers[0], entiers)
    return premiers

def pgcd(a, b):
    while b!=0:
        a,b= b, a%b
    return a 

def choix(fi):
    x=[]
    for i in range(2, fi+1):
        
        if pgcd(fi,i)== 1:
            x.append(i)
    e= random.choice(x)
    return e

# Algorithme d'euclide étendu
def euclide_etendu(a,b):
    x = 1 ; xx = 0
    y = 0 ; yy = 1
    while b != 0 :
        q = a // b
        a , b = b , a % b
        xx , x = x - q*xx , xx
        yy , y = y - q*yy , yy
    if a < 0:
        a,x,y = -a,-x,-y
    return (a,x,y)

# Creation de la clée privée 
def inverse(a,n):
    c,u,v = euclide_etendu(a,n)    # pgcd et coeff. de Bézout
    if c != 1 :            # Si pgcd différent de 1 renvoie 0
        return 0
    else :
        return u % n # ou bien u car u < n

def puissance(x, k, n): #version iterarive
    p= 1
    while k>0:
        if k%2 !=0:
            p = (p*x) %n
        x= x*x %n
        k= k//2
    return p

def chiff(M,n,e):
    code=num1(M)
    chif = ''
    for j in decoup(code, n):
        if j !=0:
            chif = chif + str(puissance(j,e,n))
    return chif 

def dechiff(chif,n,d):
    Decouper= decoup(chif,n)
    Dchif = ''
    for j in decoup(chif, n):
        if j !=0:
            Dchif = Dchif + str(puissance(j, d, n))
    return Dchif


def num1(M):
    M = M.lower()
    code = ''
    s= 'abcdefghijklmnopqrstuvwxyz'
    for c in M:
        trouv= False
        i=0
        while i<=25 and not(trouv):
            if s[i]==c:
                trouv=True
                if i < 9:
                    code = code + '0' + str(i + 1)
                else: 
                    code = code + str(i + 1)
            i = i + 1
    return code

def decoup(code,n):
    L = []
    scode=''
    for i in range(1,len(code)+1):
        if len(scode) < len(str(n))-1:
            scode=code[-i]+scode
            
        else :
            L=[int(scode)]+L
            scode= code[-i]
    L=[int(scode)]+L
    return L      


def action():
    P1=int(p1.get())
    Q1=int(q1.get())
    if not (P1 in eratosthene(P1)) or not (Q1 in eratosthene(Q1)) or (P1<30 and Q1 <30):
        n1.delete(0,END)
        n1.insert(0,'ERREUR')
    else:
         N= P1 * Q1
         fi= (P1-1)*(Q1-1)
         e= choix(fi)
         d=inverse(e,fi)
         n1.delete(0,END)
         n1.insert(0,N)
         e1.delete(0,END)
         e1.insert(0,e)
         d1.delete(0,END)
         d1.insert(0,d)

def effacer ():
    p1.delete(0,END)
    q1.delete(0,END)
    n1.delete(0,END)
    e1.delete(0,END)
    d1.delete(0,END)
    m1.delete(0,END)
    c1.delete(0,END)

def chiffrer():
    M1=m1.get()
    e= int(e1.get())
    n= int(n1.get())
    c1.delete(0,END)
    c1.insert(0,chiff(M1,n,e))

def dechiffrer():
    D1=c1.get()
    d= int(d1.get())
    n= int(n1.get())
    m1.delete(0,END)
    m1.insert(0,dechiff(D1,n,d))


    



    

        
    
   





fen = tk.Tk()
fen.geometry("1200x600")
fen.title("RSA")
#fen.iconbitmap('cad.png')
fen.config(background='#808080')
#image = PhotoImage(file='user.gif').zoom(15).subsample(32)
canvas=Canvas(fen,width=300, height=300,bg='#808080',bd=0,highlightthickness=0)
#canvas.create_image(300/2,300/2,image=image)
canvas.pack(expand=YES)

p=Label(fen, text="P > 30 :")
p.place(x=40 , y= 40)
p1=Entry(fen)
p1.place(x=90, y= 40)

q=Label(fen, text="Q > 30 :")
q.place(x=400 , y= 40)
q1=Entry(fen)
q1.place(x=450 , y= 40)

n=Label(fen, text="n : ")
n.place(x=875 , y= 40)
n1=Entry(fen)
n1.place(x=900 , y= 40)

e=Label(fen, text="e : ")
e.place(x=250 , y= 100)
e1=Entry(fen)
e1.place(x=275 , y= 100)

d=Label(fen, text="d : ")
d.place(x=690 , y= 100)
d1=Entry(fen)
d1.place(x=715 , y= 100)

m=Label(fen, text="M : ")
m.place(x=50 , y= 360)
m1=Entry(fen)
m1.place(x=100 , y= 300 , height=150 ,width=300)

c=Label(fen, text="C : ")
c.place(x=750 , y= 360)
c1=Entry(fen)
c1.place(x=780 , y= 300 ,height=150 ,width=300)



cal= Button(fen , text="Calculer",command= action)
cal.place(x=300, y=200)

eff= Button(fen , text="Effacer",command= effacer)
eff.place(x=800, y=200)

ch= Button(fen , text="Chiffrer",command= chiffrer)
ch.place(x=300, y=500)

dch= Button(fen , text="Dechiffrer",command= dechiffrer)
dch.place(x=800, y=500)



def ExitApplication():
    # MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    # if MsgBox == 'yes':
    #    fen.destroy()
    # else:
    # 
    messagebox.showinfo('Aide',
    '1- L''utilisateur choisi deux nombres premiers P et Q assez grands (>30).  \n2- Pour générer les clées, le produit n = pq est calculé grace au bouton CALCULLER. \n3- La clé publique est choisit aléatoirement parmis plusieurs possibilités de "e"  \n4- La clée privée D est calculée  (linverse du "e" choisit)  \n5- Pour chiffrer un message, dans lexemple on saisit que des lettre sans le caractère "espaces" dans le champ M et le message chiffrer saffiche dans C. \n6- Pour déchiffrer, on saisie le code dans C apres avoir rempli N , D et on déchiffre avec le boutton dechiffrer ')
    # tk.messagebox.showinfo('Return','You will now return to the application screen')
        
button1 = Button (fen, text='Aide',command=ExitApplication,bg='white',fg='black')
# button1.place( x=800, y=1000)
canvas.create_window(150, 310, window=button1)


fen.mainloop()