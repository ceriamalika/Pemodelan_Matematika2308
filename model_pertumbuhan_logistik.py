# -*- coding: utf-8 -*-
"""Model_Pertumbuhan_Logistik

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J0-K-w6wuQj5lPk22PpGMCrT-PUwpCAL
"""

#import pustaka yang diperlukan
import numpy as np  #numpy adalah packages
import matplotlib.pyplot as plt  #. panggil struktur fungsi didalam packages

def Pertumbuhan_Logistik(K, P0, t, r):
  """
  Menyelesaikan P(t) = K / (1 + ((K - P0) / P0) * e^(-r * t))

  Parameter:
    t  : array-like, waktu
    K : float, kapasitas lingkungan
    P0 : float, penduduk awal
    r  : float, konstanta laju pertumbuhan

  Mengembalikan:
  P : array-like, populasi
  """
  return K / (1 + ((K - P0) / P0) * np.exp(-r * t))

#Parameter contoh
K = 100
P0 = 20
r  = 0.2
t  = np.linspace(0, 50, 100)

#Menyelesaikan persamaan
P = Pertumbuhan_Logistik(K, P0, t, r)

#Plot hasilnya
plt.figure(figsize=(8,5))
plt.plot(t, P, label=f"T(t) = {K} / (1 ((K - P0) / P0) * exp(-{r} * t))", color="green")
plt.title("Model Pertumbuhan Logistik")
plt.xlabel("Waktu (t)")
plt.ylabel("Populasi (P)")
plt.legend()
plt.grid()
plt.show()