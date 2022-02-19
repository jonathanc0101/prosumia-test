# NO  N  NE
#  O     E
# SO  S  SE


opuestos = {"NO": "SE", "N": "S", "NE": "SE", "O": "E"}
todosLosOpuestos = {"NO": "SE", "SE": "NO", "N": "S",
                    "S": "N", "NE": "SE", "SE": "NE", "O": "E", "E": "O"}


conjuntoTest = [("A", "S", "B"), ("B", "N", "A"), ("C", "S", "A")]


def main(conjunto=conjuntoTest):

    conjuntoProcesado = []

    simbolos = {}

    for regla in conjuntoTest:

        if regla[1] in opuestos:  # cambiamos por el opuesto e invertimos el orden
            conjuntoProcesado.append((regla[2], opuestos[regla[1]], regla[0]))
        else:
            conjuntoProcesado.append((regla[0], regla[1], regla[2]))

    # eliminamos los duplicados
    conjuntoProcesado = list(set(conjuntoProcesado))

    for regla in conjuntoProcesado:
        # colocamos las direcciones y simbolos a los que se refiere cada regla
        if regla[0] not in simbolos:
            simbolos[regla[0]] = [(regla[1], regla[2])]
        else:
            simbolos[regla[0]].append((regla[1], regla[2]))

        if regla[2] not in simbolos:
            simbolos[regla[2]] = [(todosLosOpuestos[regla[1]], regla[0])]
        else:
            simbolos[regla[0]].append((todosLosOpuestos[regla[1]], regla[0]))

    print("Conjunto: ", conjunto)
    print("Conjunto procesado: ", conjuntoProcesado)
    print("Diccionario de simbolos: ", simbolos)


if __name__ == "__main__":
    main()
