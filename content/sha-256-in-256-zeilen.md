Title: SHA-256 in 256 Zeilen
Date: 2014-04-23 20:27
Author: surt91
Category: Code
Tags: C, Python
Slug: sha-256-in-256-zeilen
Status: published

Programmiersprachen muss man üben, um sie zu lernen und um sie nicht
wieder zu verlernen. Ich habe also meine Zeit damit vertrieben einen
[SHA-256](http://de.wikipedia.org/wiki/Sha256) zu schreiben -- eine
[kryptographische
Hash](http://de.wikipedia.org/wiki/Kryptologische_Hashfunktion)
Funktion. Die [Spezifikation](http://tools.ietf.org/html/rfc6234) ist
Glücklicherweise sehr sehr verständlich.  
Und auch wenn es tausende andere Implementationen gibt, die schneller
sind, alle Grenzfälle beachten (ich befürchte, dass mein Programm
Probleme auf Big Endian Systemen bekommt), und sogar Schaltkreise, die
hochoptimiert nur diese Operation beherrschen (vgl. Bitcoin ASIC), ist
meiner dennoch sehenswert, da er SHA-256 in 256 Zeilen darstellt.

    #!C
    // sha256: https://tools.ietf.org/html/rfc6234
    #include <stdint.h>
    #include <string.h>
    #include <stdio.h>
    #include <stdlib.h>

    // Format string for output
    #define FORMAT_SHA256 "%08x%08x%08x%08x%08x%08x%08x%08x"

    // First 32 Bits of the fractional part of the cuberoots of the first 64 primes
    static const uint32_t K[64] =
    {
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
        0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
        0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
        0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
        0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
        0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    };

    // First 32 Bits of the fractional part of the squareroots of the first 8 primes
    static const uint32_t H0[8] =
    {
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    };

    // Helper Functions
    inline static const uint32_t SHR(const uint32_t x, const int n)
    {
        return x>>n;
    }

    inline static const uint32_t ROTR(const uint32_t x, const int n)
    {
        return ((x >> n) | (x << (32-n)));
    }

    inline static const uint32_t CH(const uint32_t x, const uint32_t y, const uint32_t z)
    {
        return (x & y) ^ ( (~x) & z);
    }

    inline static const uint32_t MAJ(const uint32_t x, const uint32_t y, const uint32_t z)
    {
        return (x & y) ^ (x & z) ^ (y & z);
    }

    inline static const uint32_t BSIG0(const uint32_t x)
    {
        return ROTR(x, 2) ^ ROTR(x, 13) ^ ROTR(x, 22);
    }

    inline static const uint32_t BSIG1(const uint32_t x)
    {
        return ROTR(x, 6) ^ ROTR(x, 11) ^ ROTR(x, 25);
    }

    inline static const uint32_t SSIG0(const uint32_t x)
    {
        return ROTR(x, 7) ^ ROTR(x, 18) ^ SHR(x, 3);
    }

    inline static const uint32_t SSIG1(const uint32_t x)
    {
        return ROTR(x, 17) ^ ROTR(x, 19) ^ SHR(x, 10);
    }

    static void hash_block(const uint32_t *block, uint32_t *H)
    {
        int j;
        uint32_t W[64];
        uint32_t a[8];
        uint32_t T1, T2;

        for(j=0; j<16; j++)
            W[j] = block[j];
        for(j=16; j<64; j++)
            W[j] = SSIG1(W[j-2]) + W[j-7] + SSIG0(W[j-15]) + W[j-16];

        for(j=0; j<8; j++)
            a[j] = H[j];

        for(j=0; j<64; j++)
        {
            T1 = a[7] + BSIG1(a[4]) + CH(a[4], a[5], a[6]) + K[j] + W[j];
            T2 = BSIG0(a[0]) + MAJ(a[0], a[1], a[2]);
            a[7] = a[6];
            a[6] = a[5];
            a[5] = a[4];
            a[4] = a[3] + T1;
            a[3] = a[2];
            a[2] = a[1];
            a[1] = a[0];
            a[0] = T1 + T2;
        }

        for(j=0; j<8; j++)
            H[j] += a[j];
    }

    inline static uint32_t make_word32(const char *input, const size_t len)
    {
        uint32_t output = 0;
        switch(len)
        {
            // the remainder of plaintext is equal or longer than one block
            default:
            case 4:
                output |= (input[3] & 0xff) << (8*0);
            case 3:
                output |= (input[2] & 0xff) << (8*1);
            case 2:
                output |= (input[1] & 0xff) << (8*2);
            case 1:
                output |= (input[0] & 0xff) << (8*3);
            case 0:
                ;
        }
        return output;
    }

    inline static void partition_block(const char *plaintext, const size_t len, uint32_t *block)
    {
        int j;

        memset(block, 0, 64);
        for(j=0; j<16; j++)
            block[j] = make_word32(plaintext + j*4, (len > j*4) ? (len - j*4) : 0);
    }

    inline static void add_one_at_end(const size_t len, uint32_t *block)
    {
        block[(len%64)/4] |= 0x1 << (31-(len*8)%32);
    }

    inline static void append_length_at_end(const size_t total_length, uint32_t *block)
    {    // append length in Bit
        block[14] = (total_length*8) & 0xffffffff00000000;
        block[15] = (total_length*8) & 0x00000000ffffffff;
    }

    inline static void padd_block(const size_t total_length, uint32_t *block)
    {
        add_one_at_end(total_length, block);
        append_length_at_end(total_length, block);
    }

    // note: len is the length in Byte!
    static void hash_stream_mode(const char *plaintext, const size_t len,
                                 const size_t total_length, uint32_t *H, const int last_batch)
    {
        int i;
        uint32_t block[16];
        uint64_t N = len / 64;
        int L = len % 64;

        if(last_batch)
            N++;

        for(i=0; i<N; i++)
        {
            partition_block(plaintext + i*64, len - i*64, block);
            if(last_batch && (i == N-1))
            {
                if(L + 1 > 56)
                {
                    add_one_at_end(total_length, block);
                    hash_block(block, H);

                    memset(block, 0, 64);
                    append_length_at_end(total_length, block);
                }
                else
                {
                    padd_block(total_length, block);
                }
            }
            hash_block(block, H);
        }
    }

    // Hash Routine
    void sha256(const char *plaintext, char *out)
    {
        uint32_t H[8];
        memcpy(H, H0, 8 * sizeof(uint32_t));

        hash_stream_mode(plaintext, strlen(plaintext), strlen(plaintext), H, 1);

        sprintf(out, FORMAT_SHA256, H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]);
    }

    void sha256_file(const char *in_file, char* out)
    {
        FILE *file_in;
        char *buffer;
        size_t fileLen;
        const size_t block_size = 16 * 64 * 1024; // 1MB Blocks
        size_t buffer_block_size = block_size;
        int i, last = 0;
        uint32_t H[8];
        memcpy(H, H0, 8 * sizeof(uint32_t));

        // open input file
        file_in = fopen(in_file, "rb");
        if (!file_in)
        {
            fprintf(stderr, "Unable to open file %s", in_file);
            return;
        }

        // get file length
        fseek(file_in, 0, SEEK_END);
        fileLen=ftell(file_in);
        fseek(file_in, 0, SEEK_SET);

        // allocate memory
        buffer = (char *)calloc(buffer_block_size, sizeof(char));
        if (!buffer)
        {
            fprintf(stderr, "Memory error!");
            fclose(file_in);
            return;
        }

        // hash block for block
        for(i=0; i<fileLen; i+=buffer_block_size)
        {
            if(fileLen - i < buffer_block_size)
            {
                buffer_block_size = fileLen-i;
                last = 1;
            }
            // read file contents into buffer
            fread(buffer, buffer_block_size, 1, file_in);

            // call sha256 function on the buffer
            hash_stream_mode(buffer, buffer_block_size, fileLen, H, last);
        }

        fclose(file_in);
        free(buffer);

        sprintf(out, FORMAT_SHA256, H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]);
    }

Natürlich fehlt die `main()` Funktion, was daran liegt,
dass es als Bibliothek entworfen ist.  
In Python ist es übrigens etwas kürzer ;)  

    #!Python3
    print(hashlib.sha256(b"Hallo Welt!").hexdigest())

