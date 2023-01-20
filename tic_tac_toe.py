import os
import sys
import PIL

from tkinter import *

from PIL import Image, ImageTk

import tkinter.messagebox



# creo una instancia de TK para que nos deje utilizar los mensajes
root = Tk()


root.title('Tic tac toe')

#Esto es para q el user pueda o no resize la pantalla
root.resizable(width=FALSE,height = FALSE)


#Esta es la direccion ROOT del projecto
path = os.path.dirname(os.path.realpath(sys.argv[0]))
#----------------------------------------------------
#----------------- VARIABLES ------------------------
#----------------------------------------------------

# Para cada click que se haga en la pantalla
click = True

#Contador para cada boton--- SI llega a 9 significa que todos los espacios estan llenos
count = 0

#---------- BUTTONS
# COmo son 9 botones creo 9 variables de texto que estaran asociadas a los botones
# Estas variables de texto me serviran a la hora de decidir cunado se gana o no

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()


#---------- FOTOS
# Subimos las imagenes que descargamos para X y O con PhotoImage


photoX = Image.open(path + "/x.png")
photoX = photoX.resize((100,100), Image.ANTIALIAS)
xPhoto = Image.PhotoImage(photoX)

photoO = ImageTk.open(path + "/o.png")
photO = photoO.resize((130,130), Image.ANTIALIAS)
oPhoto = ImageTk.PhotoImage(photoO)
#defaultPhoto = PhotoImage(file='default.jpg')


#----------------------------------------------------
#----------------- FUNTIONS ------------------------
#----------------------------------------------------


#----------------------------------
#----------- BOARD ----------------

# Contiene el tablero de juego
def board():
    """
    La funcion LAMBDA me va a permitir enviar la info del buton a la funcion PRESS
    Primero le envio un valor
    Segundo su ubicacion ROW y COLUMN
    Esto es lo que lleva la funcion adentro
    """
#-----BTN1-----
    button1 = Button(root,height=13,width=26,bd = .5,
                     bg = '#e6ffe6',
                     textvariable = btn1,command =lambda:press(1,0,0))

    #Muestro el boton en la pantalla
    button1.grid(row=0,column=0)
#-----BTN2-----
    button2 = Button(root,height=13,width=26,bd = .5,
                     bg = '#e6ffe6',
                     textvariable = btn2,command = lambda:press(2,0,1))
    button2.grid(row=0,column=1)
#-----BTN3-----
    button3 = Button(root,height=13,width=26,bd = .5,
                     bg = '#e6ffe6',
                     textvariable = btn3,command = lambda:press(3,0,2))
    button3.grid(row=0,column=2)
#-----BTN4-----
    button4 = Button(root,height=13,width=26,bd = .5,
                     bg = '#ccffcc',
                     textvariable = btn4,command = lambda:press(4,1,0))
    button4.grid(row=1,column=0)
#-----BTN5-----
    button5 = Button(root,height=13,width=26,bd = .5,
                     bg = '#ccffcc',
                     textvariable = btn5,command = lambda:press(5,1,1))
    button5.grid(row=1,column=1)
#-----BTN6-----
    button6 = Button(root,height=13,width=26,bd = .5,
                     bg = '#ccffcc',
                     textvariable = btn6,command = lambda:press(6,1,2))
    button6.grid(row=1,column=2)
#-----BTN7-----
    button7 = Button(root,height=13,width=26,bd = .5,
                     bg = '#b3ffb3',
                     textvariable = btn7,command = lambda:press(7,2,0))
    button7.grid(row=2,column=0)
#-----BTN8-----
    button8 = Button(root,height=13,width=26,bd = .5,
                     bg = '#b3ffb3',
                     textvariable = btn8,command = lambda:press(8,2,1))
    button8.grid(row=2,column=1)
#-----BTN9-----
    button9 = Button(root,height=13,width=26,bd = .5,
                     bg = '#b3ffb3',
                     textvariable = btn9,command = lambda:press(9,2,2))
    button9.grid(row=2,column=2)


#----------------------------------
#----------- PRESS ----------------

# Esta funcion recibe lo que envia la funcion LAMBDA
# REcive el numero y despues la ubicacion de la FILA y COLUMNA
def press(num,r,c):
    #Lo primero que hacemos es traer las variables globales de COUNT y CLICK
    global count, click

    # Click esta inicializado como TRUE, entonces hacemos un IF
    if click == True:
        labelPhoto = Label(root,image=xPhoto)
        # La foto la ubicamos en las coordenadas que importamos de la funcion LAMBDA del boton que se presiona
        labelPhoto.grid(row = r, column = c)
        #------------ SET TEXT VARIABLE
        # Aqui reviso cada vez que se ingrese
        # Seteo la variable
        if num == 1:
            btn1.set("X")
        elif num == 2:
            btn2.set("X")
        elif num == 3:
            btn3.set("X")
        elif num == 4:
            btn4.set("X")
        elif num == 5:
            btn5.set("X")
        elif num == 6:
            btn6.set("X")
        elif num == 7:
            btn7.set("X")
        elif num == 8:
            btn8.set("X")
        elif num == 9:
            btn9.set("X")
        #Pasamos el click a False para que la siguiente movida aparesca la "O"
        click = False
        # Voy contando cada movida para saber si se acabaron los movimiento y si alguien gana
        count +=1

        # Ahora revisamos si alguien ganÃ³
        checkWin()

    else:
        labelPhoto = Label(root,image=oPhoto)
        # La foto la ubicamos en las coordenadas que importamos de la funcion LAMBDA del boton que se presiona
        labelPhoto.grid(row = r, column = c)
        if num == 1:
            btn1.set("O")
        elif num == 2:
            btn2.set("O")
        elif num == 3:
            btn3.set("O")
        elif num == 4:
            btn4.set("O")
        elif num == 5:
            btn5.set("O")
        elif num == 6:
            btn6.set("O")
        elif num == 7:
            btn7.set("O")
        elif num == 8:
            btn8.set("O")
        elif num == 9:
            btn9.set("O")
        #Pasamos el click a True para que la siguiente movida aparesca la "O"
        click = True
        # Voy contando cada movida para saber si se acabaron los movimiento y si alguien gana
        count +=1

        # Ahora revisamos si alguien ganÃ³
        checkWin()



#----------------------------------
#----------- CHECK-WIN ----------------
def checkWin():
    #Para tener la info de eses variables
    global count, click

    if (btn1.get()=='X' and btn2.get()=='X' and btn3.get()=='X' or
        btn4.get()=='X' and btn5.get()=='X' and btn6.get()=='X' or
        btn7.get()=='X' and btn8.get()=='X' and btn9.get()=='X' or
        btn1.get()=='X' and btn4.get()=='X' and btn7.get()=='X' or
        btn2.get()=='X' and btn5.get()=='X' and btn8.get()=='X' or
        btn3.get()=='X' and btn6.get()=='X' and btn9.get()=='X' or
        btn1.get()=='X' and btn5.get()=='X' and btn9.get()=='X' or
        btn3.get()=='X' and btn5.get()=='X' and btn7.get()=='X'
        ):

        tkinter.messagebox.showinfo("Tic-Tac-Toe","PLayer X wins")
        #Para que cuando el juego se resetee el primer movimiento sea X
        click = True
        #Reseteamos el contador
        count = 0
        # Llamamos la funcion de CLEAR
        clear()
        #COmenzamos el juego de nuevo
        board()
    elif (btn1.get()=='O' and btn2.get()=='O' and btn3.get()=='O' or
        btn4.get()=='O' and btn5.get()=='O' and btn6.get()=='O' or
        btn7.get()=='O' and btn8.get()=='O' and btn9.get()=='O' or
        btn1.get()=='O' and btn4.get()=='O' and btn7.get()=='O' or
        btn2.get()=='O' and btn5.get()=='O' and btn8.get()=='O' or
        btn3.get()=='O' and btn6.get()=='O' and btn9.get()=='O' or
        btn1.get()=='O' and btn5.get()=='O' and btn9.get()=='O' or
        btn3.get()=='O' and btn5.get()=='O' and btn7.get()=='O'
        ):

        tkinter.messagebox.showinfo("Tic-Tac-Toe","PLayer O wins")

        #Reseteamos el contador
        count = 0
        # Llamamos la funcion de CLEAR
        clear()
        #COmenzamos el juego de nuevo
        board()
    elif (count == 9):
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Tie Game")
        #Para que cuando el juego se resetee el primer movimiento sea X
        click = True
        #Reseteamos el contador
        count = 0
        # Llamamos la funcion de CLEAR
        clear()
        #COmenzamos el juego de nuevo
        board()
#----------------------------------
#----------- CLEAR ----------------
def clear():
    # Seteo todas la variables a un empty string
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')

board()

# EL un handeler que mantiene la ventana abierta
# Revisa cada cosa que utilizamos
# Se asegura que a ventana esta ALIVE
root. mainloop()
