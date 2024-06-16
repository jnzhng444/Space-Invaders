import tkinter as tk
from tkinter import messagebox
import time
import random
from threading import Thread
import glob
import pygame

def labelDestroy(List): # Esta funcion borra lo que esta en el canvas de manera recursiva
    """*******************************************************
           Instituto Tecnológico de Costa Rica
               Ingenería en Computadores
   Lenguaje: Python 3.11
   Descripción: Función que destruye los elementos de una lista
   Autor: Arturo Acuña Duran
   Fecha última modificación: Abril 22 de 2023
   Entradas: Lista
   Restricciones: Tiene que ser una lista
   Salidas: Destruye las los elementos de la lista
   ******************************************************"""
    if List == []: #Condicion de finalizacion
        return []
    else:
        (List[0]).destroy() #Se destruye el primer elemmento
        return labelDestroy(List[1:]) #Se hace slicing de la lista

score=0
scorelist=[]
usernamelist=[]

Window=tk.Tk() #Se crea ventana de Tkinter
Window.minsize(1280,720) #Se establece el tamaño
Window.title("Space Wars") #Se establece un titulo para la ventana
Window.resizable(False,False) #Se establece para que la ventana no pueda agrandar ni disminuir
Window.iconbitmap("BackgroundMenu/Icono.ico")

#Funcion para cargar imagenes
def cargarimgs(input, listaResultado): #Funcion que carga las imagenes en una lista
    """*******************************************************
           Instituto Tecnológico de Costa Rica
               Ingenería en Computadores
   Lenguaje: Python 3.11
   Descripción: Función que carga los imagenes de una lista
   Autor: Arturo Acuña Duran
   Fecha última modificación: Abril 22 de 2023
   Entradas: Una lista de imàgenes
   Restricciones: Tienen que ser imàgenes
   Salidas: Carga las imàgenes
   ******************************************************"""
    if (input == []):
        return listaResultado
    else:
        listaResultado.append(tk.PhotoImage(file = input[0]))
        return cargarimgs(input[1:], listaResultado)

def cargarSprites(patron): #Funcion que encuentra las imagenes y se las da a cargarimgs
    """*******************************************************
           Instituto Tecnológico de Costa Rica
               Ingenería en Computadores
   Lenguaje: Python 3.11
   Descripción: Función que destruye los elementos de una lista
   Autor: Arturo Acuña Duran
   Fecha última modificación: Abril 22 de 2023
   Entradas: Imagenes
   Restricciones: []
   Salidas: Todas las imagenes con un patron
   ******************************************************"""
    x = glob.glob("Fondo/" + patron)
    x.sort()
    return cargarimgs(x, [])


def lenn(elementos):  # Funcion len
    # Si no es elementos, es una lista vacia, por lo tanto, retorna 0
    if not elementos:
        return 0
    # Hace un slicing y va contando los elementos
    else:
        return 1 + lenn(elementos[1:])

#Imagenes para botones
imglogin=tk.PhotoImage(file="BackgroundMenu/BOTONLOGIN.png")
imgabout=tk.PhotoImage(file="BackgroundMenu/BOTONABOUT.png")
imgexit=tk.PhotoImage(file="BackgroundMenu/BOTONEXIT.png")
imglidel=tk.PhotoImage(file="BackgroundMenu/BOTONLIDEL.png")
imgret=tk.PhotoImage(file="BackgroundMenu/BOTONRET.png")
imgeasy=tk.PhotoImage(file="BackgroundMenu/BOTONEASY.png")
imgmed=tk.PhotoImage(file="BackgroundMenu/BOTONMED.png")
imghard=tk.PhotoImage(file="BackgroundMenu/BOTONHARD.png")

pygame.init()
pygame.mixer.music.load("Sonidos/MenuOficial.mp3")
pygame.mixer.music.set_volume(0.04)
pygame.mixer.music.play(-1)

def Menuprincipal():
    """*******************************************************
           Instituto Tecnológico de Costa Rica
               Ingenería en Computadores
   Lenguaje: Python 3.11
   Descripción: Es la funcion principal, dentro de ella esta los secciones de login, leaderboard, about, los modos de
   juegos y exit.
   Autor: Jian Yong Zheng Wu
   Fecha última modificación: Abril 22 de 2023
   ******************************************************"""

#Para acceder al inicio
    global lenn

    temp=[]

    MenuCanvas=tk.Canvas(Window, width=1280,height=720) #Se crea el Canvas para colocar las cosas
    MenuCanvas.place(x=0,y=0)

    Fondo1 = tk.PhotoImage(file="BackgroundMenu/SPACEGRANDE_00.png")  # Establecer variable para imagen de fondo
    fnd=MenuCanvas.create_image(0, 0, anchor="nw", image=Fondo1)

    Titulo1=tk.PhotoImage(file="BackgroundMenu/SPACETITLE.png")
    ttl=MenuCanvas.create_image(640,100,image=Titulo1,anchor="center")

    def LoginMenu():
        """*******************************************************
                   Instituto Tecnológico de Costa Rica
                       Ingenería en Computadores
           Lenguaje: Python 3.11
           Descripción: Es el menu de login, dentro de esta se encuentra una seccion para ingresar el usuario y aqui
           mismo se selecciona el nivel de dificultad que se desee.
           Autor: Jian Yong Zheng Wu
           Fecha última modificación: Abril 22 de 2023
           ******************************************************"""
        global Fondo2, usernameval
        global Titulo2
        labelDestroy(temp)  #Destruye los elementos del menu principal

        LoginCanvas = tk.Canvas(Window, width=1280, height=720)
        LoginCanvas.place(x=0, y=0)

        Fondo2 = tk.PhotoImage(file="BackgroundMenu/SPACEGRANDE_00.png") #Fondo 2
        fnd2=LoginCanvas.create_image(0, 0, image=Fondo2, anchor="nw")

        Titulo2 = tk.PhotoImage(file="BackgroundMenu/LOGINTITTLE.png")
        ttl1 = LoginCanvas.create_image(650, 100, image=Titulo2, anchor="center")

        LabelUsername= tk.Label(Window, text="Player's nickname:", font=("Small Fonts", 14), fg="white",bg="black")  # Para escribir sobre el fondo de pantalla
        LabelUsername.place(x=510, y=200, anchor="center")
        temp.append(LabelUsername)


        usernameval = tk.StringVar()
        User = tk.Entry(Window,textvariable=usernameval,bg="gray",fg="white")  # Para escribir el nombre de usuario

        User.place(x=650, y=200, anchor="center")
        temp.append(User)

        def add_username():
            """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Es la funcion que guarda los nombres ingresados en el tk.Entry, los almacena en una lista
               llamada usernamelist.
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
            username = usernameval.get()  # obtener el valor actual de la variable de texto
            usernamelist.append(username)  # agregar el nombre de usuario a la lista
            usernameval.set('')  # borrar el contenido del widget de entrada para que el usuario pueda ingresar otro nombre si lo desea


        def easyvalidation(): #Funcion para ejecutar el comando de validacion primero y luego la ventana de easy
            if validation():
                add_username()
                easymodescreen()
        def midvalidation(): #Funcion para ejecutar el comando de validacion primero y luego la ventana de medium
            if validation():
                add_username()
                midmodescreen()
        def hardvalidation(): #Funcion para ejecutar el comando de validacion primero y luego la ventana de hard
            if validation():
                add_username()
                hardmodescreen()
        def validation(): #Validacion para escribir el nombre
            """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Es una funcion que revisa las condiciones antes de entrar al modo de juego
               Fecha última modificación: Abril 22 de 2023
               Entradas: Numeros y letras
               Restricciones: []
               Salidas: Verifica que si se cumplieron todos los requisitos
               ******************************************************"""
            name = usernameval.get().strip() #El strip() sirve para quitar los espacios en blanco
            msg = "Must enter a nickname."
            if lenn(name) == 0:
                msg = "Name can\'t be empty."
            else:
                try:
                    if lenn(name) < 2: #Restriccion, si es menor que 2
                        msg = "Name is too short."
                    elif name.isspace(): #El .isspace busca los espacios en blanco
                        msg = "Name can't be just spaces."
                    elif lenn(name) > 19:
                        msg = "Name is too long." #Restriccion, si es mayor que 19
                    else:
                        return True #Para poder ejecutar la siguiente ventana easymode
                except Exception as ep:
                    messagebox.showerror("Error", ep)

            tk.messagebox.showinfo("Hi!",msg)


        def easymodescreen():
            """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Dificultad facil
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""

            global FondoEasy,Nave,NPCNave,score,NPCNave2,NPCNave3,lifeLabel,Heart,life,ultimo_tiempo,npcnave,Laserimg,Rock,Laserimg2
            global laser_en_pantalla,Laserimg3,Laserimg4,laser_en_pantalla2,laser_en_pantalla3,tiempo_ultimo_laser
            global tiempo_ultimo_laser2,tiempo_ultimo_laser3,rocas
            #Para parar la musica en esta ventana

            labelDestroy(temp) #Destruye los elementos de la pantalla anterior

            EasyCanvas = tk.Canvas(Window, width=1280, height=720)
            EasyCanvas.place(x=0, y=0)

            Background = cargarSprites("Moving_*")  # Se cargan los sprites del fondo
            BG = EasyCanvas.create_image(0,0)  # Se les da una posicion inicial

            def Movingbackground(i):  # Se crea una funcion recursiva que anima el fondo
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función que mueve el fondo
                Autor: Arturo Acuña Duran
                Entradas: imágenes
                Restricciones: []
                Salidas: los frames de las imagenes
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                if (i >= lenn(Background)):  # La funcion itera mientras el valor de i no sea mayor a la cantidad de fotos
                    i = 0  # Si i es mayor a la cantidad de fotos, se vuelve a iniciar el contador
                EasyCanvas.itemconfig(BG, image=Background[i],anchor="nw")  # Se cambia la imagen
                time.sleep(0.1)  # Se espera un momento
                Thread(target=Movingbackground, args=(i + 1,)).start()  # Se hace una llamada recurisva en un hilo aumentando i una unidad

            #Nave principal
            Nave=tk.PhotoImage(file="BackgroundMenu/NAVEPRINCIPAL.png")
            nve=EasyCanvas.create_image(50,360,image=Nave,anchor="center")

            #Imagen de la roca
            Rock=tk.PhotoImage(file="BackgroundMenu/Nebulosa.png")

            #Imagen el laser
            Laserimg=tk.PhotoImage(file="BackgroundMenu/LASER.png")
            Laserimg2 = tk.PhotoImage(file="BackgroundMenu/LASER2.png")
            Laserimg3 = tk.PhotoImage(file="BackgroundMenu/LASER3.png")
            Laserimg4 = tk.PhotoImage(file="BackgroundMenu/LASER4.png")


            #Coordenadas para que aparezcan las naves en lugares aleatorias
            #Naves enemigas
            npcX1 = random.randint(980, 1250)
            npcY1 = random.randint(50, 720)

            npcX2 = random.randint(980, 1250)
            npcY2 = random.randint(50, 720)

            npcX3 = random.randint(980, 1250)
            npcY3 = random.randint(50, 720)

            NPCNave = tk.PhotoImage(file="BackgroundMenu/NAVENPC.png")
            npcnve = EasyCanvas.create_image(npcX1, npcY1, image=NPCNave)

            NPCNave2 = tk.PhotoImage(file="BackgroundMenu/NAVENPC2.png")
            npcnve2 = EasyCanvas.create_image(npcX2, npcY2, image=NPCNave2)

            NPCNave3 = tk.PhotoImage(file="BackgroundMenu/NAVENPC3.png")
            npcnve3 = EasyCanvas.create_image(npcX3, npcY3, image=NPCNave3)

            #Seccion de retraso en el disparo de laser
            ultimo_tiempo = 0  # Definir afuera de todo como una variable que no sea local

            #Seccion para el nivel
            lvleasy=tk.Label(EasyCanvas,text="Easy",bg="black",fg="green",font=("Small Fonts",14))
            lvleasy.place(x=1030,y=40,anchor="center")

            #Seccion de score
            score=0
            scoreLabel=tk.Label(EasyCanvas,text="Score: "+str(score),bg="black",fg="white",font=("Small Fonts",14))
            scoreLabel.place(x=1200,y=40,anchor="center")

            # Imagen de life
            Heart = tk.PhotoImage(file="BackgroundMenu/heart pixel art 32x32.png")
            heart1 = EasyCanvas.create_image(1090, 40, image=Heart)

            #Seccion de life
            life=3
            lifeLabel=tk.Label(EasyCanvas,text=str(life),bg="black",fg="white",font=("Small Fonts",14))
            lifeLabel.place(x=1125,y=40,anchor="center")

            def edgereacheda():
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función que detecta el borde de la pantalla
                Autor: Kathie Quick
                Enlace: https://www.youtube.com/watch?v=g5qJEJjEOa4
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                Npcnaveboundary= EasyCanvas.bbox(npcnve)
                Npcnave2boundary = EasyCanvas.bbox(npcnve2)
                Npcnave3boundary = EasyCanvas.bbox(npcnve3)
                y=random.randint(50,700)
                if Npcnaveboundary[0] < 0:
                    EasyCanvas.coords(npcnve,1250,y)
                if Npcnave2boundary[0] < 0:
                    EasyCanvas.coords(npcnve2, 1250, y)
                if Npcnave3boundary[0] < 0:
                    EasyCanvas.coords(npcnve3,1250,y)

            #Game over
            def gameover():
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.8.10
                Descripción: Función que desplega la pantalla de GameOver
                Autor: Jian Yong Zheng Wu
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                global retry,Fondoover,menu,gmeover,final
                EasyCanvas.delete("all")
                PgCanvas = tk.Canvas(Window, width=1280, height=720, bg="black")
                PgCanvas.place(x=0, y=0)

                Fondoover = tk.PhotoImage(file="BackgroundMenu/SPACEGRANDE_00.png")
                Fondopg = PgCanvas.create_image(0, 0, image=Fondoover, anchor="nw")

                gmeover= tk.PhotoImage(file="BackgroundMenu/GAMEOVER-22-4-2023.png")
                gmover= PgCanvas.create_image(650,225,image=gmeover,anchor="center")

                finalscore = tk.Label(PgCanvas, text="Final score: " + str(score), bg="black", fg="white",font=("Small Fonts", 35))
                finalscore.place(x=500, y=300)

                scorelist.append(score)

                def Return():
                    global usernamelist
                    usernamelist.append(usernamelist[-1]) #Guardo el ultimo nombre ingresado
                    EasyCanvas.destroy()
                    PgCanvas.delete("all")
                    easymodescreen()


                retry = tk.PhotoImage(file="BackgroundMenu/BOTONRETRY.png")
                ReturnButtonP = tk.Button(Window, image=retry, bd=0, cursor="hand2", bg="black", relief="flat",activebackground="black", command=Return)
                ReturnButtonP.place(x=575, y=400, anchor="center")

                def home():
                    EasyCanvas.destroy()
                    PgCanvas.destroy()
                    Menuprincipal()

                menu = tk.PhotoImage(file="BackgroundMenu/BOTONHOME.png")
                MenuButtonP = tk.Button(Window, image=menu, bd=0, cursor="hand2", bg="black", relief="flat",activebackground="black", command=home)
                MenuButtonP.place(x=725, y=400, anchor="center")

            #Colision del nave y los naves enemigos
            #Las vidas de las naves
            #Gameover
            def colisionnave(npcnve):
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que detecta la colision de nave enemiga con la nave del jugador
               Autor: Jian Yong Zheng Wu y Kathie Quick
               Enlace: https://www.youtube.com/watch?v=_flFVAtmkoQ&list=PLFPWzE_xoI9kdu_Zhtc3zWkGjJPfkKiLS&index=4
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                global life, score
                NC = EasyCanvas.bbox(nve) #Variable para el bbox de la nave
                NCNPC = EasyCanvas.bbox(npcnve) #Variable para el bbox de la nave enemiga
                if (NC[0] < NCNPC[2] and NC[2] > NCNPC[0] and NC[1] < NCNPC[3] and NC[3] > NCNPC[1]): #Detecta colision en todos los lados, codigo de Kathie, pero modificado por mi persona
                    sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3") #Pygame para el sonido de disparar
                    sonidohit.set_volume(0.1)
                    sonidohit.play()
                    print("Hit")
                    EasyCanvas.coords(npcnve, 1280, random.randint(50,700))
                    life -= 1
                    lifeLabel.config(text=str(life)) #Configurar el label de la vida
                    print(life)
                    if life < 1:
                        gameover()
                    else:
                        lifeLabel.config(text=str(life))
                        EasyCanvas.after(10, colisionnave, npcnve)  # llamada recursiva con el mismo NPC

            def colisionlaser(laser):
                global life, score
                NC = EasyCanvas.bbox(nve)
                NCLASER = EasyCanvas.bbox(laser)
                # El None es una verificación adicional para asegurar que el láser todavía existe antes de continuar con la verificación de colisión.
                if NCLASER is not None and NC[0] < NCLASER[2] and NC[2] > NCLASER[0] and NC[1] < NCLASER[3] and NC[3] > NCLASER[1]:
                    sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                    sonidohit.set_volume(0.1)
                    sonidohit.play()
                    print("Hit")
                    EasyCanvas.delete(laser)
                    print("laser eliminado")
                    life -= 1
                    lifeLabel.config(text=str(life))
                    print(life)
                    if life < 1:
                        gameover()
                    else:
                        lifeLabel.config(text=str(life))
                        EasyCanvas.after(10, colisionlaser, laser)  # llamada recursiva con el mismo laser

            def colisionlasers(laser):
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que detecta la colision entre los lasers del jugador y del enemigo
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                global laser2, laser3, laser4
                NC = EasyCanvas.bbox(laser)
                if NC is not None: #Verificacion antes para que no sea vacia
                    NCLASER = EasyCanvas.bbox(laser2)
                    NCLASER2 = EasyCanvas.bbox(laser3)
                    NCLASER3 = EasyCanvas.bbox(laser4)
                    if NCLASER is not None and NC[0] < NCLASER[2] and NC[2] > NCLASER[0] and NC[1] < NCLASER[3] and NC[3] > NCLASER[1]:
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        print("Hit")
                        if laser is not None: #Verifica si la variable "laser" no es nula
                            EasyCanvas.delete(laser) #Se borra cuando detecta colision
                        if laser2 is not None: #Verifica si la variable "laser2" no es nula
                            EasyCanvas.delete(laser2) #Se borra cuando detecta colision
                        print("laser eliminado")
                    elif NCLASER2 is not None and NC[0] < NCLASER2[2] and NC[2] > NCLASER2[0] and NC[1] < NCLASER2[3] and NC[3] > NCLASER2[1]:
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        print("Hit")
                        if laser is not None:
                            EasyCanvas.delete(laser)
                        if laser3 is not None:
                            EasyCanvas.delete(laser3)
                        print("laser eliminado")
                    elif NCLASER3 is not None and NC[0] < NCLASER3[2] and NC[2] > NCLASER3[0] and NC[1] < NCLASER3[3] and NC[3] > NCLASER3[1]:
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        print("Hit")
                        if laser is not None:
                            EasyCanvas.delete(laser)
                        if laser4 is not None:
                            EasyCanvas.delete(laser4)
                        print("laser eliminado")
                    else:
                        EasyCanvas.after(10, colisionlasers, laser)  # llamada recursiva con el mismo laser

            #PRIMER NAVE NPC
            #Disparar lasers npc

            def lasernpc1():
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que hace que dispare el primer enemigo
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                global laser2, laser_image
                print("Creando nuevo láser...")
                lsrbbox = EasyCanvas.bbox(npcnve)
                centnpca = ((lsrbbox[0] + lsrbbox[2]) / 2) - 15 #Toma el centro de la nave en x y el -15 es para que dispare por la punta de la nave
                centnpcb = (lsrbbox[1] + lsrbbox[3]) / 2 #Toma el centro de la nave en y
                laser2 = EasyCanvas.create_image(centnpca, centnpcb, image=Laserimg2, tags="laser")  #Para etiquetar el objeto creado en el lienzo
                sonidoshoot = pygame.mixer.Sound("Sonidos/Disparo2.mp3")
                sonidoshoot.set_volume(0.1)
                sonidoshoot.play()
                mover_laser1(laser2)
                Window.after(5000, lasernpc1) #Actualiza cada 5 segundos

            def mover_laser1(laser2): #Funcion que mueve el laser
                if laser2 is not None: #Verifica que el laser no sea vacia
                    if EasyCanvas.bbox(laser2) is not None and EasyCanvas.bbox(laser2)[0] < 0:  #Si se sale de la pantalla se borra el laser
                        print("Laser2fuera")
                        EasyCanvas.delete(laser2)
                        laser2 = None #Para que no me tire error
                    else:
                        EasyCanvas.move(laser2, -5, 0)
                        if EasyCanvas.bbox(laser2) is not None: #Si no es vacio
                            colisionlaser(laser2) #Detectar colision

                    Window.after(10, mover_laser1, laser2) #Actualiza cada 10ms

            lasernpc1()

            # SEGUNDO NAVE NPC
            def lasernpc2():
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que hace que dispare el segundo enemigo
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                global laser3
                print("Creando nuevo láser2...")
                lsrbbox2 = EasyCanvas.bbox(npcnve2)
                centnpca2 = ((lsrbbox2[0] + lsrbbox2[2]) / 2) - 15
                centnpcb2 = (lsrbbox2[1] + lsrbbox2[3]) / 2
                laser3 = EasyCanvas.create_image(centnpca2, centnpcb2, image=Laserimg3, tags="laser3")
                mover_laser2(laser3)
                Window.after(5000, lasernpc2)

            def mover_laser2(laser3):
                if laser3 is not None:
                    if EasyCanvas.bbox(laser3) is not None and EasyCanvas.bbox(laser3)[0] < 0:  # Para que el laser llegue hasta el final del borde
                        print("Laser3fuera")
                        EasyCanvas.delete(laser3)
                        laser3 = None
                    else:
                        EasyCanvas.move(laser3, -5, 0)
                        if EasyCanvas.bbox(laser3) is not None:
                            colisionlaser(laser3)

                    Window.after(10, mover_laser2, laser3)

            lasernpc2()

            #Nave npc 3 disparar
            def lasernpc3():
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que hace que dispare el tercer enemigo
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                global laser4
                print("Creando nuevo láser3...")
                lsrbbox3 = EasyCanvas.bbox(npcnve3)
                centnpca3 = ((lsrbbox3[0] + lsrbbox3[2]) / 2) - 15
                centnpcb3 = (lsrbbox3[1] + lsrbbox3[3]) / 2
                laser4 = EasyCanvas.create_image(centnpca3, centnpcb3, image=Laserimg4, tags="laser4")
                mover_laser3(laser4)
                Window.after(5000, lasernpc3)

            def mover_laser3(laser4):
                if laser4 is not None:
                    if EasyCanvas.bbox(laser4) is not None and EasyCanvas.bbox(laser4)[0] < 0:  # Para que el laser llegue hasta el final del borde
                        print("Laser4fuera")
                        EasyCanvas.delete(laser4)
                        laser4 = None
                    else:
                        EasyCanvas.move(laser4, -5, 0)
                        if EasyCanvas.bbox(laser4) is not None:
                            colisionlaser(laser4)

                    Window.after(10, mover_laser3, laser4)

            lasernpc3()

            def NPCMove():
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que hace que se muevan los enemigos
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                edgereacheda()
                EasyCanvas.move(npcnve, -5, 0)
                EasyCanvas.move(npcnve2, -5, 0)
                EasyCanvas.move(npcnve3, -5, 0)
                colisionnave(npcnve)
                colisionnave(npcnve2)
                colisionnave(npcnve3)
                Window.after(25, NPCMove)

            NPCMove()

            #Colision del laser y la nave enemiga
            #PRUEBA 1
            laser=None
            def shoot(event):
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función para disparar laser
               Autor: Chat GPT y una parte por Jian Yong Zheng Wu
               Enlace: https://chat.openai.com/
               Fecha última modificación: Abril 22 de 2023
               Entradas: []
               Restricciones: []
               Salidas: Disparo del laser del nave de jugador
               ******************************************************"""
                global laser
                global ultimo_tiempo
                tiempoactual = time.time()  # Obtiene el tiempo actual
                # Comprueba si ha pasado al menos 0.5 segundos desde el último disparo
                if tiempoactual - ultimo_tiempo >= 0.5: #Tiempo mayor que 0.5 s
                    ultimo_tiempo = tiempoactual  # Actualiza el tiempo del último disparo
                    x, y = EasyCanvas.coords(nve) #Usamos .coords para saber donde esta la nave y establecer el x y el y
                    laser = EasyCanvas.create_image(x+15, y, image=Laserimg)  #Para que el laser salga en el centro de la nave
                    mover_laser(laser, 0) # Define una función recursiva para mover un láser hacia la derecha en cada actualización del juego
                    sonidodisparar = pygame.mixer.Sound("Sonidos/Disparoo.mp3")
                    sonidodisparar.set_volume(0.1)
                    sonidodisparar.play()

            def mover_laser(laser, count):
                """*******************************************************
                               Instituto Tecnológico de Costa Rica
                                   Ingenería en Computadores
                       Lenguaje: Python 3.11
                       Descripción: Función para disparar laser
                       Autor: Chat GPT y una parte por Jian Yong Zheng Wu
                       Enlace: https://chat.openai.com/
                       Fecha última modificación: Abril 22 de 2023
                       Entradas: []
                       Restricciones: []
                       Salidas: Mueve el laser
                       ******************************************************"""
                global score
                colisionlasers(laser) #Para detectar colision entre los lasers
                if count == 240:  # Para que el laser llegue hasta el final del borde
                    EasyCanvas.delete(laser)
                elif EasyCanvas.bbox(laser) is not None and EasyCanvas.bbox(laser)[2] > 1280:
                    print("LSR FUERA")
                    EasyCanvas.delete(laser)
                else:
                    EasyCanvas.move(laser, 9, 0)
                    if colision(laser, npcnve): #Colision de laser con algun nave enemigo
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        score = score + 50 #Suma 50 si pega a un enemigo
                        scoreLabel.config(text="Score: " + str(score)) #Cambia el puntaje
                        EasyCanvas.delete(laser) #Borra el laser
                        EasyCanvas.coords(npcnve, 1250, random.randint(50, 700)) #Genera el enemigo en una posicion distinta
                    elif colision(laser, npcnve2): #Colision de laser con algun nave enemigo
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        score = score + 50 #Suma 50 si pega a un enemigo
                        scoreLabel.config(text="Score: " + str(score)) #Cambia el puntaje
                        EasyCanvas.delete(laser) #Borra el laser
                        EasyCanvas.coords(npcnve2, 1250, random.randint(50, 700)) #Genera el enemigo en una posicion distinta
                    elif colision(laser, npcnve3): #Colision de laser con algun nave enemigo
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        score = score + 50 #Suma 50 si pega a un enemigo
                        scoreLabel.config(text="Score: " + str(score)) #Cambia el puntaje
                        EasyCanvas.delete(laser) #Borra el laser
                        EasyCanvas.coords(npcnve3, 1250, random.randint(50, 700)) #Genera el enemigo en una posicion distinta
                    else:
                        EasyCanvas.after(15, mover_laser, laser, count + 1) #Actualiza la funcion, el count es para ver cuantas veces ha llamado la funcion
                        #se verifica que el valor de count no sea mayor que 240, lo que garantiza que el láser no se mueva más allá del borde de la pantalla.

            def colision(laser, npcnve):  # Colision del laser y la nave npc
                npc_coords = EasyCanvas.coords(npcnve) #Para las coordenadas
                if not npc_coords or not EasyCanvas.find_withtag(laser):  # se utiliza para buscar el objeto "laser" en el
                    # lienzo y verificar si existe antes de intentar obtener sus coordenadas.
                    return False  # Tiraba error y no podia disparar de nuevo

                npc_x, npc_y = npc_coords  # Asignamos variables
                laser_x, laser_y = EasyCanvas.coords(laser)  # Asignamos variables

                xx = laser_x - npc_x  # Resta de pixeles
                yy = laser_y - npc_y # Resta de pixeles

                return xx < 30 and yy < 30 and xx > -30 and yy > -30
            # Si xx y yy son menores que 30 y mayores que -30, significa que el láser está a una distancia máxima de 20 píxeles
            # del NPC en ambas direcciones (horizontal y vertical), por lo que se considera que ha habido una colisión.

            #Seccion de movilidad
            def up(event): #Mover arriba
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función hacer mover la imagen a traves del teclado
               Autor: Codemy.com
               Enlace: https://www.youtube.com/watch?v=2rF8-jbTL-8
               Fecha última modificación: Abril 22 de 2023
               Entradas: W o w
               Restricciones: []
               Salidas: Mover 10 pixeles arriba
               ******************************************************"""
                x = 0
                y = -10
                if EasyCanvas.coords(nve)[1] + y > 0:  # check if the new y-coordinate is within the top boundary
                    EasyCanvas.move(nve, x, y) #En el canvas utilizando el .move, se mueve la nave en x y en y

            def down(event): #Mover abajo
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función hacer mover la imagen a traves del teclado
               Autor: Codemy.com
               Enlace: https://www.youtube.com/watch?v=2rF8-jbTL-8
               Fecha última modificación: Abril 22 de 2023
               Entradas: S o s
               Restricciones: []
               Salidas: Mover 10 pixeles abajo
               ******************************************************"""
                x = 0
                y = 10
                if EasyCanvas.coords(nve)[1] + y < EasyCanvas.winfo_height():  # check if the new y-coordinate is within the bottom boundary
                    EasyCanvas.move(nve, x, y)

            def left(event): #Mover izquierda
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función hacer mover la imagen a traves del teclado
               Autor: Codemy.com
               Enlace: https://www.youtube.com/watch?v=2rF8-jbTL-8
               Fecha última modificación: Abril 22 de 2023
               Entradas: A o a
               Restricciones: []
               Salidas: Mover 10 pixeles izquierda
               ******************************************************"""
                x = -10
                y = 0
                if EasyCanvas.coords(nve)[0] + x > 0:  # check if the new x-coordinate is within the left boundary
                    EasyCanvas.move(nve, x, y)

            def right(event): #Mover derecha
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función hacer mover la imagen a traves del teclado
               Autor: Codemy.com
               Enlace: https://www.youtube.com/watch?v=2rF8-jbTL-8
               Fecha última modificación: Abril 22 de 2023
               Entradas: D o d
               Restricciones: []
               Salidas: Mover 10 pixeles derecha
               ******************************************************"""
                x = 10
                y = 0
                if EasyCanvas.coords(nve)[0] + x < EasyCanvas.winfo_width():  # check if the new x-coordinate is within the right boundary
                    EasyCanvas.move(nve, x, y)

            #Seccion de asignacion de teclas para mover la nave y disparar
            Window.bind("<w>", up)
            Window.bind("<s>", down)
            Window.bind("<a>", left)
            Window.bind("<d>", right)
            Window.bind("<W>", up)
            Window.bind("<S>", down)
            Window.bind("<A>", left)
            Window.bind("<D>", right)
            Window.bind("<space>", shoot)

            Thread(target=Movingbackground, args=(lenn(Background) - 1,)).start()

        def midmodescreen():
            """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Dificultad medio
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
            global FondoEasy,Nave,NPCNave,score,NPCNave2,NPCNave3,lifeLabel,Heart,life,ultimo_tiempo,npcnave,Laserimg,Rock,Laserimg2
            global laser_en_pantalla,Laserimg3,Laserimg4,laser_en_pantalla2,laser_en_pantalla3,tiempo_ultimo_laser
            global tiempo_ultimo_laser2,tiempo_ultimo_laser3,rocas,roca_en_pantalla,roca,lista_laser
            #Para parar la musica en esta ventana

            labelDestroy(temp) #Destruye los elementos de la pantalla anterior

            EasyCanvas = tk.Canvas(Window, width=1280, height=720)
            EasyCanvas.place(x=0, y=0)

            Background = cargarSprites("Moving_*")  # Se cargan los sprites del fondo
            BG = EasyCanvas.create_image(0,0)  # Se les da una posicion inicial

            def Movingbackground(i):  # Se crea una funcion recursiva que anima el fondo
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función que mueve el fondo
                Autor: Arturo Acuña Duran
                Entradas: imágenes
                Restricciones: []
                Salidas: los frames de las imagenes
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                if (i >= lenn(Background)):  # La funcion itera mientras el valor de i no sea mayor a la cantidad de fotos
                    i = 0  # Si i es mayor a la cantidad de fotos, se vuelve a iniciar el contador
                EasyCanvas.itemconfig(BG, image=Background[i],anchor="nw")  # Se cambia la imagen
                time.sleep(0.1)  # Se espera un momento
                Thread(target=Movingbackground, args=(i + 1,)).start()  # Se hace una llamada recurisva en un hilo aumentando i una unidad

            #Nave principal
            Nave=tk.PhotoImage(file="BackgroundMenu/NAVEPRINCIPAL.png")
            nve=EasyCanvas.create_image(50,360,image=Nave,anchor="center")

            #Imagen el laser
            Laserimg=tk.PhotoImage(file="BackgroundMenu/LASER.png")
            Laserimg2 = tk.PhotoImage(file="BackgroundMenu/LASER2.png")
            Laserimg3 = tk.PhotoImage(file="BackgroundMenu/LASER3.png")
            Laserimg4 = tk.PhotoImage(file="BackgroundMenu/LASER4.png")

            #Coordenadas para que aparezcan las naves en lugares aleatorias
            #Naves enemigas
            npcX1 = random.randint(980, 1250)
            npcY1 = random.randint(50, 720)

            npcX2 = random.randint(980, 1250)
            npcY2 = random.randint(50, 720)

            npcX3 = random.randint(980, 1250)
            npcY3 = random.randint(50, 720)

            NPCNave = tk.PhotoImage(file="BackgroundMenu/NAVENPC.png")
            npcnve = EasyCanvas.create_image(npcX1, npcY1, image=NPCNave)

            NPCNave2 = tk.PhotoImage(file="BackgroundMenu/NAVENPC2.png")
            npcnve2 = EasyCanvas.create_image(npcX2, npcY2, image=NPCNave2)

            NPCNave3 = tk.PhotoImage(file="BackgroundMenu/NAVENPC3.png")
            npcnve3 = EasyCanvas.create_image(npcX3, npcY3, image=NPCNave3)

            #Imagen de la roca
            Rock= tk.PhotoImage(file="BackgroundMenu/ROCA 48.png")
            roca= EasyCanvas.create_image(1280,npcY1,image=Rock)

            #Seccion de retraso en el disparo de laser
            ultimo_tiempo = 0  # Definir afuera de todo como una variable que no sea local

            #Seccion para el nivel
            lvleasy=tk.Label(EasyCanvas,text="Medium",bg="black",fg="yellow",font=("Small Fonts",14))
            lvleasy.place(x=1030,y=40,anchor="center")

            #Seccion de score
            score=0
            scoreLabel=tk.Label(EasyCanvas,text="Score: "+str(score),bg="black",fg="white",font=("Small Fonts",14))
            scoreLabel.place(x=1200,y=40,anchor="center")

            # Imagen de life
            Heart = tk.PhotoImage(file="BackgroundMenu/heart pixel art 32x32.png")
            heart1 = EasyCanvas.create_image(1090, 40, image=Heart)

            #Seccion de life
            life=3
            lifeLabel=tk.Label(EasyCanvas,text=str(life),bg="black",fg="white",font=("Small Fonts",14))
            lifeLabel.place(x=1125,y=40,anchor="center")

            def edgereacheda():
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función que detecta el borde de la pantalla
                Autor: Kathie Quick
                Enlace: https://www.youtube.com/watch?v=g5qJEJjEOa4
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                Npcnaveboundary= EasyCanvas.bbox(npcnve)
                Npcnave2boundary = EasyCanvas.bbox(npcnve2)
                Npcnave3boundary = EasyCanvas.bbox(npcnve3)
                Npcnave4boundary = EasyCanvas.bbox(roca)

                y=random.randint(50,700)
                if Npcnaveboundary[0] < 0:
                    EasyCanvas.coords(npcnve,1250,y)
                if Npcnave2boundary[0] < 0:
                    EasyCanvas.coords(npcnve2, 1250, y)
                if Npcnave3boundary[0] < 0:
                    EasyCanvas.coords(npcnve3,1250,y)
                if Npcnave4boundary[0] < 0:
                    EasyCanvas.coords(roca,1250,y)

            #Game over
            def gameover():
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.8.10
                Descripción: Función que desplega la pantalla de GameOver
                Autor: Jian Yong Zheng Wu
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                global retry,Fondoover,menu,gmeover
                EasyCanvas.delete("all")
                PgCanvas = tk.Canvas(Window, width=1280, height=720)
                PgCanvas.place(x=0, y=0)

                Fondoover = tk.PhotoImage(file="BackgroundMenu/SPACEGRANDE_00.png")
                Fondopg = PgCanvas.create_image(0, 0, image=Fondoover, anchor="nw")

                gmeover= tk.PhotoImage(file="BackgroundMenu/GAMEOVER-22-4-2023.png")
                gmover= PgCanvas.create_image(650,225,image=gmeover,anchor="center")

                finalscore = tk.Label(PgCanvas, text="Final score: " + str(score), bg="black", fg="white",font=("Small Fonts", 35))
                finalscore.place(x=500, y=300)

                scorelist.append(score)

                def Return():
                    global usernamelist
                    usernamelist.append(usernamelist[-1]) #Guardo el ultimo nombre ingresado
                    EasyCanvas.destroy()
                    PgCanvas.delete("all")
                    midmodescreen()

                retry = tk.PhotoImage(file="BackgroundMenu/BOTONRETRY.png")
                ReturnButtonP = tk.Button(Window, image=retry, bd=0, cursor="hand2", bg="black", relief="flat",activebackground="black", command=Return)
                ReturnButtonP.place(x=575, y=400, anchor="center")

                def home():
                    EasyCanvas.destroy()
                    PgCanvas.destroy()
                    Menuprincipal()

                menu = tk.PhotoImage(file="BackgroundMenu/BOTONHOME.png")
                MenuButtonP = tk.Button(Window, image=menu, bd=0, cursor="hand2", bg="black", relief="flat",activebackground="black", command=home)
                MenuButtonP.place(x=725, y=400, anchor="center")

            #Colision del nave y los naves enemigos
            #Las vidas de las naves
            #Gameover
            def colisionnave(npcnve):
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que detecta la colision de nave enemiga con la nave del jugador
               Autor: Jian Yong Zheng Wu y Kathie Quick
               Enlace: https://www.youtube.com/watch?v=_flFVAtmkoQ&list=PLFPWzE_xoI9kdu_Zhtc3zWkGjJPfkKiLS&index=4
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                global life, score
                NC = EasyCanvas.bbox(nve)
                NCNPC = EasyCanvas.bbox(npcnve)
                if (NC[0] < NCNPC[2] and NC[2] > NCNPC[0] and NC[1] < NCNPC[3] and NC[3] > NCNPC[1]):
                    sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                    sonidohit.set_volume(0.1)
                    sonidohit.play()
                    EasyCanvas.coords(npcnve, 1280, random.randint(50,700))
                    life -= 1
                    lifeLabel.config(text=str(life))
                    print(life)
                    if life < 1:
                        gameover()
                    else:
                        lifeLabel.config(text=str(life))
                        EasyCanvas.after(10, colisionnave, npcnve)  # llamada recursiva con el mismo NPC

            def colisionroca(roca):
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que detecta la colision de la nave del jugador con el obstaculo
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                global life, score
                NC = EasyCanvas.bbox(nve)
                NCNPC = EasyCanvas.bbox(roca)
                if NCNPC is not None and (NC[0] < NCNPC[2] and NC[2] > NCNPC[0] and NC[1] < NCNPC[3] and NC[3] > NCNPC[1]):
                    sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                    sonidohit.set_volume(0.1)
                    sonidohit.play()
                    EasyCanvas.coords(roca, 1280, random.randint(50,700))
                    life -= 1
                    lifeLabel.config(text=str(life))
                    print(life)
                    if life < 1:
                        gameover()
                    else:
                        lifeLabel.config(text=str(life))
                        EasyCanvas.after(10, colisionroca, roca)  # llamada recursiva con el mismo NPC

            def colisionlaser(laser):
                global life, score
                NC = EasyCanvas.bbox(nve)
                NCLASER = EasyCanvas.bbox(laser)
                if NCLASER is not None and NC[0] < NCLASER[2] and NC[2] > NCLASER[0] and NC[1] < NCLASER[3] and NC[3] > NCLASER[1]:
                    sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                    sonidohit.set_volume(0.1)
                    sonidohit.play()
                    EasyCanvas.delete(laser)
                    print("laser eliminado")
                    life -= 1
                    lifeLabel.config(text=str(life))
                    print(life)
                    if life < 1:
                        gameover()
                    else:
                        lifeLabel.config(text=str(life))
                        EasyCanvas.after(10, colisionlaser, laser)  # llamada recursiva con el mismo laser

            def colisionlasers(laser):
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que detecta la colision entre los lasers del jugador y del enemigo
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                global laser2, laser3, laser4,roca
                NC = EasyCanvas.bbox(laser)
                if NC is not None:
                    NCLASER = EasyCanvas.bbox(laser2)
                    NCLASER2 = EasyCanvas.bbox(laser3)
                    NCLASER3 = EasyCanvas.bbox(laser4)
                    NCRoca = EasyCanvas.bbox(roca)
                    if NCLASER is not None and NC[0] < NCLASER[2] and NC[2] > NCLASER[0] and NC[1] < NCLASER[3] and NC[3] > NCLASER[1]:
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        if laser is not None:
                            EasyCanvas.delete(laser)
                        if laser2 is not None:
                            EasyCanvas.delete(laser2)
                        print("laser eliminado")
                    elif NCRoca is not None and NC[0] < NCRoca[2] and NC[2] > NCRoca[0] and NC[1] < NCRoca[3] and NC[3] > NCRoca[1]:
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        if laser is not None:
                            EasyCanvas.delete(laser)
                        if roca is not None:
                            pass
                        print("rock eliminado")
                    elif NCLASER2 is not None and NC[0] < NCLASER2[2] and NC[2] > NCLASER2[0] and NC[1] < NCLASER2[3] and NC[3] > NCLASER2[1]:
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        if laser is not None:
                            EasyCanvas.delete(laser)
                        if laser3 is not None:
                            EasyCanvas.delete(laser3)
                        print("laser eliminado")
                    elif NCLASER3 is not None and NC[0] < NCLASER3[2] and NC[2] > NCLASER3[0] and NC[1] < NCLASER3[3] and NC[3] > NCLASER3[1]:
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        if laser is not None:
                            EasyCanvas.delete(laser)
                        if laser4 is not None:
                            EasyCanvas.delete(laser4)
                        print("laser eliminado")
                    else:
                        EasyCanvas.after(10, colisionlasers, laser)  # llamada recursiva con el mismo laser

            #PRIMER NAVE NPC
            #Disparar lasers npc


            def lasernpc1():
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que hace que dispare el primer enemigo
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                global laser2, laser_image
                print("Creando nuevo láser...")
                lsrbbox = EasyCanvas.bbox(npcnve)
                centnpca = ((lsrbbox[0] + lsrbbox[2]) / 2) - 15
                centnpcb = (lsrbbox[1] + lsrbbox[3]) / 2
                laser2 = EasyCanvas.create_image(centnpca, centnpcb, image=Laserimg2, tags="laser")
                sonidoshoot = pygame.mixer.Sound("Sonidos/Disparo2.mp3")
                sonidoshoot.set_volume(0.1)
                sonidoshoot.play()
                mover_laser1(laser2)
                Window.after(3000, lasernpc1)

            def mover_laser1(laser2):
                if laser2 is not None:
                    if EasyCanvas.bbox(laser2) is not None and EasyCanvas.bbox(laser2)[0] < 0:  # Para que el laser llegue hasta el final del borde
                        print("Laser2fuera")
                        EasyCanvas.delete(laser2)
                        laser2 = None
                    else:
                        EasyCanvas.move(laser2, -5, 0)
                        if EasyCanvas.bbox(laser2) is not None:
                            colisionlaser(laser2)

                    Window.after(10, mover_laser1, laser2)

            lasernpc1()

            # SEGUNDO NAVE NPC
            def lasernpc2():
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que hace que dispare el segundo enemigo
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                global laser3
                print("Creando nuevo láser2...")
                lsrbbox2 = EasyCanvas.bbox(npcnve2)
                centnpca2 = ((lsrbbox2[0] + lsrbbox2[2]) / 2) - 15
                centnpcb2 = (lsrbbox2[1] + lsrbbox2[3]) / 2
                laser3 = EasyCanvas.create_image(centnpca2, centnpcb2, image=Laserimg3, tags="laser3")
                mover_laser2(laser3)
                Window.after(3000, lasernpc2)

            def mover_laser2(laser3):
                if laser3 is not None:
                    if EasyCanvas.bbox(laser3) is not None and EasyCanvas.bbox(laser3)[0] < 0:  # Para que el laser llegue hasta el final del borde
                        print("Laser3fuera")
                        EasyCanvas.delete(laser3)
                        laser3 = None
                    else:
                        EasyCanvas.move(laser3, -5, 0)
                        if EasyCanvas.bbox(laser3) is not None:
                            colisionlaser(laser3)

                    Window.after(10, mover_laser2, laser3)

            lasernpc2()

            #Nave npc 3 disparar
            def lasernpc3():
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que hace que dispare el tercer enemigo
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                global laser4
                print("Creando nuevo láser3...")
                lsrbbox3 = EasyCanvas.bbox(npcnve3)
                centnpca3 = ((lsrbbox3[0] + lsrbbox3[2]) / 2) - 15
                centnpcb3 = (lsrbbox3[1] + lsrbbox3[3]) / 2
                laser4 = EasyCanvas.create_image(centnpca3, centnpcb3, image=Laserimg4, tags="laser4")
                mover_laser3(laser4)
                Window.after(3000, lasernpc3)

            def mover_laser3(laser4):
                if laser4 is not None:
                    if EasyCanvas.bbox(laser4) is not None and EasyCanvas.bbox(laser4)[0] < 0:  # Para que el laser llegue hasta el final del borde
                        print("Laser4fuera")
                        EasyCanvas.delete(laser4)
                        laser4 = None
                    else:
                        EasyCanvas.move(laser4, -5, 0)
                        if EasyCanvas.bbox(laser4) is not None:
                            colisionlaser(laser4)

                    Window.after(10, mover_laser3, laser4)

            lasernpc3()

            def NPCMove():
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que hace que se muevan los enemigos
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                edgereacheda()
                EasyCanvas.move(npcnve, -5, 0)
                EasyCanvas.move(npcnve2, -6, 0)
                EasyCanvas.move(npcnve3, -7, 0)
                colisionnave(npcnve)
                colisionnave(npcnve2)
                colisionnave(npcnve3)
                Window.after(25, NPCMove)

            NPCMove()

            def RocaMove():
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que hace que se mueva la piedra
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                edgereacheda()
                EasyCanvas.move(roca,-5,0)
                colisionroca(roca)
                Window.after(10,RocaMove)

            RocaMove()

            #Colision del laser y la nave enemiga
            #PRUEBA 1
            laser=None
            def shoot(event):
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función para disparar laser
                Autor: Chat GPT y una parte por Jian Yong Zheng Wu
                Enlace: https://chat.openai.com/
                Fecha última modificación: Abril 22 de 2023
                Entradas: []
                Restricciones: []
                Salidas: Disparo del laser del nave de jugador
                ******************************************************"""
                global laser
                global ultimo_tiempo
                tiempoactual = time.time()  # Obtiene el tiempo actual
                # Comprueba si ha pasado al menos 0.5 segundos desde el último disparo
                if tiempoactual - ultimo_tiempo >= 0.5:
                    ultimo_tiempo = tiempoactual  # Actualiza el tiempo del último disparo
                    x, y = EasyCanvas.coords(nve) #Usamos .coords para saber donde esta la nave y establecer el x y el y
                    laser = EasyCanvas.create_image(x+15, y, image=Laserimg)  #Para que el laser salga en el centro de la nave
                    mover_laser(laser, 0) # Define una función recursiva para mover un láser hacia la derecha en cada actualización del juego
                    sonidodisparar = pygame.mixer.Sound("Sonidos/Disparoo.mp3")
                    sonidodisparar.set_volume(0.1)
                    sonidodisparar.play()

            def mover_laser(laser, count):
                """*******************************************************
                               Instituto Tecnológico de Costa Rica
                                   Ingenería en Computadores
                       Lenguaje: Python 3.11
                       Descripción: Función para disparar laser
                       Autor: Chat GPT y una parte por Jian Yong Zheng Wu
                       Enlace: https://chat.openai.com/
                       Fecha última modificación: Abril 22 de 2023
                       Entradas: []
                       Restricciones: []
                       Salidas: Mueve el laser
                       ******************************************************"""
                global score
                colisionlasers(laser)
                if count == 240:  # Para que el laser llegue hasta el final del borde
                    EasyCanvas.delete(laser)
                elif EasyCanvas.bbox(laser) is not None and EasyCanvas.bbox(laser)[2] > 1280:
                    EasyCanvas.delete(laser)
                else:
                    EasyCanvas.move(laser, 9, 0)
                    if colision(laser, npcnve): #Colision de laser con algun nave enemigo
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        score = score + 10**2 #Suma 100 si mata a un enemigo
                        scoreLabel.config(text="Score: " + str(score)) #Se actualiza el score
                        EasyCanvas.delete(laser) #Se borra el laser
                        EasyCanvas.coords(npcnve, 1250, random.randint(50, 700)) #Se genera en otra ubicacion
                    elif colision(laser, npcnve2): #Colision de laser con algun nave enemigo
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        score = score + 10**2 #Suma 100 si mata a un enemigo
                        scoreLabel.config(text="Score: " + str(score)) #Se actualiza el score
                        EasyCanvas.delete(laser) #Se borra el laser
                        EasyCanvas.coords(npcnve2, 1250, random.randint(50, 700)) #Se genera en otra ubicacion
                    elif colision(laser, npcnve3): #Colision de laser con algun nave enemigo
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        score = score + 10**2 #Suma 100 si mata a un enemigo
                        scoreLabel.config(text="Score: " + str(score)) #Se actualiza el score
                        EasyCanvas.delete(laser) #Se borra el laser
                        EasyCanvas.coords(npcnve3, 1250, random.randint(50, 700)) #Se genera en otra ubicacion
                    else:
                        EasyCanvas.after(15, mover_laser, laser, count + 1) #Actualiza la funcion, el count es para ver cuantas veces ha llamado la funcion
                        #se verifica que el valor de count no sea mayor que 240, lo que garantiza que el láser no se mueva más allá del borde de la pantalla.

            def colision(laser, npcnve):  # Colision del laser y la nave npc
                npc_coords = EasyCanvas.coords(npcnve)
                if not npc_coords or not EasyCanvas.find_withtag(laser):  # se utiliza para buscar el objeto "laser" en el
                    # lienzo y verificar si existe antes de intentar obtener sus coordenadas.
                    return False  # Tiraba error y no podia disparar de nuevo

                npc_x, npc_y = npc_coords  # Asignamos variables
                laser_x, laser_y = EasyCanvas.coords(laser)  # Asignamos variables

                xx = laser_x - npc_x  # Resta de pixeles
                yy = laser_y - npc_y  # Resta de pixeles

                return xx < 30 and yy < 30 and xx > -30 and yy > -30
            # Si xx y yy son menores que 30 y mayores que -30, significa que el láser está a una distancia máxima de 20 píxeles
            # del NPC en ambas direcciones (horizontal y vertical), por lo que se considera que ha habido una colisión.

            #Seccion de movilidad
            def up(event): #Mover arriba
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función hacer mover la imagen a traves del teclado
               Autor: Codemy.com
               Enlace: https://www.youtube.com/watch?v=2rF8-jbTL-8
               Fecha última modificación: Abril 22 de 2023
               Entradas: W o w
               Restricciones: []
               Salidas: Mover 10 pixeles arriba
               ******************************************************"""
                x = 0
                y = -10
                if EasyCanvas.coords(nve)[1] + y > 0:  # check if the new y-coordinate is within the top boundary
                    EasyCanvas.move(nve, x, y) #En el canvas utilizando el .move, se mueve la nave en x y en y

            def down(event): #Mover abajo
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función hacer mover la imagen a traves del teclado
               Autor: Codemy.com
               Enlace: https://www.youtube.com/watch?v=2rF8-jbTL-8
               Fecha última modificación: Abril 22 de 2023
               Entradas: S o s
               Restricciones: []
               Salidas: Mover 10 pixeles abajo
               ******************************************************"""
                x = 0
                y = 10
                if EasyCanvas.coords(nve)[1] + y < EasyCanvas.winfo_height():  # check if the new y-coordinate is within the bottom boundary
                    EasyCanvas.move(nve, x, y)

            def left(event): #Mover izquierda
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función hacer mover la imagen a traves del teclado
               Autor: Codemy.com
               Enlace: https://www.youtube.com/watch?v=2rF8-jbTL-8
               Fecha última modificación: Abril 22 de 2023
               Entradas: A o a
               Restricciones: []
               Salidas: Mover 10 pixeles izquierda
               ******************************************************"""
                x = -10
                y = 0
                if EasyCanvas.coords(nve)[0] + x > 0:  # check if the new x-coordinate is within the left boundary
                    EasyCanvas.move(nve, x, y)

            def right(event): #Mover derecha
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función hacer mover la imagen a traves del teclado
               Autor: Codemy.com
               Enlace: https://www.youtube.com/watch?v=2rF8-jbTL-8
               Fecha última modificación: Abril 22 de 2023
               Entradas: D o d
               Restricciones: []
               Salidas: Mover 10 pixeles derecha
               ******************************************************"""
                x = 10
                y = 0
                if EasyCanvas.coords(nve)[0] + x < EasyCanvas.winfo_width():  # check if the new x-coordinate is within the right boundary
                    EasyCanvas.move(nve, x, y)

            #Seccion de asignacion de teclas para mover la nave y disparar
            Window.bind("<w>", up)
            Window.bind("<s>", down)
            Window.bind("<a>", left)
            Window.bind("<d>", right)
            Window.bind("<W>", up)
            Window.bind("<S>", down)
            Window.bind("<A>", left)
            Window.bind("<D>", right)
            Window.bind("<space>", shoot)

            Thread(target=Movingbackground, args=(lenn(Background) - 1,)).start()

        def hardmodescreen():
            """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Dificultad dificil
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
            global FondoEasy,Nave,NPCNave,score,NPCNave2,NPCNave3,lifeLabel,Heart,life,ultimo_tiempo,npcnave,Laserimg,Rock,Laserimg2
            global laser_en_pantalla,Laserimg3,Laserimg4,laser_en_pantalla2,laser_en_pantalla3,tiempo_ultimo_laser
            global tiempo_ultimo_laser2,tiempo_ultimo_laser3,rocas, NPCNave4,roca
            #Para parar la musica en esta ventana

            labelDestroy(temp) #Destruye los elementos de la pantalla anterior

            EasyCanvas = tk.Canvas(Window, width=1280, height=720)
            EasyCanvas.place(x=0, y=0)

            Background = cargarSprites("Moving_*")  # Se cargan los sprites del fondo
            BG = EasyCanvas.create_image(0,0)  # Se les da una posicion inicial

            def Movingbackground(i):  # Se crea una funcion recursiva que anima el fondo
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función que mueve el fondo
                Autor: Arturo Acuña Duran
                Entradas: imágenes
                Restricciones: []
                Salidas: los frames de las imagenes
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                if (i >= lenn(Background)):  # La funcion itera mientras el valor de i no sea mayor a la cantidad de fotos
                    i = 0  # Si i es mayor a la cantidad de fotos, se vuelve a iniciar el contador
                EasyCanvas.itemconfig(BG, image=Background[i],anchor="nw")  # Se cambia la imagen
                time.sleep(0.1)  # Se espera un momento
                Thread(target=Movingbackground, args=(i + 1,)).start()  # Se hace una llamada recurisva en un hilo aumentando i una unidad

            #Nave principal
            Nave=tk.PhotoImage(file="BackgroundMenu/NAVEPRINCIPAL.png")
            nve=EasyCanvas.create_image(50,360,image=Nave,anchor="center")

            #Imagen el laser
            Laserimg=tk.PhotoImage(file="BackgroundMenu/LASER.png")
            Laserimg2 = tk.PhotoImage(file="BackgroundMenu/LASER2.png")
            Laserimg3 = tk.PhotoImage(file="BackgroundMenu/LASER3.png")
            Laserimg4 = tk.PhotoImage(file="BackgroundMenu/LASER4.png")


            #Coordenadas para que aparezcan las naves en lugares aleatorias
            #Naves enemigas
            npcX1 = random.randint(980, 1250)
            npcY1 = random.randint(50, 720)

            npcX2 = random.randint(980, 1280)
            npcY2 = random.randint(50, 720)

            npcX3 = random.randint(980, 1250)
            npcY3 = random.randint(50, 720)

            npcX4 = 900
            npcY4 = random.randint(50, 720)

            NPCNave = tk.PhotoImage(file="BackgroundMenu/NAVENPC.png")
            npcnve = EasyCanvas.create_image(npcX1, npcY1, image=NPCNave)

            NPCNave2 = tk.PhotoImage(file="BackgroundMenu/NAVENPC2.png")
            npcnve2 = EasyCanvas.create_image(npcX2, npcY2, image=NPCNave2)

            NPCNave3 = tk.PhotoImage(file="BackgroundMenu/NAVENPC3.png")
            npcnve3 = EasyCanvas.create_image(npcX3, npcY3, image=NPCNave3)

            NPCNave4 = tk.PhotoImage(file="BackgroundMenu/NAVENPC4.png")
            npcnve4 = EasyCanvas.create_image(npcX4, npcY4, image=NPCNave4)

            #Imagen de la roca
            Rock= tk.PhotoImage(file="BackgroundMenu/ROCA 48.png")
            roca= EasyCanvas.create_image(1280,npcY1,image=Rock)

            #Seccion de retraso en el disparo de laser
            ultimo_tiempo = 0  # Definir afuera de todo como una variable que no sea local

            #Seccion para el nivel
            lvleasy=tk.Label(EasyCanvas,text="Hard",bg="black",fg="red",font=("Small Fonts",14))
            lvleasy.place(x=1030,y=40,anchor="center")

            #Seccion de score
            score=0
            scoreLabel=tk.Label(EasyCanvas,text="Score: "+str(score),bg="black",fg="white",font=("Small Fonts",14))
            scoreLabel.place(x=1200,y=40,anchor="center")

            # Imagen de life
            Heart = tk.PhotoImage(file="BackgroundMenu/heart pixel art 32x32.png")
            heart1 = EasyCanvas.create_image(1090, 40, image=Heart)

            #Seccion de life
            life=3
            lifeLabel=tk.Label(EasyCanvas,text=str(life),bg="black",fg="white",font=("Small Fonts",14))
            lifeLabel.place(x=1125,y=40,anchor="center")

            def edgereacheda():
                """*******************************************************
                            Instituto Tecnológico de Costa Rica
                                Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función que detecta el borde de la pantalla
                Autor: Kathie Quick
                Enlace: https://www.youtube.com/watch?v=g5qJEJjEOa4
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                Npcnaveboundary= EasyCanvas.bbox(npcnve)
                Npcnave2boundary = EasyCanvas.bbox(npcnve2)
                Npcnave3boundary = EasyCanvas.bbox(npcnve3)
                Npcnave4boundary = EasyCanvas.bbox(npcnve4)
                Npcnave5boundary = EasyCanvas.bbox(roca)
                y=random.randint(50,700)
                if Npcnaveboundary[0] < 0:
                    EasyCanvas.coords(npcnve,1250,y)
                if Npcnave2boundary[0] < 0:
                    EasyCanvas.coords(npcnve2, 1250, y)
                if Npcnave3boundary[0] < 0:
                    EasyCanvas.coords(npcnve3,1250,y)
                if Npcnave4boundary[0] < 0:
                    EasyCanvas.coords(npcnve4,1250,y)
                if Npcnave5boundary[0] < 0:
                    EasyCanvas.coords(roca,1250,y)

            #Game over
            def gameover():
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.8.10
                Descripción: Función que desplega la pantalla de GameOver
                Autor: Jian Yong Zheng Wu
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                global retry,Fondoover,menu,gmeover
                EasyCanvas.delete("all")
                PgCanvas = tk.Canvas(Window, width=1280, height=720)
                PgCanvas.place(x=0, y=0)

                Fondoover = tk.PhotoImage(file="BackgroundMenu/SPACEGRANDE_00.png")
                Fondopg = PgCanvas.create_image(0, 0, image=Fondoover, anchor="nw")

                gmeover= tk.PhotoImage(file="BackgroundMenu/GAMEOVER-22-4-2023.png")
                gmover= PgCanvas.create_image(650,225,image=gmeover,anchor="center")

                finalscore = tk.Label(PgCanvas, text="Final score: " + str(score), bg="black", fg="white",font=("Small Fonts", 35))
                finalscore.place(x=500, y=300)

                scorelist.append(score)

                def Return():
                    global usernamelist
                    usernamelist.append(usernamelist[-1]) #Guardo el ultimo nombre agregado
                    EasyCanvas.destroy()
                    PgCanvas.delete("all")
                    hardmodescreen()

                retry = tk.PhotoImage(file="BackgroundMenu/BOTONRETRY.png")
                ReturnButtonP = tk.Button(Window, image=retry, bd=0, cursor="hand2", bg="black", relief="flat",activebackground="black", command=Return)
                ReturnButtonP.place(x=575, y=400, anchor="center")

                def home():
                    EasyCanvas.destroy()
                    PgCanvas.destroy()
                    Menuprincipal()

                menu = tk.PhotoImage(file="BackgroundMenu/BOTONHOME.png")
                MenuButtonP = tk.Button(Window, image=menu, bd=0, cursor="hand2", bg="black", relief="flat",activebackground="black", command=home)
                MenuButtonP.place(x=725, y=400, anchor="center")

            #Colision del nave y los naves enemigos
            #Las vidas de las naves
            #Gameover
            def colisionnave(npcnve):
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que detecta la colision de nave enemiga con la nave del jugador
               Autor: Jian Yong Zheng Wu y Kathie Quick
               Enlace: https://www.youtube.com/watch?v=_flFVAtmkoQ&list=PLFPWzE_xoI9kdu_Zhtc3zWkGjJPfkKiLS&index=4
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                global life, score
                NC = EasyCanvas.bbox(nve)
                NCNPC = EasyCanvas.bbox(npcnve)
                if (NC[0] < NCNPC[2] and NC[2] > NCNPC[0] and NC[1] < NCNPC[3] and NC[3] > NCNPC[1]):
                    sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                    sonidohit.set_volume(0.1)
                    sonidohit.play()
                    EasyCanvas.coords(npcnve, 1280, random.randint(50,700))
                    life -= 1
                    lifeLabel.config(text=str(life))
                    print(life)
                    if life < 1:
                        gameover()
                    else:
                        lifeLabel.config(text=str(life))
                        EasyCanvas.after(10, colisionnave, npcnve)  # llamada recursiva con el mismo NPC

            def colisionroca(roca):
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que detecta la colision de la nave del jugador con el obstaculo
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                global life, score
                NC = EasyCanvas.bbox(nve)
                NCNPC = EasyCanvas.bbox(roca)
                if NCNPC is not None and (NC[0] < NCNPC[2] and NC[2] > NCNPC[0] and NC[1] < NCNPC[3] and NC[3] > NCNPC[1]):
                    sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                    sonidohit.set_volume(0.1)
                    sonidohit.play()
                    EasyCanvas.coords(roca, 1280, random.randint(50,700))
                    life -= 1
                    lifeLabel.config(text=str(life))
                    print(life)
                    if life < 1:
                        gameover()
                    else:
                        lifeLabel.config(text=str(life))
                        EasyCanvas.after(10, colisionroca, roca)  # llamada recursiva con el mismo NPC

            def colisionlaser(laser):
                global life, score
                NC = EasyCanvas.bbox(nve)
                NCLASER = EasyCanvas.bbox(laser)
                if NCLASER is not None and NC[0] < NCLASER[2] and NC[2] > NCLASER[0] and NC[1] < NCLASER[3] and NC[3] > NCLASER[1]:
                    sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                    sonidohit.set_volume(0.1)
                    sonidohit.play()
                    print("Colision laser enemiga a nave jugador") #El None es una verificación adicional para asegurar que el láser todavía existe antes de continuar con la verificación de colisión.
                    EasyCanvas.delete(laser)
                    print("laser eliminado")
                    life -= 1
                    lifeLabel.config(text=str(life))
                    print(life)
                    if life < 1:
                        gameover()
                    else:
                        lifeLabel.config(text=str(life))
                        EasyCanvas.after(10, colisionlaser, laser)  # llamada recursiva con el mismo laser

            def colisionlasers(laser):
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función que detecta la colision entre los lasers del jugador y del enemigo
                Autor: Jian Yong Zheng Wu
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                global laser2, laser3, laser4,roca, laser5
                NC = EasyCanvas.bbox(laser)
                if NC is not None:
                    NCLASER = EasyCanvas.bbox(laser2)
                    NCLASER2 = EasyCanvas.bbox(laser3)
                    NCLASER3 = EasyCanvas.bbox(laser4)
                    NCLASER4 = EasyCanvas.bbox(laser5)
                    NCRoca= EasyCanvas.bbox(roca)
                    if NCLASER is not None and NC[0] < NCLASER[2] and NC[2] > NCLASER[0] and NC[1] < NCLASER[3] and NC[3] > NCLASER[1]:
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        print("Colision de lasers")
                        if laser is not None:
                            EasyCanvas.delete(laser)
                        if laser2 is not None:
                            EasyCanvas.delete(laser2)
                        print("laser eliminado")
                    elif NCRoca is not None and NC[0] < NCRoca[2] and NC[2] > NCRoca[0] and NC[1] < NCRoca[3] and NC[3] > NCRoca[1]:
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        print("Franco")
                        if laser is not None:
                            EasyCanvas.delete(laser)
                        if roca is not None:
                            pass
                        print("roca eliminado")
                    elif NCLASER2 is not None and NC[0] < NCLASER2[2] and NC[2] > NCLASER2[0] and NC[1] < NCLASER2[3] and NC[3] > NCLASER2[1]:
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        print("Colision de lasers")
                        if laser is not None:
                            EasyCanvas.delete(laser)
                        if laser3 is not None:
                            EasyCanvas.delete(laser3)
                        print("laser eliminado")
                    elif NCLASER3 is not None and NC[0] < NCLASER3[2] and NC[2] > NCLASER3[0] and NC[1] < NCLASER3[3] and NC[3] > NCLASER3[1]:
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        print("Colision de lasers")
                        if laser is not None:
                            EasyCanvas.delete(laser)
                        if laser4 is not None:
                            EasyCanvas.delete(laser4)
                        print("laser eliminado")
                    elif NCLASER4 is not None and NC[0] < NCLASER4[2] and NC[2] > NCLASER4[0] and NC[1] < NCLASER4[3] and NC[3] > NCLASER4[1]:
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        print("Colision de lasers")
                        if laser is not None:
                            EasyCanvas.delete(laser)
                        if laser5 is not None:
                            EasyCanvas.delete(laser5)
                        print("laser eliminado")
                    else:
                        EasyCanvas.after(10, colisionlasers, laser)  # llamada recursiva con el mismo laser


            #PRIMER NAVE NPC
            #Disparar lasers npc

            def lasernpc1():
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función que hace que dispare el primer enemigo
                Autor: Jian Yong Zheng Wu
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                global laser2, laser_image
                print("Creando nuevo láser...")
                lsrbbox = EasyCanvas.bbox(npcnve)
                centnpca = ((lsrbbox[0] + lsrbbox[2]) / 2) - 15
                centnpcb = (lsrbbox[1] + lsrbbox[3]) / 2
                laser2 = EasyCanvas.create_image(centnpca, centnpcb, image=Laserimg2, tags="laser")
                sonidoshoot = pygame.mixer.Sound("Sonidos/Disparo2.mp3")
                sonidoshoot.set_volume(0.1)
                sonidoshoot.play()
                mover_laser1(laser2)
                Window.after(2500, lasernpc1)

            def mover_laser1(laser2):
                if laser2 is not None:
                    if EasyCanvas.bbox(laser2) is not None and EasyCanvas.bbox(laser2)[0] < 0:  # Para que el laser llegue hasta el final del borde
                        print("Laser2fuera")
                        EasyCanvas.delete(laser2)
                        laser2 = None
                    else:
                        EasyCanvas.move(laser2, -5, 0)
                        if EasyCanvas.bbox(laser2) is not None:
                            colisionlaser(laser2)

                    Window.after(10, mover_laser1, laser2)

            lasernpc1()

            # SEGUNDO NAVE NPC
            def lasernpc2():
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función que hace que dispare el segundo enemigo
                Autor: Jian Yong Zheng Wu
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                global laser3
                print("Creando nuevo láser2...")
                lsrbbox2 = EasyCanvas.bbox(npcnve2)
                centnpca2 = ((lsrbbox2[0] + lsrbbox2[2]) / 2) - 15
                centnpcb2 = (lsrbbox2[1] + lsrbbox2[3]) / 2
                laser3 = EasyCanvas.create_image(centnpca2, centnpcb2, image=Laserimg3, tags="laser3")
                mover_laser2(laser3)
                Window.after(2500, lasernpc2)

            def mover_laser2(laser3):
                if laser3 is not None:
                    if EasyCanvas.bbox(laser3) is not None and EasyCanvas.bbox(laser3)[0] < 0:  # Para que el laser llegue hasta el final del borde
                        print("Laser3fuera")
                        EasyCanvas.delete(laser3)
                        laser3 = None
                    else:
                        EasyCanvas.move(laser3, -5, 0)
                        if EasyCanvas.bbox(laser3) is not None:
                            colisionlaser(laser3)

                    Window.after(10, mover_laser2, laser3)

            lasernpc2()

            #Nave npc 3 disparar
            def lasernpc3():
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función que hace que dispare el tercer enemigo
                Autor: Jian Yong Zheng Wu
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                global laser4
                print("Creando nuevo láser3...")
                lsrbbox3 = EasyCanvas.bbox(npcnve3)
                centnpca3 = ((lsrbbox3[0] + lsrbbox3[2]) / 2) - 15
                centnpcb3 = (lsrbbox3[1] + lsrbbox3[3]) / 2
                laser4 = EasyCanvas.create_image(centnpca3, centnpcb3, image=Laserimg4, tags="laser4")
                mover_laser3(laser4)
                Window.after(2500, lasernpc3)

            def mover_laser3(laser4):
                if laser4 is not None:
                    if EasyCanvas.bbox(laser4) is not None and EasyCanvas.bbox(laser4)[0] < 0:  # Para que el laser llegue hasta el final del borde
                        print("Laser4fuera")
                        EasyCanvas.delete(laser4)
                        laser4 = None
                    else:
                        EasyCanvas.move(laser4, -5, 0)
                        if EasyCanvas.bbox(laser4) is not None:
                            colisionlaser(laser4)

                    Window.after(10, mover_laser3, laser4)

            lasernpc3()

            #Cuarta nave disparar
            def lasernpc4():
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función que hace que dispare el cuarto enemigo
                Autor: Jian Yong Zheng Wu
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                global laser5

                print("Creando nuevo láser3...")
                lsrbbox4 = EasyCanvas.bbox(npcnve4)
                centnpca4 = ((lsrbbox4[0] + lsrbbox4[2]) / 2) - 15
                centnpcb4 = (lsrbbox4[1] + lsrbbox4[3]) / 2
                laser5 = EasyCanvas.create_image(centnpca4, centnpcb4, image=Laserimg, tags="laser5")
                mover_laser4(laser5)
                Window.after(2500, lasernpc4)

            def mover_laser4(laser5):
                if laser5 is not None:
                    if EasyCanvas.bbox(laser5) is not None and EasyCanvas.bbox(laser5)[0] < 0:  # Para que el laser llegue hasta el final del borde
                        print("Laser5fuera")
                        EasyCanvas.delete(laser5)
                        laser5 = None
                    else:
                        EasyCanvas.move(laser5, -5, 0)
                        if EasyCanvas.bbox(laser5) is not None:
                            colisionlaser(laser5)

                    Window.after(10, mover_laser4, laser5)

            lasernpc4()

            def NPCMove():
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función que hace que se muevan los enemigos
               Autor: Jian Yong Zheng Wu
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
                edgereacheda()
                EasyCanvas.move(npcnve, -6, 0)
                EasyCanvas.move(npcnve2, -5, 0)
                EasyCanvas.move(npcnve3, -4, 0)
                EasyCanvas.move(npcnve4,-7,0)
                colisionnave(npcnve)
                colisionnave(npcnve2)
                colisionnave(npcnve3)
                colisionnave(npcnve4)
                Window.after(25, NPCMove)

            NPCMove()

            def RocaMove():
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función que hace que se mueva la piedra
                Autor: Jian Yong Zheng Wu
                Fecha última modificación: Abril 22 de 2023
                ******************************************************"""
                edgereacheda()
                EasyCanvas.move(roca, -5, 0)
                colisionroca(roca)
                Window.after(10, RocaMove)

            RocaMove()

            #Colision del laser y la nave enemiga
            #PRUEBA 1
            laser=None

            def shoot(event):
                """*******************************************************
                        Instituto Tecnológico de Costa Rica
                            Ingenería en Computadores
                Lenguaje: Python 3.11
                Descripción: Función para disparar laser
                Autor: Chat GPT y una parte por Jian Yong Zheng Wu
                Enlace: https://chat.openai.com/
                Fecha última modificación: Abril 22 de 2023
                Entradas: []
                Restricciones: []
                Salidas: Disparo del laser del nave de jugador
                ******************************************************"""
                global laser
                global ultimo_tiempo
                tiempoactual = time.time()  # Obtiene el tiempo actual
                # Comprueba si ha pasado al menos 0.5 segundos desde el último disparo
                if tiempoactual - ultimo_tiempo >= 0.5:
                    ultimo_tiempo = tiempoactual  # Actualiza el tiempo del último disparo
                    x, y = EasyCanvas.coords(nve) #Usamos .coords para saber donde esta la nave y establecer el x y el y
                    laser = EasyCanvas.create_image(x+20, y, image=Laserimg)  #Para que el laser salga en el centro de la nave
                    mover_laser(laser, 0) # Define una función recursiva para mover un láser hacia la derecha en cada actualización del juego
                    sonidodisparar = pygame.mixer.Sound("Sonidos/Disparoo.mp3")
                    sonidodisparar.set_volume(0.1)
                    sonidodisparar.play()

            def mover_laser(laser, count):
                """*******************************************************
                                Instituto Tecnológico de Costa Rica
                                    Ingenería en Computadores
                        Lenguaje: Python 3.11
                        Descripción: Función para disparar laser
                        Autor: Chat GPT y una parte por Jian Yong Zheng Wu
                        Enlace: https://chat.openai.com/
                        Fecha última modificación: Abril 22 de 2023
                        Entradas: []
                        Restricciones: []
                        Salidas: Mueve el laser
                        ******************************************************"""
                global score
                colisionlasers(laser)
                if count == 240:  # Para que el laser llegue hasta el final del borde
                    EasyCanvas.delete(laser)
                elif EasyCanvas.bbox(laser) is not None and EasyCanvas.bbox(laser)[2] > 1280:
                    print("laser eliminado")
                    EasyCanvas.delete(laser)
                else:
                    EasyCanvas.move(laser, 9, 0)
                    if colision(laser, npcnve):
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        score = score + 10**2
                        scoreLabel.config(text="Score: " + str(score))
                        EasyCanvas.delete(laser)
                        EasyCanvas.coords(npcnve, 1250, random.randint(50, 700))
                    elif colision(laser, npcnve2):
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        score += 150
                        scoreLabel.config(text="Score: " + str(score))
                        EasyCanvas.delete(laser)
                        EasyCanvas.coords(npcnve2, 1250, random.randint(50, 700))
                    elif colision(laser, npcnve3):
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        score += 150
                        scoreLabel.config(text="Score: " + str(score))
                        EasyCanvas.delete(laser)
                        EasyCanvas.coords(npcnve3, 1250, random.randint(50, 700))
                    elif colision(laser, npcnve4):
                        sonidohit = pygame.mixer.Sound("Sonidos/Impacto.mp3")
                        sonidohit.set_volume(0.1)
                        sonidohit.play()
                        score += 150
                        scoreLabel.config(text="Score: " + str(score))
                        EasyCanvas.delete(laser)
                        EasyCanvas.coords(npcnve4, 1250, random.randint(50, 700))
                    else:
                        EasyCanvas.after(15, mover_laser, laser, count + 1)#Actualiza la funcion, el count es para ver cuantas veces ha llamado la funcion
                        #se verifica que el valor de count no sea mayor que 240, lo que garantiza que el láser no se mueva más allá del borde de la pantalla.

            def colision(laser, npcnve):  # Colision del laser y la nave npc
                npc_coords = EasyCanvas.coords(npcnve)
                if not npc_coords or not EasyCanvas.find_withtag(laser):  # se utiliza para buscar el objeto "laser" en el
                    # lienzo y verificar si existe antes de intentar obtener sus coordenadas.
                    return False  # Tiraba error y no podia disparar de nuevo

                npc_x, npc_y = npc_coords  # Asignamos variables
                laser_x, laser_y = EasyCanvas.coords(laser)  # Asignamos variables

                xx = laser_x - npc_x  # Resta de pixeles
                yy = laser_y - npc_y

                return xx < 30 and yy < 30 and xx > -30 and yy > -30
            # Si xx y yy son menores que 30 y mayores que -30, significa que el láser está a una distancia máxima de 20 píxeles
            # del NPC en ambas direcciones (horizontal y vertical), por lo que se considera que ha habido una colisión.

            #Seccion de movilidad
            def up(event): #Mover arriba
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función hacer mover la imagen a traves del teclado
               Autor: Codemy.com
               Enlace: https://www.youtube.com/watch?v=2rF8-jbTL-8
               Fecha última modificación: Abril 22 de 2023
               Entradas: W o w
               Restricciones: []
               Salidas: Mover 10 pixeles arriba
               ******************************************************"""
                x = 0
                y = -10
                if EasyCanvas.coords(nve)[1] + y > 0:  # check if the new y-coordinate is within the top boundary
                    EasyCanvas.move(nve, x, y) #En el canvas utilizando el .move, se mueve la nave en x y en y

            def down(event): #Mover abajo
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función hacer mover la imagen a traves del teclado
               Autor: Codemy.com
               Enlace: https://www.youtube.com/watch?v=2rF8-jbTL-8
               Fecha última modificación: Abril 22 de 2023
               Entradas: S o s
               Restricciones: []
               Salidas: Mover 10 pixeles abajo
               ******************************************************"""
                x = 0
                y = 10
                if EasyCanvas.coords(nve)[1] + y < EasyCanvas.winfo_height():  # check if the new y-coordinate is within the bottom boundary
                    EasyCanvas.move(nve, x, y)

            def left(event): #Mover izquierda
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función hacer mover la imagen a traves del teclado
               Autor: Codemy.com
               Enlace: https://www.youtube.com/watch?v=2rF8-jbTL-8
               Fecha última modificación: Abril 22 de 2023
               Entradas: A o a
               Restricciones: []
               Salidas: Mover 10 pixeles izquierda
               ******************************************************"""
                x = -10
                y = 0
                if EasyCanvas.coords(nve)[0] + x > 0:  # check if the new x-coordinate is within the left boundary
                    EasyCanvas.move(nve, x, y)

            def right(event): #Mover derecha
                """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Función hacer mover la imagen a traves del teclado
               Autor: Codemy.com
               Enlace: https://www.youtube.com/watch?v=2rF8-jbTL-8
               Fecha última modificación: Abril 22 de 2023
               Entradas: W o w
               Restricciones: []
               Salidas: Mover 10 pixeles derecha
               ******************************************************"""
                x = 10
                y = 0
                if EasyCanvas.coords(nve)[0] + x < EasyCanvas.winfo_width():  # check if the new x-coordinate is within the right boundary
                    EasyCanvas.move(nve, x, y)

            #Seccion de asignacion de teclas para mover la nave y disparar
            Window.bind("<w>", up)
            Window.bind("<s>", down)
            Window.bind("<a>", left)
            Window.bind("<d>", right)
            Window.bind("<W>", up)
            Window.bind("<S>", down)
            Window.bind("<A>", left)
            Window.bind("<D>", right)
            Window.bind("<space>", shoot)

            Thread(target=Movingbackground, args=(lenn(Background) - 1,)).start()

        LabelUsername = tk.Label(Window, text="Select your difficulty", font=("Small Fonts", 14), fg="white",bg="black")  # Para escribir sobre el fondo de pantalla
        LabelUsername.place(x=500, y=250, anchor="center")
        temp.append(LabelUsername)

        Easy = tk.Button(Window,image=imgeasy,bd=0,cursor="hand2",bg="black",relief="flat",activebackground="black",command=easyvalidation)
        Easy.place(x=650, y=250, anchor="center")
        temp.append(Easy)
        Medium = tk.Button(Window,image=imgmed,bd=0,cursor="hand2",bg="black",relief="flat",activebackground="black",command=midvalidation)
        Medium.place(x=650, y=325,anchor="center")
        temp.append(Medium)
        Hard = tk.Button(Window,image=imghard,bd=0,cursor="hand2",bg="black",relief="flat",activebackground="black",command=hardvalidation)
        Hard.place(x=650, y=400,anchor="center")
        temp.append(Hard)

        def Return():
            labelDestroy(temp) #Destruye los elementos del menu login
            Menuprincipal()

        ReturnButton = tk.Button(Window,image=imgret,bd=0,cursor="hand2",bg="black",relief="flat",activebackground="black", command=Return)
        ReturnButton.place(x=80, y=40, anchor="center")

    Boton1 = tk.Button(Window,image=imglogin,bd=0,cursor="hand2",bg="black",relief="flat",activebackground="black", command=LoginMenu)
    Boton1.place(x=650, y=200, anchor="center")
    temp.append(Boton1)

    def infoadi():
        message= "Move with wasd or WASD and shoot with SPACE\n Enjoy the game!"
        tk.messagebox.showinfo("Hi!", message)

    addinfo=tk.PhotoImage(file="BackgroundMenu/ADDITIONALINFO.png")
    Botonex= tk.Button(Window,image=addinfo ,bd=0,cursor="hand2",bg="black",relief="flat",activebackground="black", command=infoadi)
    Botonex.place(x=35,y=35, anchor="center")
    temp.append(Botonex)

#Para acceder al leadearboard
    def LeaderboardMenu():
        """*******************************************************
                   Instituto Tecnológico de Costa Rica
                       Ingenería en Computadores
           Lenguaje: Python 3.11
           Descripción: Es el menu de los mejores puntajes, dentro de esta se encuentra un maximo de 7 puntajes ordenados
           de mayor a menor
           Autor: Jian Yong Zheng Wu
           Fecha última modificación: Abril 22 de 2023
           ******************************************************"""
        global score, usernamelist,username
        global Fondo3
        global Titulo3
        labelDestroy(temp)  #Destruye los elementos del menu principal

        LeaderCanvas = tk.Canvas(Window, width=1280, height=720)
        LeaderCanvas.place(x=0, y=0)
        Fondo3 = tk.PhotoImage(file="BackgroundMenu/SPACEGRANDE_00.png")  # Fondo 2
        fnd3 = LeaderCanvas.create_image(0, 0, image=Fondo3, anchor="nw")
        Titulo3 = tk.PhotoImage(file="BackgroundMenu/LEADERBOARD.png")
        ttl3 = LeaderCanvas.create_image(650, 100, image=Titulo3, anchor="center")

        def juntarlista(usernamelist, scorelist, i=0):
            """*******************************************************
                       Instituto Tecnológico de Costa Rica
                           Ingenería en Computadores
               Lenguaje: Python 3.11
               Descripción: Junta la lista de los nombres y la lista de los puntos
               Autor: Jian Yong Zheng Wu y parte de Chat GPT
               Enlace: https://chat.openai.com
               Entrada: lista de nombres y lista de puntos
               Restricciones: []
               Salidas: Lista de nombres y lista de puntos
               Fecha última modificación: Abril 22 de 2023
               ******************************************************"""
            if i == lenn(usernamelist) or i == 7: #Maixmo 7
                # si hemos llegado al final de la lista de usernames o hemos alcanzado el límite máximo de 7 líderes, terminamos la recursión
                return "" #Retorna vacio
            else:
                max_score_index = find_max_score_index(scorelist, i) #Se llama a la función find_max_score_index() para
                # encontrar el índice del mayor puntaje en la lista de puntajes (scorelist) a partir de la posición i.
                swap(scorelist, i, max_score_index)  #Se llama a la función swap() para intercambiar el elemento en la posición i con el elemento
                # en la posición max_score_index de la lista de puntajes (scorelist).
                swap(usernamelist, i, max_score_index) # Se llama a la función swap() para intercambiar el elemento en la posición i con el elemento
                # en la posición max_score_index de la lista de nombres de usuario (usernamelist).
                leaderboard_entry = f"{usernamelist[i]}: {scorelist[i]}\n" #El f es para el tipo de formato y el /n es equivalente a darle un enter
                # concatenamos la cadena con el resultado de la recursión para el resto de la lista
                return leaderboard_entry + juntarlista(usernamelist, scorelist, i + 1) #Llamada recursiva

        def find_max_score_index(scorelist, start_index): #Se busca el índice del puntaje máximo a partir de un índice de inicio dado en una lista de puntajes.
            if start_index == lenn(scorelist) - 1: #Condicion base, si el índice de inicio es igual al índice del último elemento
                return start_index
            else:
                max_score_index = find_max_score_index(scorelist, start_index + 1) #se llama a la función recursivamente con el siguiente índice de inicio
                # (start_index + 1) y se guarda el índice del puntaje máximo en la variable max_score_index.
                return max_score_index if scorelist[max_score_index] >= scorelist[start_index] else start_index #la línea de código devuelve el índice que tiene
                # la puntuación máxima en la lista scorelist, considerando max_score_index como el índice inicial y start_index como una posible alternativa.

        def swap(lst, i, j): #Intercambia los elementos de i y j
            if i != j:
                lst[i], lst[j] = lst[j], lst[i]

        # crear la etiqueta de líder y establecer su texto
        TOP1 = tk.Label(Window, text="TOP 1= ", font=("Small Fonts", 20), fg="white",bg="black")
        TOP1.place(x=500, y=230)
        TOP2 = tk.Label(Window, text="TOP 2= ", font=("Small Fonts", 20), fg="white", bg="black")
        TOP2.place(x=500, y=260)
        TOP3 = tk.Label(Window, text="TOP 3= ", font=("Small Fonts", 20), fg="white", bg="black")
        TOP3.place(x=500, y=290)
        TOP4 = tk.Label(Window, text="TOP 4= ", font=("Small Fonts", 20), fg="white", bg="black")
        TOP4.place(x=500, y=320)
        TOP5 = tk.Label(Window, text="TOP 5= ", font=("Small Fonts", 20), fg="white", bg="black")
        TOP5.place(x=500, y=350)
        TOP6 = tk.Label(Window, text="TOP 6= ", font=("Small Fonts", 20), fg="white", bg="black")
        TOP6.place(x=500, y=380)
        TOP7 = tk.Label(Window, text="TOP 7= ", font=("Small Fonts", 20), fg="white", bg="black")
        TOP7.place(x=500, y=410)

        leader = tk.Label(Window, text=juntarlista(usernamelist, scorelist), font=("Small Fonts", 18), fg="white",bg="black")
        leader.place(x=600, y=232)

        def Return2():
            labelDestroy(temp)  #Destruye los elementos del menu leaderboard
            Menuprincipal()

        ReturnButton2 = tk.Button(Window, image=imgret,bd=0, cursor="hand2", bg="black", relief="flat",activebackground="black", command=Return2)
        ReturnButton2.place(x=80, y=40, anchor="center")
        temp.append(ReturnButton2)

    Boton2 = tk.Button(Window,image=imglidel,bd=0,cursor="hand2",bg="black",relief="flat",activebackground="black", command=LeaderboardMenu)
    Boton2.place(x=650, y=300, anchor="center")
    temp.append(Boton2)
#Para acceder al about
    def AboutMenu():
        """*******************************************************
                   Instituto Tecnológico de Costa Rica
                       Ingenería en Computadores
           Lenguaje: Python 3.11
           Descripción: El menu de informacion adicional sobre el juego y el creador
           Autor: Jian Yong Zheng Wu
           Fecha última modificación: Abril 22 de 2023
           ******************************************************"""
        global FondoAbout

        labelDestroy(temp) #Destruye los elementos del menu principal

        AboutCanvas = tk.Canvas(Window, width=1280, height=720)
        AboutCanvas.place(x=0, y=0)
        FondoAbout = tk.PhotoImage(file="BackgroundMenu/FONDOABOUT.png")  # Fondo 2
        fnd4 = AboutCanvas.create_image(0, 0, image=FondoAbout, anchor="nw")

        def Return3(): #Funcion para regresar al menu principal

            labelDestroy(temp)  #Destruye los elementos del menu about
            Menuprincipal()

        ReturnButton3 = tk.Button(Window, image=imgret, bd=0, cursor="hand2", bg="black", relief="flat",activebackground="black", command=Return3)
        ReturnButton3.place(x=80, y=40, anchor="center")
        temp.append(ReturnButton3)
    Boton3 = tk.Button(Window,image=imgabout, bd=0,cursor="hand2",bg="black",relief="flat",activebackground="black", command=AboutMenu)
    Boton3.place(x=650, y=400, anchor="center")
    temp.append(Boton3)

#Boton de salida
    def Exit():  # Funcion para cerrar el juego
        """*******************************************************
                   Instituto Tecnológico de Costa Rica
                       Ingenería en Computadores
           Lenguaje: Python 3.11
           Descripción: Funcion que cierra el juego
           Autor: Jian Yong Zheng Wu
           Fecha última modificación: Abril 22 de 2023
           ******************************************************"""
        Window.destroy()
    Boton4 = tk.Button(Window,image=imgexit,bd=0 ,cursor="hand2",bg="black",relief="flat",activebackground="black", command=Exit) #Boton para cerrar el juego
    Boton4.place(x=650, y=500, anchor="center")
    temp.append(Boton4)

    Window.mainloop()

Menuprincipal()

