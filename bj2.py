from random import *
def generarMazo():
    #return sample([(x,y) for x in ['A','K'] for y in ['P','T','D','C']],8)
    #return sample([(x,y) for x in ['A','A','A','A','A','A','A','A','A','A','J','Q','K'] for y in ['P','T','D','C']],52)
    return sample([(x,y) for x in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'] for y in ['P','T','D','C']],52)
def cantidadAs(mano):
    if mano==[]:
       return 0
    return valorCarta(mano[0], True)+cantidadAs(mano[1:]) #Como va contar los ases, se envia true
def valorCarta(carta, As11): #Si As = verdadero, cuenta la cantidad de ases; As = Falso cuenta las cartas con As valiendo 1
    if(str(carta[0]) in "JQK")and (not As11):
       return 10
    if(carta[0]=='A'):
        return 1
    elif(As11): #Como esta contando ases, las otras cartas retornan 0
        return 0
    return int(carta[0])
def valorMano(cantidadAs, mano, resultado): #Verifica el valor de la mano y tiene en cuenta los Ases
    if mano==[]:
        if(cantidadAs==0):
            return resultado
        else:
            if(resultado+10<=21-(cantidadAs-1)): #Verifica si se pueden sumar ases con valor 11 dependiendo del puntuja
                return valorMano(cantidadAs-1, mano,resultado+10) #Como ya se sumaron los ases con valor 1, solo se suma 10 si es necesario
            else:
                return resultado
    if(valorCarta(mano[0],False)==1):
        return valorMano(cantidadAs, mano[1:], resultado+1) #Añade As=1
    else:
        return valorMano(cantidadAs, mano[1:], resultado+valorCarta(mano[0],False)) #Añade puntaje de la carta (no es as)
        
def jugar(mazo, casa, jugador, continuaJugador):
    if mazo!=[]:
        if(casa==[] and jugador==[]): #Inicia mazo
            return jugar(mazo[4:], casa+mazo[:2], jugador+mazo[2:4],True)
        if(valorMano(cantidadAs(casa),casa,0)<=21 and valorMano(cantidadAs(jugador),jugador,0)<=21): #Dependiendo del puntaje continua el juego
            return continuacion(mazo, casa, jugador, continuaJugador)
        else:
            imprimirCartas(casa,jugador,continuaJugador,True)
            return imprimirResultado(valorMano(cantidadAs(casa),casa,0), valorMano(cantidadAs(jugador),jugador,0)) #Si alguno de los dos paso los 21 termina el juego
def continuacion(mazo, casa, jugador, continuaJugador):
    imprimirCartas(casa,jugador,continuaJugador,False)
    if(confirmar(continuaJugador)): #Si el jugador dice que ya no quiere jugar, solo juega la casa
        if(jugarCasa(casa)):
            if(valorMano(cantidadAs(jugador+[mazo[0]]),jugador+[mazo[0]],0)<21):
                return jugar(mazo[2:], casa+[mazo[1]], jugador+[mazo[0]],continuaJugador)
            else:
                return jugar(mazo[1:], casa, jugador+[mazo[0]],continuaJugador)
                imprimirCartas(casa,jugador,continuaJugador,True)
                return imprimirResultado(valorMano(cantidadAs(casa),casa,0), valorMano(cantidadAs(jugador),jugador,0)) #Si se pasa el jugador finaliza
        else:
            return jugar(mazo[1:], casa, jugador+[mazo[0]],continuaJugador)
    else:
        if(jugarCasa(casa) and valorMano(cantidadAs(jugador),jugador,0)<=21):
            return jugar(mazo[1:], casa+[mazo[0]], jugador, False)
        else:
            imprimirCartas(casa,jugador,continuaJugador,True)
            return imprimirResultado(valorMano(cantidadAs(casa),casa,0), valorMano(cantidadAs(jugador),jugador,0)) #Si ninguno de los dos continua, termina el juego
def confirmar(continuarJugador): #Confirma si quiere mas cartas, sino solo juega la casa
    if(continuarJugador):
       if(input("\nJugador, quiere mas cartas? (Escriba 'N' para finalizar): ")!="N"):
            return True
    return False
def jugarCasa(casa): #Dependiendo del puntaje de la casa, decide si pide mas cartas o no
    if(valorMano(cantidadAs(casa),casa,0)<21):
        return True
    else:
        return False

def imprimirResultado(casa,jugador): #RESULTADOS: Analiza el puntaje de cada jugador e imprime el resultado
    if(casa==jugador)or((casa<=21)and((casa>jugador)and(jugador<=21)))or((casa<=21)and(jugador>=21)):
       return "Gano la casa"
    else:
        if(casa>21 and jugador>21):
            return "Nadie gano"
        return "Gano el jugador"

def imprimirCartas(casa,jugador,continuaJugador,finalizo): #Impresiones por pantalla
    if(finalizo):
        print("*** Termino el juego *")
        print("Cartas casa: ",casa)
        print("Puntaje casa: ",valorMano(cantidadAs(casa),casa,False))
    else:
        print("Cartas casa: [('X', 'X')] ",casa[1:])
    if(continuaJugador)or(finalizo):
        print("Cartas jugador: ",jugador)
        print("Puntaje jugador: ",valorMano(cantidadAs(jugador),jugador,False))
        
print(jugar(generarMazo(),[],[],True))
