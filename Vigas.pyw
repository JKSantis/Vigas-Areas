from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import os
import math

# VENTANA PRINCIPAL
raiz = Tk()
raiz.title("JKSANTIS VIGAS")
raiz.iconbitmap('C:/Users/jksan/Desktop/PRIMERAGUI/naruto1.ico')
raiz.geometry("600x400") # tamaño de la ventana principal raiz
raiz.resizable(width=0, height=0)


#PANEL PARA PESTAÑAS
nb = ttk.Notebook(raiz)
nb.pack(fill='both',expand = 'yes')

#CREAMOS PESTAÑÁS
p1 = ttk.Frame(nb)
p2 = ttk.Frame(nb)
p3 = ttk.Frame(nb)

#AGREGAMOS PESTAÑAS CREADAS
nb.add(p1,text='Datos Sección')
nb.add(p2,text='Momento Curvatura')
nb.add(p3,text='Diagra de interacción')

#CREAR GRAFICA

fig = Figure(figsize=(2, 2), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2*np.sin(2*np.pi*t)) #añadir subplot

canvas = FigureCanvasTkAgg(fig, master = p2) #CREAR AREA DE DIBUJO DE TKINTER
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#AÑADIR BARRA DE HERRAMIENTAS

toolbar = NavigationToolbar2Tk(canvas, p2) # barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


miframe = Frame(raiz)
miframe.pack()

miMenu = Menu(raiz)

raiz.config(menu = miMenu)

def info():
    messagebox.showinfo("V.S.C","Mi primera GUI\nJohann Gonzalez\nVersion 1.00\nDate: 2020-04-16\n informe de errores: \n jksantis@hotmail.com")

def avisoSalir():
    respuesta = messagebox.askquestion("Cuidado","Estás seguro de que quieres salir?")
    if respuesta =="yes":
        raiz.destroy()

miFile = Menu(miMenu, tearoff = 0)
miFile.add_command(label="New File")
miFile.add_command(label="New Window")
miFile.add_separator()
miFile.add_command(label="Open File..")
miFile.add_command(label="Close Editor")
miFile.add_command(label="Exit", command = avisoSalir)

miHelp = Menu(miMenu, tearoff = 0)
miHelp.add_command(label="Welcome")
miHelp.add_command(label="About", command= info)

miMenu.add_cascade(label="File",menu=miFile)

miMenu.add_cascade(label="Help",menu=miHelp)
#----CREACION DE VISORES-------------------------------------

varVisorinput = StringVar() # Despues probar con DoubleVar(0)
varVisorinput.set(20)
varVisorb = StringVar() # Despues probar con DoubleVar(0)
varVisorb.set(20)
varVisord = StringVar() # Despues probar con DoubleVar(0)
varVisord.set(50)
varVisormin = StringVar() # Despues probar con DoubleVar(0)
varVisormax = StringVar() # Despues probar con DoubleVar(0)

varVisoroutput = StringVar() # Despues probar con DoubleVar(0)

#------------------------------------CREACION DE INPUT Y OUTPUT

Input= Entry(p1, textvariable=varVisorinput)
Input.place(x=200,y=100)
Input.config(bg = "white", fg = "black", justify="center")

Inputb= Entry(p1, textvariable=varVisorb)
Inputb.place(x=200,y=50)
Inputb.config(bg = "white", fg = "black", justify="center")

Inputd= Entry(p1, textvariable=varVisord)
Inputd.place(x=200,y=25)
Inputd.config(bg = "white", fg = "black", justify="center")

Inputmin= Entry(p1, textvariable=varVisormin, state='readonly')
Inputmin.place(x=200,y=270)
Inputmin.config(bg = "white", fg = "black", justify="center")

Inputmax= Entry(p1, textvariable=varVisormax, state='readonly')
Inputmax.place(x=200,y=290)
Inputmax.config(bg = "white", fg = "black", justify="center")

Output= Entry(p1, textvariable=varVisoroutput, state='readonly') 
Output.place(x=200,y=250)
Output.config(bg = "white", fg = "black", justify="center")

#----------------------------------ETIQUETAS
etiquetainput = Label(p1, text = "d [cm]")
etiquetainput.place(x=100,y=25)
etiquetainput = Label(p1, text = "b [cm]")
etiquetainput.place(x=100,y=50)

etiquetainput = Label(p1, text = "Mu [Tonf m]")
etiquetainput.place(x=100,y=100)

etiquetaoutput = Label(p1, text = "As req [cm²] ")
etiquetaoutput.place(x=100,y=250)

etiquetaoutput = Label(p1, text = "As min [cm²] ")
etiquetaoutput.place(x=100,y=270)

etiquetaoutput = Label(p1, text = "As max [cm²] ")
etiquetaoutput.place(x=100,y=290)

#--------------------------- FUNCIONES

def escribir():

    try:
        Mu = float(varVisorinput.get())

        b = float(varVisorb.get())

        d = float(varVisord.get())

        fc = f_c[tipo_hormigon.current()]

        fy = 4200.0

        b1 = beta1[tipo_hormigon.current()]

        As = 0.85*(fc/fy)*b*d*(1-math.sqrt(1-(2.622*Mu*100000.0)/(b*d*d*fc)))

        Asmin = max(0.8*(math.sqrt(fc)/fy)*d*b,(14/fy)*d*b)

        Asmax = 0.85*b1*fc*b*d*0.003/(fy*(0.004+0.003))

        varVisoroutput.set(round(As,3))

        varVisormin.set(round(Asmin,3))
        varVisormax.set(round(Asmax,3))

        answer.config(text = '')

    except ValueError:

        answer.config(text = 'Debes ingresar valores numéricos',fg='red')

answer = Label(p1,text = '')
answer.place(x=400,y=300)
#------------boton ejecutar---------

calcular_btn = PhotoImage(file='C:/Users/jksan/Desktop/PRIMERAGUI/imagen2.png')
img_label = Label(image=calcular_btn)
botonejecutar = Button(p1, image=calcular_btn,width = 50,command = escribir, borderwidth = 0)

botonejecutar.place(x=450,y=250)

#-------LISTA DEPLEGABLE----------

tipo_hormigon=ttk.Combobox(p1,width = 17,state='readonly')
tipo_hormigon.place(x= 450,y=20)
#lista de opciones
opciones = ['G20','G25','G30','G35','G40','G45','G50']
f_c = [200,250,300,350,400,450,500]
beta1 = [0.85,0.85,0.8357,0.8,0.7643,0.7286,0.6929]
#insertar valores
tipo_hormigon['values']=opciones
tipo_hormigon.set('G20')


raiz.mainloop()