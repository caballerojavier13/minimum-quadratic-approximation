import numpy as np
from MathParser import PyMathParser

# ----- Inicializamos el analizador de funciones -----
mathparser = PyMathParser()
mathparser.addDefaultFunctions()
mathparser.addDefaultVariables()
# ----------------------------------------------------

# ----------------- Datos de entrada -----------------
x = [1.00, 1.20, 1.40, 1.60, 1.80]
y = [0.242, 0.1942, 0.1497, 0.1109, 0.079]
# ----------------------------------------------------


# -- Completamos la tabla para las funciones básicas -
f1_expression = 'ln(x)'
f1 = []

mathparser.expression = f1_expression
for v in x:
    mathparser.variables['x'] = v
    f1.append(mathparser.evaluate())

f2_expression = 'pow(e, (x * -1))'
f2 = []

mathparser.expression = f2_expression
for v in x:
    mathparser.variables['x'] = v
    f2.append(mathparser.evaluate())
# ----------------------------------------------------


# --------- Presentamos los Datos de entrada ---------
print()
print('================================')
print('Presentamos los Datos de entrada')
print('================================')
print()
print("x = %s" % x)
print("y = %s" % y)
print("f1 [%s] = %s" % (f1_expression, f1))
print("f2 [%s] = %s" % (f2_expression, f2))
print('')
print('--------------------------------')
print('')
# ----------------------------------------------------


# Resolvemos juntos alguno producto escalares:

n = len(x)
f1_f1 = 0
f1_f2 = 0
f2_f1 = 0
f2_f2 = 0

f_f1 = 0
f_f2 = 0

for k in range(0, n):  # Sumatoria
    f1_f1 += f1[k] * f1[k]
    f1_f2 += f1[k] * f2[k]
    f2_f1 += f2[k] * f1[k]
    f2_f2 += f2[k] * f2[k]

    f_f1 += y[k] * f1[k]
    f_f2 += y[k] * f2[k]

A = np.array([
    [f1_f1, f2_f1],
    [f1_f2, f2_f2]
])

print(A)

"""
[[0.7128513  0.32993982]
 [0.32993982 0.3549492 ]]
"""

B = np.array([
    [f_f1],
    [f_f2]
])

print(B)

"""
[[0.18433529]
 [0.21988323]]
"""

A_inv = np.linalg.inv(A)  # Obtenemos la inversa de la matriz A = A-1

C = A_inv.dot(B)  # Producto punto entre las dos matrices

print('-----------------')
print(C)
"""
[[-0.04937769]
 [ 0.66537662]]
"""
print('-----------------')
print()
print('==============================')
print('Calculamos el error del método')
print('==============================')
print()

c0 = C[0][0]
c1 = C[1][0]

delta = 0

for k in range(0, n):  # Sumatoria
    delta += (y[k])**2 - ((c0 * y[k] * f1[k]) + (c1 * y[k] * f2[k]))


e = np.sqrt(abs(delta))

print("El error del método es de: %s" % str(e))
# El error del método es de: 0.0049424443349604325
