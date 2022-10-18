import tkinter
from typing import Text 

alfabeto =  ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
listaImpares = ["a","e","i","m","p","t","x","b","f","j","n","q","u","y","c","g","k","ñ","r","v","z","d","h","l","o","s","w"]
listaPares = ["n","r","w","b","g","l","p","u","z","e","j","ñ","s","x","c","h","m","q","v","a","f","k","o","t","y","d","i"]

ventana = tkinter.Tk()
ventana.title("Encriptación")
ventana.geometry("800x300")

etiqueta = tkinter.Label(ventana, text="Aplicación para encriptar :D",font="Times 15")
entry = tkinter.Entry(ventana, font= "Helvetica 20", width=30)
resultado = tkinter.Text(ventana, font="Helvetica 20", height=2, width=30)

def obtenerEncriptado():
    resultado.delete(1.0, 'end')
    nuevaPalabra = ""
    contador=1
    cajatexto = entry.get()
    cajatexto_limpia = cajatexto.replace(" ","")
    cajatexto_limpia =  cajatexto_limpia.lower()
    for i in cajatexto_limpia:
        
        if contador%2 == 0 :
            x = alfabeto.index(i)
            y= listaPares[x]
            nuevaPalabra= nuevaPalabra + y
            contador=contador+1
        else:
            u = alfabeto.index(i)
            w= listaImpares[u]
            nuevaPalabra= nuevaPalabra + w
            contador=contador+1
    
    resultado.insert(1.0,nuevaPalabra)

button1 = tkinter.Button(ventana, text = "Encriptar", command=obtenerEncriptado, highlightbackground='#3E4149')

etiqueta.pack()
entry.pack()
button1.pack()
resultado.pack()

ventana.mainloop()