# Lista dei file da svuotare
files_to_empty = [
    "File/FileToDecrypt/FileEncrypted/1_KB.enc",
    "File/FileToDecrypt/FileEncrypted/10_KB.enc",
    "File/FileToDecrypt/FileEncrypted/1_MB.enc",
    "File/FileToDecrypt/FileDecrypted/1_KB.txt",
    "File/FileToDecrypt/FileDecrypted/10_KB.txt",
    "File/FileToDecrypt/FileDecrypted/1_MB.bin",
    "File/key.bin",
    "File/iv.bin"
]

# Svuota il contenuto di ogni file
for file_path in files_to_empty:
    with open(file_path, 'w') as file:
        pass  # Non scriviamo nulla, quindi il file rimane vuoto

print("Contenuto dei file svuotato con successo.")
