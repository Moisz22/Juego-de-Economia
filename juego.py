import random
import tkinter.messagebox
from tkinter import *

minas = []                  ###lista donde se guardaran las minas generadas aleatoriamente


for i in range(5):         ### creando las minas aleatoriamente
    minatemp = random.randint(1, 16)
    if not minatemp in minas:
    	minas.append(minatemp)
        

rango = len(minas)          ###especifica la cantidad de minas existentes

def resp1():
	if var.get() == 1:
		messagebox.showinfo("Juego de economia buscaminas", "Respuesta correcta")
	else:
		messagebox.showinfo("Juego de economia buscaminas", "Respuesta incorrecta, la respuesta correcta es la primera")

def resp2():
	if var.get() == 2:
		messagebox.showinfo("Juego de economia buscaminas", "Respuesta correcta")
	else:
		messagebox.showinfo("Juego de economia buscaminas", "Respuesta incorrecta, la respuesta correcta es la segunda")


preguntazar = random.randint(1, 5)
def pregunta(preguntazar):
	if preguntazar == 1:
		Label(root, text="Cuales son los tipos de Organismos Internacionales").pack()
		Radiobutton(root,text="Gubernamentales y no Gubernamentales", variable=var, value=1,justify="left", cursor="hand1", command=resp1).pack()
		Radiobutton(root,text="Exteriores e Interiores", variable=var, value=2,justify="left", cursor="hand1", command=resp1).pack()
		Radiobutton(root,text="Micro y Macro", variable=var, value=3,justify="left", cursor="hand1", command=resp1).pack()
		Radiobutton(root,text="De competencia general y especial", variable=var, value=4,justify="left", cursor="hand1", command=resp1).pack()
	elif preguntazar == 2:
		Label(root, text="Los organismos internacionales son grupos organizados cuya area de accion se extiende mas alla \nde las fronteras de un Estado o nacion").pack()
		Radiobutton(root,text="Verdadero", variable=var, value=1,justify="left", cursor="hand1", command=resp1).pack()
		Radiobutton(root,text="Falso", variable=var, value=2,justify="left", cursor="hand1", command=resp1).pack()
	elif preguntazar == 3:
		Label(root, text="Los Organismos Internacionales Gubernamentales son aquellos conformados por diferentes Estados \nque se comprometen a cooperar").pack()
		Radiobutton(root,text="Verdadero", variable=var, value=1,justify="left", cursor="hand1", command=resp1).pack()
		Radiobutton(root,text="Falso", variable=var, value=2,justify="left", cursor="hand1", command=resp1).pack()
	elif preguntazar == 4:
		Label(root, text="Los Organismos Internacionales No Gubernamentales son aquellos que estan conformados por actores\nprivados o agrupaciones sociales").pack()
		Radiobutton(root,text="Verdadero", variable=var, value=1,justify="left", cursor="hand1", command=resp1).pack()
		Radiobutton(root,text="Falso", variable=var, value=2,justify="left", cursor="hand1", command=resp1).pack()
	elif preguntazar == 5:
		Label(root, text="La Organizacion Mundial del Comercio ha sido sustituido por el GATT").pack()
		Radiobutton(root,text="Verdadero", variable=var, value=1,justify="left", cursor="hand1", command=resp2).pack()
		Radiobutton(root,text="Falso", variable=var, value=2,justify="left", cursor="hand1", command=resp2).pack()


def descubrirminas():       ###si presiona sobre una mina se descubren las demas
	for i in range(rango):
		if minas[i] == 1:
			boton1.config(state="disabled", bg="red")
		else:
			boton1.config(state="disabled")

		if minas[i] == 2:
			boton2.config(state="disabled", bg="red")
		else:
			boton2.config(state="disabled")

		if minas[i] == 3:
			boton3.config(state="disabled", bg="red")
		else:
			boton3.config(state="disabled")

		if minas[i] == 4:
			boton4.config(state="disabled", bg="red")

		else:
			boton4.config(state="disabled")

		if minas[i] == 5:
			boton5.config(state="disabled", bg="red")
		else:
			boton5.config(state="disabled")

		if minas[i] == 6:
			boton6.config(state="disabled", bg="red")
		else:
			boton6.config(state="disabled")

		if minas[i] == 7:
			boton7.config(state="disabled", bg="red")
		else:
			boton7.config(state="disabled")

		if minas[i] == 8:
			boton8.config(state="disabled", bg="red")
		else:
			boton8.config(state="disabled")

		if minas[i] == 9:
			boton9.config(state="disabled", bg="red")
		else:
			boton9.config(state="disabled")

		if minas[i] == 10:
			boton10.config(state="disabled", bg="red")
		else:
			boton10.config(state="disabled")

		if minas[i] == 11:
			boton11.config(state="disabled", bg="red")
		else:
			boton11.config(state="disabled")

		if minas[i] == 12:
			boton12.config(state="disabled", bg="red")
		else:
			boton12.config(state="disabled")

		if minas[i] == 13:
			boton13.config(state="disabled", bg="red")
		else:
			boton13.config(state="disabled")

		if minas[i] == 14:
			boton14.config(state="disabled", bg="red")
		else:
			boton14.config(state="disabled")

		if minas[i] == 15:
			boton15.config(state="disabled", bg="red")
		else:
			boton15.config(state="disabled")

		if minas[i] == 16:
			boton16.config(state="disabled", bg="red")
		else:
			boton16.config(state="disabled")


def salir():
	root.destroy()

def posicion_minas():
	messagebox.showinfo("Minas existentes", minas)

def reglas():
	messagebox.showinfo("Reglas del juego", "Solo tiene una oportunidad, las minas se generar automaticamente y maximo existen 5 minas en cada partida")

def presionar1():        
	for i in range(rango):
		if minas[i] == 1:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton1.config(state="disabled", bg="blue")


def presionar2():         
	for i in range(rango):
		if minas[i] == 2:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton2.config(state="disabled", bg="blue")


def presionar3():         
	for i in range(rango):
		if minas[i] == 3:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton3.config(state="disabled", bg="blue")


def presionar4():         
	for i in range(rango):
		if minas[i] == 4:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton4.config(state="disabled", bg="blue")


def presionar5():         
	for i in range(rango):
		if minas[i] == 5:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton5.config(state="disabled", bg="blue")


def presionar6():         
	for i in range(rango):
		if minas[i] == 6:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton6.config(state="disabled", bg="blue")


def presionar7():         
	for i in range(rango):
		if minas[i] == 7:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton7.config(state="disabled", bg="blue")


def presionar8():         
	for i in range(rango):
		if minas[i] == 8:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton8.config(state="disabled", bg="blue")


def presionar9():         
	for i in range(rango):
		if minas[i] == 9:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton9.config(state="disabled", bg="blue")


def presionar10():         
	for i in range(rango):
		if minas[i] == 10:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton10.config(state="disabled", bg="blue")


def presionar11():         
	for i in range(rango):
		if minas[i] == 11:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton11.config(state="disabled", bg="blue")

def presionar12():         
	for i in range(rango):
		if minas[i] == 12:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton12.config(state="disabled", bg="blue")


def presionar13():         
	for i in range(rango):
		if minas[i] == 13:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton13.config(state="disabled", bg="blue")


def presionar14():         
	for i in range(rango):
		if minas[i] == 14:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton14.config(state="disabled", bg="blue")


def presionar15():         
	for i in range(rango):
		if minas[i] == 15:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton15.config(state="disabled", bg="blue")


def presionar16():         
	for i in range(rango):
		if minas[i] == 16:
			messagebox.showinfo("Juego de economia buscaminas", "Perdiste")
			descubrirminas()
			pregunta(preguntazar)
	boton16.config(state="disabled", bg="blue")


root = Tk()
var = IntVar()
root.iconbitmap("cisc.ico")
root.title("Juego de economia buscaminas")
root.config(cursor="pirate")
root.geometry('600x500')
root.resizable(0,0)


frame = Frame(root)
frame.pack()
frame.config(bd=50)

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Salir", command=salir)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Mostrar minas", command=posicion_minas)
helpmenu.add_separator()
helpmenu.add_command(label="Reglas del juego", command=reglas)
menubar.add_cascade(label="Juego",menu=filemenu)
menubar.add_cascade(label="Ayuda",menu=helpmenu)



boton1 = Button(frame, bd=10, command=presionar1,text="1",font=("arial",15), bg="light gray")
boton1.grid(row=0, column=0)
boton2 = Button(frame, bd=10, command=presionar2,text="2",font=("arial",15), bg="light gray")
boton2.grid(row=1, column=0)
boton3 = Button(frame, bd=10, command=presionar3,text="3",font=("arial",15), bg="light gray")
boton3.grid(row=2, column=0)
boton4 = Button(frame, bd=10, command=presionar4,text="4",font=("arial",15), bg="light gray")
boton4.grid(row=3, column=0)
boton5 = Button(frame, bd=10, command=presionar5,text="5",font=("arial",15), bg="light gray")
boton5.grid(row=0, column=1)
boton6 = Button(frame, bd=10, command=presionar6,text="6",font=("arial",15), bg="light gray")
boton6.grid(row=1, column=1)
boton7 = Button(frame, bd=10, command=presionar7,text="7",font=("arial",15), bg="light gray")
boton7.grid(row=2, column=1)
boton8 = Button(frame, bd=10, command=presionar8,text="8",font=("arial",15), bg="light gray")
boton8.grid(row=3, column=1)
boton9 = Button(frame, bd=10, command=presionar9,text="9",font=("arial",15), bg="light gray")
boton9.grid(row=0, column=2)
boton10 = Button(frame, bd=10, command=presionar10,text="10",font=("arial",15), bg="light gray")
boton10.grid(row=1, column=2)
boton11= Button(frame, bd=10, command=presionar11,text="11",font=("arial",15), bg="light gray")
boton11.grid(row=2, column=2)
boton12= Button(frame, bd=10, command=presionar12,text="12",font=("arial",15), bg="light gray")
boton12.grid(row=3, column=2)
boton13 = Button(frame, bd=10, command=presionar13,text="13",font=("arial",15), bg="light gray")
boton13.grid(row=0, column=3)
boton14 = Button(frame, bd=10, command=presionar14,text="14",font=("arial",15), bg="light gray")
boton14.grid(row=1, column=3)
boton15 = Button(frame, bd=10, command=presionar15,text="15",font=("arial",15), bg="light gray")
boton15.grid(row=2, column=3)
boton16 = Button(frame, bd=10, command=presionar16,text="16",font=("arial",15), bg="light gray")
boton16.grid(row=3, column=3)

root.mainloop()




print("hola mundo");
