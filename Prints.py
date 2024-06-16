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
print(labelDestroy.__doc__)

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

print(cargarimgs.__doc__)

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

print(cargarSprites.__doc__)

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
print(Menuprincipal.__doc__)


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
print(LoginMenu.__doc__)


def add_username():
    """*******************************************************
               Instituto Tecnológico de Costa Rica
                   Ingenería en Computadores
       Lenguaje: Python 3.11
       Descripción: Es la funcion que guarda los nombres ingresados en el tk.Entry, los almacena en una lista
       llamada usernamelist.
       Fecha última modificación: Abril 22 de 2023
       ******************************************************"""
print(add_username.__doc__)


def validation():  # Validacion para escribir el nombre
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
print(validation.__doc__)


def easymodescreen():
    """*******************************************************
               Instituto Tecnológico de Costa Rica
                   Ingenería en Computadores
       Lenguaje: Python 3.11
       Descripción: Dificultad facil
       Autor: Jian Yong Zheng Wu
       Fecha última modificación: Abril 22 de 2023
       ******************************************************"""

print(easymodescreen.__doc__)


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

print(Movingbackground.__doc__)


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

print(edgereacheda.__doc__)


def gameover():
    """*******************************************************
            Instituto Tecnológico de Costa Rica
                Ingenería en Computadores
    Lenguaje: Python 3.8.10
    Descripción: Función que desplega la pantalla de GameOver
    Autor: Jian Yong Zheng Wu
    Fecha última modificación: Abril 22 de 2023
    ******************************************************"""
print(gameover.__doc__)


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
print(colisionnave.__doc__)


def colisionlasers(laser):
    """*******************************************************
           Instituto Tecnológico de Costa Rica
               Ingenería en Computadores
   Lenguaje: Python 3.11
   Descripción: Función que detecta la colision entre los lasers del jugador y del enemigo
   Autor: Jian Yong Zheng Wu
   Fecha última modificación: Abril 22 de 2023
   ******************************************************"""
print(colisionlasers.__doc__)


def lasernpc1():
    """*******************************************************
           Instituto Tecnológico de Costa Rica
               Ingenería en Computadores
   Lenguaje: Python 3.11
   Descripción: Función que hace que dispare el primer enemigo
   Autor: Jian Yong Zheng Wu
   Fecha última modificación: Abril 22 de 2023
   ******************************************************"""
print(lasernpc1.__doc__)


def lasernpc2():
    """*******************************************************
           Instituto Tecnológico de Costa Rica
               Ingenería en Computadores
   Lenguaje: Python 3.11
   Descripción: Función que hace que dispare el segundo enemigo
   Autor: Jian Yong Zheng Wu
   Fecha última modificación: Abril 22 de 2023
   ******************************************************"""
print(lasernpc2.__doc__)


def lasernpc3():
    """*******************************************************
           Instituto Tecnológico de Costa Rica
               Ingenería en Computadores
   Lenguaje: Python 3.11
   Descripción: Función que hace que dispare el tercer enemigo
   Autor: Jian Yong Zheng Wu
   Fecha última modificación: Abril 22 de 2023
   ******************************************************"""
print(lasernpc3.__doc__)


def NPCMove():
    """*******************************************************
           Instituto Tecnológico de Costa Rica
               Ingenería en Computadores
   Lenguaje: Python 3.11
   Descripción: Función que hace que se muevan los enemigos
   Autor: Jian Yong Zheng Wu
   Fecha última modificación: Abril 22 de 2023
   ******************************************************"""
print(NPCMove.__doc__)


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
print(shoot.__doc__)


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
print(mover_laser.__doc__)


def up(event):  # Mover arriba
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
print(up.__doc__)


def down(event):  # Mover abajo
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
print(down.__doc__)


def left(event):  # Mover izquierda
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
print(left.__doc__)


def right(event):  # Mover derecha
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
print(right.__doc__)


def RocaMove():
    """*******************************************************
           Instituto Tecnológico de Costa Rica
               Ingenería en Computadores
   Lenguaje: Python 3.11
   Descripción: Función que hace que se mueva la piedra
   Autor: Jian Yong Zheng Wu
   Fecha última modificación: Abril 22 de 2023
   ******************************************************"""
print(RocaMove.__doc__)


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
print(LeaderboardMenu.__doc__)


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
print(juntarlista.__doc__)


def AboutMenu():
    """*******************************************************
               Instituto Tecnológico de Costa Rica
                   Ingenería en Computadores
       Lenguaje: Python 3.11
       Descripción: El menu de informacion adicional sobre el juego y el creador
       Autor: Jian Yong Zheng Wu
       Fecha última modificación: Abril 22 de 2023
       ******************************************************"""
print(AboutMenu.__doc__)

def Exit():  # Funcion para cerrar el juego
    """*******************************************************
               Instituto Tecnológico de Costa Rica
                   Ingenería en Computadores
       Lenguaje: Python 3.11
       Descripción: Funcion que cierra el juego
       Autor: Jian Yong Zheng Wu
       Fecha última modificación: Abril 22 de 2023
       ******************************************************"""
print(Exit.__doc__)