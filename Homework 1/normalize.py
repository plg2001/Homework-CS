frequences_english = {
    'E': 12.7,'T': 9.06,'A': 8.17,'O': 7.51,'I': 6.97,'N': 6.75,'S': 6.33,'H': 6.09,'R': 5.99,'D': 4.25,'L': 4.03,'C': 2.78,'U': 2.76,'M': 2.41,
    'W': 2.36,'F': 2.23,'G': 2.02,'Y': 1.97,'P': 1.93,'B': 1.49,'V': 0.98,'K': 0.77,'X': 0.15,'J': 0.1,'Q': 0.1,'Z': 0.05
}
frequences_in_msg = {}

total_cipher_frequency = sum(frequences_in_msg.values())
total_english_frequency = sum(frequences_english.values())


# Normalizzazione delle frequenze del messaggio cifrato
for char in frequences_in_msg:
    frequences_in_msg[char] = round((frequences_in_msg[char] / total_english_frequency) * 100,2)
# Normalizzazione delle frequenze della lingua inglese
for char in frequences_english:
    frequences_english[char] = round((frequences_english[char] / total_english_frequency) * 100,2)