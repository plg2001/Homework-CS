#include <openssl/evp.h>
#include <openssl/ssl.h>
#include <openssl/rsa.h>
#include <openssl/x509.h>
#include <openssl/aes.h>
#include <openssl/rand.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>


#define AES_BLOCK_SIZE 16
#define KEY_SIZE 16
#define BUFFER_SIZE 4096




void handleErrors(const char *errorMessage) {
    perror(errorMessage);
    exit(EXIT_FAILURE);
}



int encrypt(FILE *in, FILE *out, unsigned char *key, unsigned char *iv) {
    
    // Inizializza il contesto per la cifratura con AES-128-CBC
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    if (!ctx) handleErrors("Errore nella crazione del contesto");

   
    if (EVP_EncryptInit_ex(ctx, EVP_aes_128_cbc(), NULL, key, iv) != 1) {
        handleErrors("Errore nella inizializzazzione del contesto");
    }

    unsigned char buffer[BUFFER_SIZE];
    unsigned char cipher_buffer[BUFFER_SIZE + AES_BLOCK_SIZE];
    int len;
    int cipher_len;

    // Legge il file di input e cifralo
    while ((len = fread(buffer, 1, BUFFER_SIZE, in)) > 0) {
        if (EVP_EncryptUpdate(ctx, cipher_buffer, &cipher_len, buffer, len) != 1) {
            handleErrors("Errore nella cifratura");
        }
        fwrite(cipher_buffer, 1, cipher_len, out);
    }

    // Finalizza la cifratura
    if (EVP_EncryptFinal_ex(ctx, cipher_buffer, &cipher_len) != 1) {
        handleErrors("Errore nella finalizzazione della cifratura");
    }
    fwrite(cipher_buffer, 1, cipher_len, out);

    EVP_CIPHER_CTX_free(ctx);
    return 1;
}


int main(){
    FILE *KB_1 = fopen("../File/FileToEncrypt/1_KB.txt","r");
    FILE *KB_10 = fopen("../File/FileToEncrypt/10_KB.txt","r");
    FILE *MB_1 = fopen("../File/FileToEncrypt/1_MB.bin","r");

    FILE *KB_1_enc = fopen("../File/FileToDecrypt/FileEncrypted/1_KB.enc","w");
    FILE *KB_10_enc = fopen("../File/FileToDecrypt/FileEncrypted/10_KB.enc","w");
    FILE *MB_1_enc = fopen("../File/FileToDecrypt/FileEncrypted/1_MB.enc","w");

    FILE *keyfile = fopen("../File/key.bin","wb");
    FILE *ivfile =  fopen("../File/iv.bin","wb");

    if (keyfile  == NULL || ivfile == NULL ) {
        handleErrors("Errore apertura file");
    }


    if (KB_1 == NULL || KB_10 == NULL || MB_1 == NULL || 
        KB_1_enc == NULL || KB_10_enc == NULL || MB_1_enc == NULL) {
        handleErrors("Errore apertura file");
    }


    unsigned char KEY[KEY_SIZE];
    unsigned char IV[AES_BLOCK_SIZE];


    if (RAND_bytes(IV, sizeof(IV)) == -1) { handleErrors("Errore nella generazione di IV"); }

    if (RAND_bytes(KEY, sizeof(KEY)) == -1) { handleErrors("Errore nella generazione di IV"); }


   
    size_t bytes_written = fwrite(KEY, sizeof(unsigned char), KEY_SIZE, keyfile);
    if (bytes_written != 16) {
        handleErrors("Errore nella scrittura del file");
    }

    bytes_written = fwrite(IV, sizeof(unsigned char), KEY_SIZE, ivfile);
    if (bytes_written != 16) {
        handleErrors("Errore nella scrittura del file");
    }




    encrypt(KB_1, KB_1_enc,KEY,IV);
    encrypt(KB_10, KB_10_enc,KEY,IV);
    encrypt(MB_1, MB_1_enc,KEY,IV);
    

  



}