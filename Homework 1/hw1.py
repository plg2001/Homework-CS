def num_of_blank_and_ap(msg):
    count = 0
    for x in msg:
        if x == " " or x == "'":
            count += 1
    return count    

def create_cipher_suite(frequences_in_msg,frequences_english): 
    cipher_suite = {}
    for key1 in frequences_in_msg:
        min_diff = float('inf')
        closest_key = None
        keys_checked = set()  # Per tenere traccia delle chiavi già verificate
        if key1 not in cipher_suite.keys():
            while True:
                min_diff = float('inf')  
                for key2 in frequences_english:
                    if key2 in keys_checked:  
                        continue
                    diff = abs(frequences_in_msg[key1] - frequences_english[key2])
                    if diff < min_diff:
                        min_diff = diff
                        closest_key = key2
                if closest_key not in cipher_suite.values():
                    cipher_suite[key1] = closest_key
                    break 
                else:
                    keys_checked.add(closest_key)   

    return cipher_suite 


with open('l.ct', 'r') as file:
    # Leggo tutto il contenuto del messaggio
    msg = file.read()


msg = msg.replace(" ", "")
msg = msg.replace("K", " ")

#Inizializzo 3 dizionari
frequences_english = {
    'E': 12.7,'T': 9.06,'A': 8.17,'O': 7.51,'I': 6.97,'N': 6.75,'S': 6.33,'H': 6.09,'R': 5.99,'D': 4.25,'L': 4.03,'C': 2.78,'U': 2.76,'M': 2.41,
    'W': 2.36,'F': 2.23,'G': 2.02,'Y': 1.97,'P': 1.93,'B': 1.49,'V': 0.98,'K': 0.77,'X': 0.15,'J': 0.1,'Q': 0.1,'Z': 0.05
}
frequences_in_msg = {}
cipher_suite = {}

for letter in msg:
    if letter not in frequences_in_msg and letter != "'" and letter != " ":
        frequences_in_msg[letter] = 0

#Conto le frequenze delle lettere
for letter in msg:
    if letter != "'" and letter != " ":
        frequences_in_msg[letter] += 1
        

#Porto in percentuale le frequenze
num_of_letter = len(msg) - num_of_blank_and_ap(msg)
for key in frequences_in_msg:
    frequences_in_msg[key] /= num_of_letter
    frequences_in_msg[key] *= 100
    frequences_in_msg[key] = round(frequences_in_msg[key],2) 

frequences_in_msg= dict(sorted(frequences_in_msg.items(), key=lambda item: item[1], reverse=True))


cipher_suite = create_cipher_suite(frequences_in_msg,frequences_english)


cipher_suite["R"] = "E"

#Perche per intuito dalla prima decrittografia spunta SOL'UE che mi fa pensare grazie anche all'apostrofo a YOU'RE 
cipher_suite["Y"] = "R" 
cipher_suite["M"] = "Y"
cipher_suite["I"] = "U" 

#Perche per intuito dalla prima decrittografia spunta RONNA DE che potrebbe essere GONNA BE
cipher_suite["J"] = "A"
cipher_suite["A"] = "G" 
cipher_suite["P"] = "B" 

#Perche dopo un ulteriore analisi dopo la precedenti sostituzioni é che nella prima frase abbiamo BUCCY YOU'RE A BOY GAE A BIG NOIME e NOIME, dopo un attenta analisi mi fa pensare a NOISE
cipher_suite["V"] = "S" 

#Perche SWREEW mi fa pensare a STREET
cipher_suite["T"] = "T" 

#Con la sostituzione precedente si arriva alla costruzione della frase IN THE STREET
cipher_suite["H"] = "H" 

#GONNA BE A BIG GAN mi fa pensare a "GONNA BE A BIG MAN"
cipher_suite["D"] = "M"  

#GONNA BE A BIG MAN SOME CAY mi fa pensare a "GONNA BE A BIG MAN SOME DAY"
cipher_suite["F"] = "D" 

#La frase You Got Mud on Yo' KAFE mi fa pensare (ovviamente anche traducendola) You got mud on yo FACE
cipher_suite["S"] = "F" 
cipher_suite["O"] = "C" 

#A questo punto si arriva alle soluzione finale perche si riconosce la canzone we will rock you
cipher_suite["N"] = "P"
cipher_suite["G"] = "L"

decrypted_msg = ''
for letter in msg:
    if letter in cipher_suite:
        decrypted_msg += cipher_suite[letter]
    else:
        decrypted_msg += letter
  
    


print(frequences_in_msg)
print("\n")
print(frequences_english)
print("\n")
print(cipher_suite)
print("\n")
print(msg)
print("\n")
print("\n")
print("\n")
print(decrypted_msg)
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")




        






