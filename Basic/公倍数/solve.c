#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[], char* envp[]) {
    unsigned long long result = 0;
    for (unsigned long long i = 0; i < 1000000000ull; ++i) 
        if (i % 3 == 0 || i % 5 == 0)
            result += i;
    printf("PCTF{%llu}\n", result);
    return 0;
}
