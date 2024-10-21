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


#define CAMELLIA_BLOCK_SIZE 16
#define KEY_SIZE 16
#define BUFFER_SIZE 4096




void handleErrors(const char *errorMessage) {
    perror(errorMessage);
    exit(EXIT_FAILURE);
}



int decrypt(FILE *in, FILE *out, unsigned char *key, unsigned char *iv) {
   
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    if (!ctx) handleErrors("Errore nella crazione del contesto");

    // Inizializza il contesto per la decifratura con CAMELLIA-128-CBC
    if (EVP_DecryptInit_ex(ctx, EVP_camellia_128_cbc(), NULL, key, iv) != 1) {
        handleErrors("Errore nella inizializzazione del contesto");
    }

    unsigned char buffer[BUFFER_SIZE];
    unsigned char decrypted_buffer[BUFFER_SIZE + CAMELLIA_BLOCK_SIZE];
    int len;
    int decrypted_len;

    // Legge il file cifrato e decifralo
    while ((len = fread(buffer, 1, BUFFER_SIZE, in)) > 0) {
        if (EVP_DecryptUpdate(ctx, decrypted_buffer, &decrypted_len, buffer, len) != 1) {
            handleErrors("Errore nela decifratura");
        }
        fwrite(decrypted_buffer, 1, decrypted_len, out);
    }

    // Finalizza la decifratura
    if (EVP_DecryptFinal_ex(ctx, decrypted_buffer, &decrypted_len) != 1) {
        handleErrors("Errore nella finalizzazione della decifratura");
    }
    fwrite(decrypted_buffer, 1, decrypted_len, out);

    EVP_CIPHER_CTX_free(ctx);
    return 1;
}



int main(){
    FILE *KB_1_enc  = fopen("../File/FileToDecrypt/FileEncrypted/1_KB.enc","rb");
    FILE *KB_10_enc = fopen("../File/FileToDecrypt/FileEncrypted/10_KB.enc","rb");
    FILE *MB_1_enc  = fopen("../File/FileToDecrypt/FileEncrypted/1_MB.enc","rb");

    FILE *KB_1  = fopen("../File/FileToDecrypt/FileDecrypted/1_KB.txt","w");
    FILE *KB_10 = fopen("../File/FileToDecrypt/FileDecrypted/10_KB.txt","w");
    FILE *MB_1  = fopen("../File/FileToDecrypt/FileDecrypted/1_MB.bin","w");

    FILE *keyfile = fopen("../File/key.bin","rb");
    FILE *ivfile =  fopen("../File/iv.bin","rb");

    if (keyfile  == NULL || ivfile == NULL ) {
        handleErrors("Errore apertura file");
    }

    if (KB_1 == NULL || KB_10 == NULL || MB_1 == NULL || 
        KB_1_enc == NULL || KB_10_enc == NULL || MB_1_enc == NULL) {
        handleErrors("Errore apertura file");
    }


    unsigned char KEY[KEY_SIZE];
    unsigned char IV[CAMELLIA_BLOCK_SIZE];

    size_t key_bytes_read = fread(KEY, sizeof(unsigned char), KEY_SIZE, keyfile);
    if (key_bytes_read != KEY_SIZE) { handleErrors("Errore nella lettura di KEY, controlla se generata");   }


    size_t iv_bytes_read = fread(IV,  sizeof(unsigned char), KEY_SIZE, ivfile);
    if (iv_bytes_read != CAMELLIA_BLOCK_SIZE) {handleErrors("Errore nella lettura di IV, controlla se generato");}


    double vector_time[3];

    clock_t start = clock();
    decrypt(KB_1_enc,KB_1,KEY,IV);
    clock_t end = clock();

    double time_spent = (double)(end - start) * 1000 / CLOCKS_PER_SEC;
    vector_time[0] = time_spent;

    start = clock();
    decrypt(KB_10_enc,KB_10,KEY,IV);                    
    end = clock();

    time_spent = (double)(end - start) * 1000 / CLOCKS_PER_SEC;
    vector_time[1] = time_spent;



    start = clock();
    decrypt(MB_1_enc,MB_1,KEY,IV);
    end = clock();

    time_spent = (double)(end - start) * 1000/ CLOCKS_PER_SEC;
    vector_time[2] = time_spent;
   

    for (int i = 0; i < 3; i++)
    {
       printf("Tempo di esecuzione file %d: %f secondi\n", i+1,vector_time[i]);
    }
    
    
    


}