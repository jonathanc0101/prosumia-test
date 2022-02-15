# posibles direcciones
# NO  N  NE
#  O     E
# SO  S  SE

# una regla tiene el siguiente formato
# simbolo direccion simbolo

# el objetivo de este programa es determinar si un conjunto de reglas, digase por
# ej: (A,S,B) (A,N,C), (C,SO,B) es posible

# un caso donde un conjunto de reglas es imposible, es cuando dos reglas distintas
# contienen al mismo conjunto de simbolos, en el mismo orden, pero una direccion no opuesta, ej:
#  (A,S,B) (A,N,B) es imposible, pero (A,N,B) , (B,S,A) es posible
# a partir de esto tenemos en cuenta las direcciones y sus opuestos:
# direccion: opuesto:
# N          S
# E          O
# SE         NO
# SO         NE

# cada simbolo tiene 8 posibles direcciones, pensemoslo asi:
#  NO  N    NE
#  O   Sim  E
#  SO  S    SE
#   Ninguna de las direcciones puede estar ocupada por el mismo simbolo

# podríamos ir formando algo asi como un grafo de todos los simbolos
#  NO  N    NE NO  N    NE NO  N    NE NO  N    NE NO  N    NE
#  O   Sim0  E O   Sim1  E O   Sim2  E O   Sim3  E O   Sim4  E ...
#  SO  S    SE SO  S    SE SO  S    SE SO  S    SE SO  S    SE
#  NO  N    NE NO  N    NE NO  N    NE NO  N    NE NO  N    NE
#  O   Sim5  E O   Sim6  E O   Sim7  E O   Sim8  E O   Sim9  E ...
#  SO  S    SE SO  S    SE SO  S    SE SO  S    SE SO  S    SE

# un ejemplo de esto sería:
# se lee la primera regla (A,S,B) del conjunto de reglas [(A,S,B),(B,N,A),(C,S,A)]

#  NO  N    NE
#  O   B    E
#  SO  S    SE
#  NO  N    NE
#  O   A    E
#  SO  S    SE

#   dado que (A,S,B) implica (B,N,A) se lee recien la tercera regla:

#  NO  N    NE
#  O   B    E
#  SO  S    SE
#  NO  N    NE
#  O   A    E
#  SO  S    SE
#  NO  N    NE
#  O   C    E
#  SO  S    SE

# El conjunto de reglas termina siendo valido, ahora si le añadimos la regla (D,N,C) vemos que el conjunto no es valido, ya que el lugar al norte de C está ocupado por A

# Si pensamos el problema en terminos de un plano XY, donde el simbolo inicial se coloca en el punto (0,0), el norte es (0,1), sur es (0,-1), este es (1,0), oeste es ...

# constantes
norte = [0, 1]
sur = [0, -1]
este = [1, 0]
oeste = [-1, 0]

norOeste = [-1, 1]
norEste = [1, 1]
surOeste = [-1, -1]
surEste = [1, -1]

posInicial = [0, 0]

conjuntoTest = [("A", "S", "B"), ("B", "N", "A"), ("C", "S", "A")]


def main(conjunto=conjuntoTest):

    return


if __name__ == "__main__":
    main()
