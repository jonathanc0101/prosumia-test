
opuestos = {"NO": "SE", "N": "S", "NE": "SO", "O": "E"}
todosLosOpuestos = {"NO": "SE", "SE": "NO", "N": "S",
                    "S": "N", "NE": "SO", "SO": "NE", "O": "E", "E": "O"}

conjuntoTest = [("A", "S", "B"), ("B", "N", "A"), ("C", "S", "A")]
# conjuntoTest = [("A", "S", "B"),
#                 ("C", "S", "A"),
#                 ("C", "NO", "A")]


def opuesto(regla):
    return((regla[2], todosLosOpuestos[regla[1]], regla[0]))


def comprobarDiccionarioDeSimbolos(simbolos):
    for simbolo in simbolos:
        diccAux = {}
        # comprobamos si hay mas de un mismo simbolo al que se va, con una direccion distinta (recordemos que no hay tuplas duplicadas)
        for tupla in simbolos[simbolo]:
            direccion = tupla[0]
            if direccion not in diccAux:
                diccAux[direccion] = True
            else:
                return False

            simboloTerminal = tupla[1]
            if simboloTerminal not in diccAux:
                diccAux[simboloTerminal] = True
            else:
                return False
    return True


def main(conjunto=conjuntoTest):

    conjuntoProcesado = []

    simbolos = {}

    for regla in conjuntoTest:

        if regla[1] in opuestos:  # cambiamos por el opuesto
            conjuntoProcesado.append(opuesto(regla))
        else:
            conjuntoProcesado.append(regla)

    # eliminamos los duplicados
    conjuntoProcesado = list(set(conjuntoProcesado))

    for regla in conjuntoProcesado:
        # colocamos las direcciones y simbolos a los que se refiere cada regla
        simboloInicial = regla[0]
        direccionOriginal = regla[1]
        simboloTerminal = regla[2]

        if simboloInicial not in simbolos:
            simbolos[simboloInicial] = [(direccionOriginal, simboloTerminal)]
        else:
            simbolos[simboloInicial].append(
                (direccionOriginal, simboloTerminal))

        if simboloTerminal not in simbolos:
            simbolos[simboloTerminal] = [
                (todosLosOpuestos[direccionOriginal], simboloInicial)]
        else:
            simbolos[simboloTerminal].append(
                (todosLosOpuestos[direccionOriginal], simboloInicial))

    print("Conjunto: ", conjunto)
    print("Conjunto procesado: ", conjuntoProcesado)
    print("Diccionario de simbolos: ", simbolos)

    conjuntoValido = comprobarDiccionarioDeSimbolos(simbolos)

    if conjuntoValido:
        print("El conjunto de reglas es valido")
    else:
        print("El conjunto de reglas no es valido")


if __name__ == "__main__":
    main()
