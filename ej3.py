# posibles direcciones
# NO  N  NE
#  O     E
# SO  S  SE

# una regla tiene el siguiente formato
# simbolo direccion simbolo

# el objetivo de este programa es determinar si un conjunto de reglas, digase por
# ej: (A,S,B) (A,N,C), (C,SO,B) es posible
# un caso donde un conjunto de reglas es imposible, es cuando dos reglas distintas
# contienen al mismo conjunto de simbolos, en la misma orientacion, ej:
#  (A,S,B) (A,N,B) es imposible, pero (A,N,B) , (B,S,A) es posible
