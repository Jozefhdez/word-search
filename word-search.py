import tkinter as tk
import random

# Define las letras que se usarán en la sopa de letras
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Tamaño de la sopa de letras (filas x columnas)
filas = 10
columnas = 10

# Lista de palabras predefinidas que son menores a 10 letras por palabra
palabras_predefinidas = ["CASA", "PERRO", "GATO", "LAPIZ", "MESA", "SILLA", "AUTO", "LIBRO", "TREN"]

# Lista para almacenar las palabras encontradas
palabras_encontradas = []

# Función para generar una sopa de letras aleatoria
def generar_sopa_de_letras():
    global palabras_encontradas
    palabras_encontradas = []  # Reinicia la lista de palabras encontradas
    sopa_de_letras.delete("1.0", tk.END)  # Borra el contenido existente en el widget
    sopa = [[" " for _ in range(columnas)] for _ in range(filas)]  #Crea una matriz bidimensional vacía para representar la sopa de letras.

    for palabra in palabras_predefinidas: #Comienza a recorrer las palabras predefinidas.
        direccion = random.choice(["horizontal", "vertical"]) #Decide aleatoriamente si la palabra se colocará en dirección horizontal o vertical.
        if direccion == "horizontal":
            while True:
                fila = random.randint(0, filas - 1) #En el caso horizontal se revisa en que fila quedara la palabra
                columna = random.randint(0, columnas - len(palabra)) #Se revisa que la palabra quepa en la columna
                if all(sopa[fila][columna + i] == " " for i in range(len(palabra))): #En caso de todos los espacios estar vacios pone cada letra de la palabra seleccionada
                    break
        else: #Caso que toque vertical
            while True:
                fila = random.randint(0, filas - len(palabra)) #Revisa que la palabra quepa en la fila
                columna = random.randint(0, columnas - 1)#Selecciona una columna para poner la palabra
                if all(sopa[fila + i][columna] == " " for i in range(len(palabra))): #En caso de todos los espacios estar vacios pone cada letra de la palabra seleccionada
                    break

        for i, letra in enumerate(palabra): #Llena la sopa de letras con la palabra seleccionada en la dirección apropiada.
            if direccion == "horizontal":
                sopa[fila][columna + i] = letra
            else:
                sopa[fila + i][columna] = letra

    # Rellenar espacios vacíos con letras aleatorias
    for i in range(filas):
        for j in range(columnas):
            if sopa[i][j] == " ": #Revisa que esten vacias y en caso de estarlo pone una letra aleatorias de 'letras'
                sopa[i][j] = random.choice(letras)

    # Actualizar la sopa de letras con letras aleatorias
    #Esta parte del codigo tiene el objetivo de limpiar y actualizar visualmente la sopa de letras en la interfaz gráfica.
    sopa_de_letras.delete("1.0", tk.END)
    for fila in sopa:
        fila_str = " ".join(fila)
        sopa_de_letras.insert(tk.END, fila_str + "\n")

    # Ocultar el botón "Reiniciar Juego"
    reiniciar_boton.pack_forget()

# Función para verificar si se encontraron todas las palabras
def verificar_ganador():
    if set(palabras_encontradas) == set(palabras_predefinidas): #Cuando se encuentran todas las palabras y las palabras encontradas es igual a las palabras predefinidas se muestra el mensaje de que gano el juego.
        mensaje_label.config(text="¡GANASTE! Encontraste todas las palabras.")
        # Mostrar el botón "Reiniciar Juego"
        reiniciar_boton.pack()

# Función para verificar y marcar palabras
def verificar_palabra():
    palabra_ingresada = palabra_entry.get().upper() #Obtiene la palabra ingresada y le da formato en mayusculas y lo almacena en la variable palabra_ingresada
    if palabra_ingresada in palabras_predefinidas and palabra_ingresada not in palabras_encontradas: #Checa si esta en palabras predefinidas y no la hemos encontrado aun
        palabras_encontradas.append(palabra_ingresada) #En caso de ser correcta la agrega a palabras encontradas
        palabra_entry.delete(0, tk.END) #Se borra del widget para que el usuario pueda ingresar otra
        palabra_label.config(text="Palabra encontrada: " + palabra_ingresada) #Muestra mensaje que ha sido encontrada
        verificar_ganador() #Luego de encontrar una palabra, se llama a la función verificar_ganador para comprobar si todas las palabras predefinidas han sido encontradas y, en ese caso, mostrar un mensaje de victoria.
    else:
        mensaje_label.config(text="Palabra no encontrada: " + palabra_ingresada) #Muestra mensaje en caso de ser incorrecta


# Función para reiniciar el juego
def reiniciar_juego():
    mensaje_label.config(text="") #borra cualquier mensaje de la interfaz grafica
    reiniciar_boton.pack_forget() #oculta el boton de reiniciar juego
    generar_sopa_de_letras() #llamamos a la funcion para reiniciar el juego

# Configura la ventana principal
ventana = tk.Tk()
ventana.title("Sopa de Letras") #damos titulo a la ventana

# Botón para generar la sopa de letras
generar_boton = tk.Button(ventana, text="Generar Sopa de Letras", command=generar_sopa_de_letras) #Especificamos donde esta el boton, que texto tiene y que funcion hara cuando se le de click
generar_boton.pack() #utilizamos el metodo pack esto hace que el botón sea visible en la interfaz gráfica y se ajuste automáticamente al tamaño necesario

# Widget de texto para mostrar la sopa de letras
sopa_de_letras = tk.Text(ventana, width=20, height=10) #ajustamos el tamaño de la ventana
sopa_de_letras.pack()

# Etiqueta y entrada para ingresar palabras encontradas
palabra_label = tk.Label(ventana, text="Ingresa una palabra encontrada:") 
palabra_label.pack() #Esto hace que la etiqueta sea visible en la interfaz gráfica.
palabra_entry = tk.Entry(ventana) #Guardamos en esta variable lo que ingrese el usuario
palabra_entry.pack() #Colocamos el campo para que el usuario ingrese la plabra en la ventana principal

# Botón para verificar palabra ingresada
verificar_boton = tk.Button(ventana, text="Verificar Palabra", command=verificar_palabra) #creamos boton que llama a la funcion para verificar la palabra
verificar_boton.pack() #utilizamos el metodo pack esto hace que el botón sea visible en la interfaz gráfica y se ajuste automáticamente al tamaño necesario

# Etiqueta para mostrar el mensaje de ganador
mensaje_label = tk.Label(ventana, text="") #Creamos etiqueta de texto
mensaje_label.pack()

# Botón para reiniciar el juego
reiniciar_boton = tk.Button(ventana, text="Reiniciar Juego", command=reiniciar_juego) #llama a la funcion para reiniciar el juego

# Genera una sopa de letras inicial
generar_sopa_de_letras()

ventana.mainloop() #Esto interfaz gráfica se ejecute

