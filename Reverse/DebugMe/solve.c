#include <stdio.h>

int sub_E14(unsigned int a, unsigned int b) {
    signed int v2;
    unsigned int v3;
    int v4;
    int result;

    v2 = a ^ b;
    v3 = 1;
    v4 = 0;
    if ((b & 0x80000000) != 0)
        b = -b;
    if ((a & 0x80000000) != 0)
        a = -a;
    if (a >= b) {
        while (b < 0x10000000 && b < a) {
            b *= 16;
            v3 *= 16;
        }
        while (b < 0x80000000 && b < a) {
            b *= 2;
            v3 *= 2;
        }
        while (1) {
            if (a >= b) {
                a -= b;
                v4 |= v3;
            }
            if (a >= b >> 1) {
                a -= b >> 1;
                v4 |= v3 >> 1;
            }
            if (a >= b >> 2) {
                a -= b >> 2;
                v4 |= v3 >> 2;
            }
            if (a >= b >> 3) {
                a -= b >> 3;
                v4 |= v3 >> 3;
            }
            if (!a)
                break;
            v3 >>= 4;
            if (!v3)
                break;
            b >>= 4;
        }
    }
    result = v4;
    if (v2 < 0)
        result = -v4;
    return result;
}

const char table[] = "ie\x00ndags\x00r";

int main() {
    char flag[16] = {0};
    for (int i = 0, p = 0;; ++i, p = (7 * (p + 1)) - 11 * sub_E14(7 * (p + 1), 11)) {
        if (table[p]) {
            flag[i] = table[p];
        } else {
            break;
        }
    }

    printf("possible flag0: CTF{%s}\n", flag);

    printf("possible flag1: CTF{");
    for (int i = 0; flag[i]; ++i) {
        printf("%c", flag[i] ^ i);
    }
    printf("}\n");

    printf("possible flag2: CTF{");
    for (int i = 0; flag[i]; ++i) {
        printf("%c", flag[i] ^ 1);
    }
    printf("}\n");
    return 0;
}
