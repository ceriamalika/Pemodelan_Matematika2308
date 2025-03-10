# -*- coding: utf-8 -*-
"""Kesetimbangan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aPW4imWVRb_kU4DrhBBhnMo7uwpduxjQ
"""

import numpy as np #numpy packages untuk keperluan saintis. Np sebagai panggilan dari numpy
import matplotlib.pyplot as plt

#Rentang nilai x dan waktu untuk medan vektor (parameter)
x = np.arange(0, 3, 0.1)
t = np.arange (0, 4, 0.1)
T, X = np.meshgrid(t, x) #meshgrid adalah bingkai yang berarti dari gari X dan T

# Definisikan sistem
dX = -X**2 + 3 * X - 2
dT = np.ones(dX.shape)  #np.ones artinya dijadikan satu baris

# Plot stream plot
plt.figure(figsize=(10, 6))
plt.streamplot(T, X, dT, dX, color=dX, cmap='coolwarm', linewidth=1) #Perintah untuk memunculkan salah satu fungsi di matplotlib

plt.title("Stream Plot of the System")
plt.xlabel("Time (t)")
plt.ylabel("x")
plt.axhline(0, color='gray', linestyle='--')
plt.colorbar(label='dx/dt')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Parameter konstanta
k = 0.1 # Konstanta pendinginan
Ta = 25 # Suhu lingkungan

#Definisi sistem persamaan diferensial
def system(T):  #def adalah definisi
  return -k * (T - Ta)

# Membuat grid untuk visualisasi
t_vals = np.linspace(0, 50, 20) # Rentang waktu
T_vals = np.linspace(0, 50, 20) # Rentang suhu
t, T = np.meshgrid(t_vals, T_vals) # Perbaikan urutan meshgrid

# Menghitung vektor arah
U = np.ones_like(T) # Arah horizontal tetap untuk menunjukkan perubahan dalam waktu
V = system(T) # Arah vertikal mengikuti sistem persamaan diferensial

# Plot medan vektor menggunakan streamplot
plt.figure(figsize=(7, 5))
plt.streamplot(t, T, U, V, color='blue')
plt.axhline(Ta, color='red', linestyle='--', label='Solusi Setimbang (T = Ta)')
plt.xlabel('t(waktu)')
plt.ylabel('T(suhu)')
plt.title("Medan Vektor untuk Persamaan Diferensial Pendinginan Newton")
plt.legend()
plt.grid()
plt.show()