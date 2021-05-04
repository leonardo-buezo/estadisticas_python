from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show


""" Nuestro helper para graficas """
def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos x', y_axis_label='pasos y')
    grafica.line(x, y)
    show(grafica)


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenadas(borracho)
    for _ in range(pasos):
        campo.mover_borracho(borracho)
    return inicio.distancia(campo.obtener_coordenadas(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0, 0)
    distancias = []
    x_ilum = []
    y_ilum = []
    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))
        a = campo.coordenadas_de_borrachos[borracho].x
        b = campo.coordenadas_de_borrachos[borracho].y
        x_ilum.append(a)
        y_ilum.append(b)
    return (x_ilum, y_ilum)

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []
    for pasos in distancias_de_caminata:
        coord_x, coord_y = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        """distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos}')
        print(f'Media = {distancia_media}')
        print(f'Maxima = {distancia_maxima}')
        print(f'Minima = {distancia_minima}')"""
    graficar(coord_x, coord_y)


if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100
    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)
