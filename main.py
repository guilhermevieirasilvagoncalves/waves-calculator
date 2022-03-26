import numpy as np

variable = {
  1: ["f", "Hz"],
  2: ["l", "m/s"],
  3: ["k", "rad/m"],
  4: ["w", "rad/s"],
  5: ["Em", "V/m"],
  6: ["Bm", "T"]
}

# variaveis
f = 0.0 # Frequencia
T = 0.0 # Período
l = 0.0 # Comprimento
k = 0.0 # Número de ondas
w = 0.0 # Frequencia angular
Em = 0.0 # Campo Elétrico
Bm = 0.0 # Campo Magnégtico
pi = np.pi # Pi
c = 3 * pow(10,8) # Velocidade da Luz

# c = m/s
# w = rad/s
# l = m/s
# k = rad/m
# f = Hz
# Em = V/m
# Bm = T

# caso entre o valor de w
# f = 2.pi / w
# k = w / c
# l = c / f

# caso entre o valor de f
# l = c / f
# w = 2.pi.f
# k = w / c

# caso entre o valor de l
# f = c / l
# k = 2.pi / l
# w = 2.pi.f

#caso entre o valor de k 
# l = 2.pi / k
# w = k . c
# f = w / 2.pi

# caso entre o valor de bm
# em = c . bm

#casp entre o valor de em
# bm = em / c
while True:
  print(
  """
  Digite a opção de entrada:
  [1] - Frequência (f)
  [2] - Comprimento de Onda (l)
  [3] - Número de Ondas (k)
  [4] - Frequência Angular (w)
  [5] - Campo Elétrico (Em)
  [6] - Campo Magnéico (Bm)
  [7] - Parar o programa (X)
  """)
  N = int(input("Digite: "))
  if N >= 1 and N <= 4:
    D = float(input("Digite o valor para %s na unidade %s: "%(variable[N][0], variable[N][1])))
    if N == 1:
      f = D
      l = c / f
      w = 2 * pi * f
      k = w / c
    if N == 2:
      l = D
      f = c / l
      k = (2 * pi) / l
      w = 2 * pi * f
    if N == 3:
      k = D
      l = (2 * pi) / k
      w = k * c
      f = w / (2 * pi)
    if N == 4:
      w = D
      f = w / (2 * pi)
      k = w / c
      l = c / f
      
    print(
      """
      [f] Frequência = {0} Hz
      [l] Comprimento de Onda = {1} m
      [k] Número de Ondas = {2}
      [w] Frequência Angular = {3}
      """.format(np.format_float_scientific(f, precision = 2, exp_digits = 1), np.format_float_scientific(l, precision = 2, exp_digits = 1), np.format_float_scientific(k, precision = 2,exp_digits = 1), np.format_float_scientific(w, precision = 2, exp_digits = 1)))
  if N == 5 or N == 6:
    D = float(input("Digite o valor para %s na unidade %s: "%(variable[N][0], variable[N][1])))
    if N == 5:
      Em = D
      Bm = Em/c
    if N == 6:
      Bm = D
      Em = c * Bm
    print(
      """
      [Em] Campo Elétrico = {0}
      [Bm] Campo Magnético = {1}
      """.format(np.format_float_scientific(Em, precision = 2, exp_digits = 1),np.format_float_scientific(Bm, precision = 2, exp_digits = 1)))
  if N == 7:
    break
  if N > 7 or N < 0:
    print("O valor digitado não corresponde as opções disponíveis, por favor selecione outra opção.")
