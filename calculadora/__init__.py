def GenerarEstructura(estadisticas_jugador):
    names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA,
    CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia,
    Francsica', FEDERICO, Fernanda, GONZALO, Nancy """
    goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0,
    11]
    goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2,
    3, 0, 0]
    assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1,
    0]
    name_list= [name.strip() for name in names.split(',')]
    for i in range (len(name_list)):
        jugador_actual= {
            'nombre': name_list[i],
            'goles': goals[i],
            'goles_avoided': goals_avoided[i],
            'asistencias': assists[i]
        }
        estadisticas_jugador.append(jugador_actual)
    return(estadisticas_jugador)

def CalcularGoleador(listaJugadores):
    mayor_goleador = max(listaJugadores, key=lambda x: x['goles'])
    print(f"El mayor goleador es {mayor_goleador['nombre']} con {mayor_goleador['goles']} goles.")
    
def JugadorMasInfluyente(listaJugadores):
    goat=""
    max=0
    for player in listaJugadores:
        nombre= player['nombre']
        asistencias=player['asistencias']
        goles=player['goles']
        goles_evitados=player['goles_avoided']
        goles=goles*1.5
        goles_evitados=goles_evitados*1.25
        total=goles+goles_evitados+asistencias
        if total>max:
            max=total
            goat=nombre
    print("El jugador mas influyente es: ",goat)

def PromedioGolesEquipoGeneral(listaJugadores):
    total_goles=0
    for player in listaJugadores:
        goles=player['goles']
        total_goles=total_goles+goles
    promedio=total_goles/25
    print("Promedio de goles por partido del equipo en general: ",promedio)

def PromedioGolesGoleador(listaJugadores):
    mayor_goleador = max(listaJugadores, key=lambda x: x['goles'])
    promedio=mayor_goleador['goles']/25
    print(f"El mayor goleador es {mayor_goleador['nombre']} con promedio de",promedio," goles.")