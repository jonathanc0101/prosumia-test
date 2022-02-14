

import argparse


def calcularAlturaMaxIzquierda(alturas):
    maxVal = alturas[0]

    maxAlturas = []

    for i in range(len(alturas)):
        maxAlturas.append(maxVal)
        if(maxVal < alturas[i]):
            maxVal = alturas[i]

    return maxAlturas


def calcularAlturaMaxDerecha(alturas):
    maxVal = alturas[len(alturas)-1]

    maxAlturas = []

    for i in range(len(alturas)-1, -1, -1):
        maxAlturas.insert(0, maxVal)
        if(maxVal < alturas[i]):
            maxVal = alturas[i]

    return maxAlturas


def main(alturas):

    maxAlturasIzquierda = calcularAlturaMaxIzquierda(alturas)

    maxAlturasDerecha = calcularAlturaMaxDerecha(alturas)

    minAlturas = [min(maxAlturasDerecha[i], maxAlturasIzquierda[i])
                  for i in range(len(alturas))]

    cantAgua = [minAlturas[i] - alturas[i] for i in range(len(alturas))]

    sumaAgua = sum(cant for cant in cantAgua if cant > 0)

    print("La cantidad de agua posible a acumular es {totalAgua} unidades".format(
        totalAgua=sumaAgua))


if __name__ == "__main__":
    # defined command line options
    # this also generates --help and error handling
    CLI = argparse.ArgumentParser()
    CLI.add_argument(
        "--alturas",  # name on the CLI
        nargs="*",  # 0 or more values expected => creates a list
        type=int,
        default=[5, 3, 1, 1, 3, 1],  # default if nothing is provided
    )

    # parse the command line
    args = CLI.parse_args()
    # access CLI options
    print("alturas: %r" % args.alturas)

    main(args.alturas)
    print("para probar distintas configuraciones de terreno usar el parametro --alturas seguido de las alturas separadas por espacios")
