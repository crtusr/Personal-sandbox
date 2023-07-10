import random
from midiutil.MidiFile import MIDIFile

def generar_intervalo(intervalo_anterior, intervalo_suma):
    grado_conjunto = [-2,-1, 1, 2]
    grado_conjunto_asc = [1, 2]
    grado_conjunto_desc = [-2,-1]
    salto = [-12, -8, -7, -5, -4, -3, 3, 4, 5, 7, 8, 12]
    salto_asc = [3, 4, 5, 7, 8, 12]
    salto_desc = [-12, -8, -7, -5, -4, -3]
    octava_asc = [12]
    octava_desc = [-12]
    
    # Regla 1: Si el intervalo anterior pertenece a grado conjunto y tiene signo opuesto.
    if intervalo_anterior in grado_conjunto and intervalo_anterior * intervalo_suma < 0:
        intervalos_posibles = grado_conjunto + salto
    # Regla 2: Si el intervalo anterior es mayor.
    elif intervalo_anterior > intervalo_suma:
        intervalos_posibles = grado_conjunto + salto
    # Regla 3: Si la suma entre el intervalo anterior y el nuevo intervalo esta dentro de los intervalos posibles
    elif (intervalo_anterior + intervalo_suma) in grado_conjunto + salto:
        intervalos_posibles = grado_conjunto + salto
    # Regla 4: Si es octava, que vaya para el otro lado
    elif intervalo_anterior in octava_asc:
        intervalos_posibles = grado_conjunto_desc
    elif intervalo_anterior in octava_desc:
        intervalos_posibles = grado_conjunto_asc
    else:
        intervalos_posibles = grado_conjunto

    return random.choice(intervalos_posibles)

def generar_notas_con_intervalos(num_notas, duracion_min, duracion_max):
    notas = []
    escala_do_mayor = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83]

    # Generar la primera nota
    pitch = random.choice(escala_do_mayor)
    duracion = random.randint(duracion_min, duracion_max)
    notas.append((pitch, duracion))
    intervalo_anterior = 0
    intervalo_suma = 0

    # Generar las siguientes notas
    for _ in range(1, num_notas):
        intervalo_suma += intervalo_anterior
        intervalo = generar_intervalo(intervalo_anterior, intervalo_suma)
        pitch = notas[-1][0] + intervalo
        # Asegurar que la nota esté en la escala de Do Mayor
        while pitch not in escala_do_mayor:
            intervalo = generar_intervalo(intervalo_anterior, intervalo_suma)
            pitch = notas[-1][0] + intervalo
        print(f'Intervalo generado: {intervalo}')  # Imprime el intervalo en la consola
        duracion = random.randint(duracion_min, duracion_max)
        notas.append((pitch, duracion))
        intervalo_anterior = intervalo

    return notas


    return notas


# Crear el objeto MIDI
mf = MIDIFile(1)     # solo 1 pista
track = 0   # la única pista

time = 0    # empezar al principio
mf.addTrackName(track, time, "Pista de muestra")
mf.addTempo(track, time, 120)

# Generar notas aleatorias
notas = generar_notas_con_intervalos(10, 1, 4)

# Agregar las notas al archivo MIDI
channel = 0
volume = 100
time = 0
for pitch, duracion in notas:
    mf.addNote(track, channel, pitch, time, duracion, volume)
    time += duracion  # avanzar el tiempo

# Escribirlo en el disco
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)
