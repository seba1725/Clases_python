import tkinter

def aceptar():
    a = float(n1.get())
    b = float(n2.get())
    c = float(n3.get())
    if a >= b and a >= c:
        etiqueta = tkinter.Label(ventana, text = "Es un triangulo")
    elif b >= a and b >= c:
        etiqueta = tkinter.Label(ventana, text = "Es un triangulo")
    else: 
        etiqueta = tkinter.Label(ventana, text = "Es un triangulo")

ventana = tkinter.Tk()
ventana.title("Bienvenido al programa identificador de triangulos")
ventana.resizable(0, 0)

label0 = tkinter.Label(ventana, text="Ingrese medidas del Triangulo")
label0.pack()
etiqueta = tkinter.Label(ventana)
etiqueta.pack()

label = tkinter.Label(ventana, text="Ingrese lado izquierdo")
label.grid(row = 0, column = 0)
n1 = tkinter.Entry(ventana)
n1.grid(row = 0, column = 1)

label2 = tkinter.Label(ventana, text="Ingrese lado inferior")
label2.grid(row = 1, column = 0)
n2 = tkinter.Entry(ventana)
n2.grid(row = 1, column = 1)

label3 = tkinter.Label(ventana, text="Ingrese lado derecho")
label3.grid(row = 2, column = 0)
n3 = tkinter.Entry(ventana)
n3.grid(row = 2, column = 1)

labelf = tkinter.Label(ventana)
labelf.pack()
boton = tkinter.Button(ventana, text="Resultado", command=aceptar)
boton.pack()

frame = tkinter.Frame(ventana)
frame.pack()
frame.config(width=480, height=180)

ventana.mainloop()