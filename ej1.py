# fuente de la resolucion de este ejercicio
# https://www.translatorscafe.com/unit-converter/da-DK/calculator/two-points-distance/#:~:text=The%20Chebyshev%20distance%20is%20also,aligned%20to%20the%20edges%20of


def calcularDistanciaEntreDosPuntos(posicionInicial=None, posicionSiguiente=None):
    if(posicionInicial is None or posicionSiguiente is None):
        print("falta posicion inicial o posicion siguiente!")
        return

    distancia = max([posicionSiguiente[0]-posicionInicial[0],
                    posicionSiguiente[1]-posicionInicial[1]])

    return distancia


def main(arrayRecibido=[(0, 0), (1, 2), (1, 3)]):

    # la posicion inicial es la primera
    maximoIndice = len(arrayRecibido)-1

    distanciaTotal = sum([calcularDistanciaEntreDosPuntos(
        arrayRecibido[x], arrayRecibido[x+1]) for x in range(maximoIndice)])

    print("La distancia total desde el punto {p1} hasta el punto {pn} pasando por {puntos} es {dist}".format(
        dist=distanciaTotal, p1=arrayRecibido[0], pn=arrayRecibido[maximoIndice], puntos=arrayRecibido[1:maximoIndice]))


if __name__ == "__main__":
    print(
        "Se debe cambiar el array de tuplas recibido como argumento dentro de la funcion main, no encontré manera mas simple. Por defecto se llama con la lista [(0, 0), (1, 2), (1, 3)]")
    main()
