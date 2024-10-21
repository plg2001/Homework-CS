import matplotlib.pyplot as plt
import numpy as np

# Dimensioni dei file (in KB) per le quali misuriamo il tempo
file_sizes = np.array([1, 10, 1024])  # 1 KB, 10 KB, 1 MB

# Simulazione dei tempi di cifratura (in millisecondi)
aes_encrypt_times = [0.067, 0.098, 6.06]  # Tempi simulati per AES
camellia_encrypt_times = [0.13, 0.1180, 7.83]  # Tempi simulati per CAMELLIA
aria_encrypt_times = [0.091, 0.125, 9.68]  # Tempi simulati per ARIA

# Simulazione dei tempi di decifratura (in millisecondi)
aes_decrypt_times = [0.07, 0.105, 6.532]  # Tempi simulati per AES
camellia_decrypt_times = [0.111, 0.144, 7.06]  # Tempi simulati per CAMELLIA
aria_decrypt_times = [0.079, 0.14, 10.47]  # Tempi simulati per ARIA

plt.figure(figsize=(10, 5))
plt.plot(file_sizes, aes_encrypt_times, label="AES", marker='o')
plt.plot(file_sizes, camellia_encrypt_times, label="CAMELLIA", marker='o')
plt.plot(file_sizes, aria_encrypt_times, label="ARIA", marker='o')
plt.title("Tempi di cifratura per file delle diverse dimensioni")
plt.xlabel("Dimensione del file (KB)")
plt.ylabel("Tempo di cifratura (ms)")  # Modificato in millisecondi
plt.xscale('log')  # Imposta l'asse X su scala logaritmica
plt.xticks(file_sizes, labels=["1 KB", "10 KB", "1 MB"])
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()

# Creazione del grafico per la decifratura
plt.figure(figsize=(10, 5))
plt.plot(file_sizes, aes_decrypt_times, label="AES", marker='o')
plt.plot(file_sizes, camellia_decrypt_times, label="CAMELLIA", marker='o')
plt.plot(file_sizes, aria_decrypt_times, label="ARIA", marker='o')
plt.title("Tempi di decifratura per file delle diverse dimensioni")
plt.xlabel("Dimensione del file (KB)")
plt.ylabel("Tempo di decifratura (ms)")  # Modificato in millisecondi
plt.xscale('log')  # Imposta l'asse X su scala logaritmica
plt.xticks(file_sizes, labels=["1 KB", "10 KB", "1 MB"])
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()
