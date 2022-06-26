#falta incorporar numeros con coma
#incorporar funcion borrar numero

from tkinter import *

raiz=Tk()
raiz.title("Calculadora")
raiz.iconbitmap("C:/Users/victo/Documents/Curso Python/Calculadora/calculadora_icon.ico")
raiz.geometry("250x320")
raiz.config(background='gray50')

miFrame=Frame(raiz)
miFrame.config(background='gray50')
miFrame.pack()

operacion=""
resultado=0
reset_pantalla=False


#----------------PANTALLA------------------

numeroPantalla=StringVar()


pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=0,column=1,padx=0,pady=10,columnspan=4,rowspan=2)      #columnspan: q ocupe 4 lugares
pantalla.config(background="black",fg="#03f943",justify="right",font=("ISOCP_IV25",16))
#pantalla.place(width=6,height=2)

numeroPantalla.set("0")   #prende y aparece el 0 en pantalla


#---------------Pulsaciones teclado------------

def numeroPulsado(num):
    global operacion
    global reset_pantalla
    if numeroPantalla.get()=="0":      #se prende y aparece 0, luego cuando se usa se va
        numeroPantalla.set("")
    if reset_pantalla!=False:
        numeroPantalla.set(num)
        reset_pantalla=False
    else: 
        numeroPantalla.set(numeroPantalla.get()+num)    # agrega(set) lo q haya (get) CONCATECANDO con el 4

#-----------------Borrar pantalla (CS)-----------------

def limpiar_pantalla():
    global reset_pantalla
    global operacion
    global resultado
    global cont_divi,cont_multi,cont_resta
    numeroPantalla.set("0")
    reset_pantalla=True
    cont_resta=0
    cont_multi=0
    cont_divi=0
    resultado=0
    operacion=""

#----------------funcion borrar numero----------


#----------------funcion borrar elemento (CE)----------


#----------------funcion suma------------------

def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado+=int(num)   #texto a entero
    operacion="suma"
    reset_pantalla=True
    numeroPantalla.set(resultado)

#---------------funcion resta-------------------
num1=0
cont_resta=0

def resta(num):
    global operacion
    global resultado
    global num1
    global cont_resta
    global reset_pantalla
    if cont_resta==0:
        num1=int(num)
        resultado=num1
    elif cont_resta==1:
        resultado=num1-int(num)
    else: 
        resultado=int(resultado)-int(num)
    numeroPantalla.set(resultado)
    resultado=numeroPantalla.get()

    cont_resta+=1
    operacion="resta"
    reset_pantalla=True

#-----------------funcion multiplicacion----------
cont_multi=0

def multiplica(num):
    global operacion
    global reset_pantalla
    global resultado
    global cont_multi
    global num1
    if cont_multi==0:
        num1=int(num)
        resultado=num1
    elif cont_multi==1:
        resultado=num1*int(num)
    else:
        resultado=int(resultado)*int(num)
    numeroPantalla.set(resultado)
    resultado=numeroPantalla.get()
    cont_multi+=1
    operacion="multiplicacion"
    reset_pantalla=True

#------------------funcion division-----------------
cont_divi=0

def dividir(num):
    global operacion
    global resultado
    global reset_pantalla
    global cont_divi
    global num1
    if cont_divi==0:
        num1=int(num)
        resultado=num1
    elif cont_divi==1:
        resultado=num1/int(num)
    else: 
        resultado=int(resultado)/int(num)
    numeroPantalla.set(resultado)
    resultado=numeroPantalla.get()
    cont_divi+=1
    operacion="division"
    reset_pantalla=True

        



#-----------------funcion el_resultado----------

def el_resultado():
    global resultado
    global operacion
    global cont_resta
    global cont_multi
    global cont_divi
    if operacion=="suma":
        numeroPantalla.set(resultado+int(numeroPantalla.get()))
        resultado=0
    elif operacion=="resta":
        numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))
        cont_resta=0
        resultado=0
    elif operacion=="multiplicacion":
        numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))
        cont_multi=0
        resultado=0
    elif operacion=="division":
        numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))
        cont_divi=0
        resultado=0
    else: print("Operacion no incorporada")


    

#---------------FILA 1--------------------

botonCS=Button(miFrame,text="CS",width=6,height=2,command=lambda:limpiar_pantalla())   #CS: clear screen
botonCS.grid(row=2,column=1)
botonCS.config(background='gray20',activebackground='gray30',fg='white',cursor='hand2')
botonCE=Button(miFrame,text="CE",width=6,height=2)    #CE: clear element
botonCE.grid(row=2,column=2)
botonCE.config(background='gray20',activebackground='gray30',fg='white',cursor='hand2')
botonBorrar=Button(miFrame,text="BORRAR",width=6,height=2) #borrar digito ---->ver!!
botonBorrar.grid(row=2,column=3,columnspan=2,sticky=S+N+E+W)
botonBorrar.config(background='gray20',activebackground='gray30',fg='white',cursor='hand2')


#-------------FILA 2---------------------


boton7=Button(miFrame,text="7",width=6,height=2,command=lambda:numeroPulsado("7"))
boton7.grid(row=3,column=1)
boton7.config(background='gray10',activebackground='gray20',fg='white',cursor='hand2')
boton8=Button(miFrame,text="8",width=6,height=2,command=lambda:numeroPulsado("8"))
boton8.grid(row=3,column=2)
boton8.config(background='gray10',activebackground='gray20',fg='white',cursor='hand2')
boton9=Button(miFrame,text="9",width=6,height=2,command=lambda:numeroPulsado("9"))
boton9.grid(row=3,column=3)
boton9.config(background='gray10',activebackground='gray20',fg='white',cursor='hand2')
botonDiv=Button(miFrame,text="/",width=6,height=2,command=lambda:dividir(numeroPantalla.get()))
botonDiv.grid(row=3,column=4)
botonDiv.config(background='gray20',activebackground='gray30',fg='white',cursor='hand2')

#------------FILA 3------------------------

boton4=Button(miFrame,text="4",width=6,height=2,command=lambda:numeroPulsado("4"))     #Lambda
boton4.grid(row=4,column=1)
boton4.config(background='gray10',activebackground='gray20',fg='white',cursor='hand2')
boton5=Button(miFrame,text="5",width=6,height=2,command=lambda:numeroPulsado("5"))
boton5.grid(row=4,column=2)
boton5.config(background='gray10',activebackground='gray20',fg='white',cursor='hand2')
boton6=Button(miFrame,text="6",width=6,height=2,command=lambda:numeroPulsado("6"))
boton6.grid(row=4,column=3)
boton6.config(background='gray10',activebackground='gray20',fg='white',cursor='hand2')
botonMult=Button(miFrame,text="x",width=6,height=2,command=lambda:multiplica(numeroPantalla.get()))
botonMult.grid(row=4,column=4)
botonMult.config(background='gray20',activebackground='gray30',fg='white',cursor='hand2')

#-------------FILA 4--------------------

boton1=Button(miFrame,text="1",width=6,height=2,command=lambda:numeroPulsado("1"))
boton1.grid(row=5,column=1)
boton1.config(background='gray10',activebackground='gray20',fg='white',cursor='hand2')
boton2=Button(miFrame,text="2",width=6,height=2,command=lambda:numeroPulsado("2"))
boton2.grid(row=5,column=2)
boton2.config(background='gray10',activebackground='gray20',fg='white',cursor='hand2')
boton3=Button(miFrame,text="3",width=6,height=2,command=lambda:numeroPulsado("3"))
boton3.grid(row=5,column=3)
boton3.config(background='gray10',activebackground='gray20',fg='white',cursor='hand2')
botonRest=Button(miFrame,text="-",width=6,height=2,command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=5,column=4)
botonRest.config(background='gray20',activebackground='gray30',fg='white',cursor='hand2')


#-------------FILA 5-------------------

boton0=Button(miFrame,text="0",width=6,height=2,command=lambda:numeroPulsado("0"))
boton0.grid(row=6,column=1)
boton0.config(background='gray10',activebackground='gray20',fg='white',cursor='hand2')
botonComa=Button(miFrame,text=",",width=6,height=2,command=lambda:numeroPulsado(","))
botonComa.grid(row=6,column=2)
botonComa.config(background='gray10',activebackground='gray20',fg='white',cursor='hand2')
botonSum=Button(miFrame,text="+",width=6,height=2,command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=6,column=3,columnspan=2,sticky=S+N+E+W)
botonSum.config(background='gray20',activebackground='gray30',fg='white',cursor='hand2')


#-----------------FILA 6----------------------

botonIgual=Button(miFrame,text="=",width=6,height=2,command=lambda:el_resultado())
botonIgual.grid(row=7,column=1,columnspan=4,sticky=S+N+E+W)
botonIgual.config(background='gray20',activebackground='gray30',fg='white',cursor='hand2')









raiz.mainloop()