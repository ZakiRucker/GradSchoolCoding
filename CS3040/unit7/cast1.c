#include <stdio.h>

int main(int argc, char *argv[])
{
        unsigned int bigger = 1;
        signed int   smaller = -1;

        printf("bigger = %u\n", bigger);
        printf("smaller = %d\n\n", smaller);

        // Unexpected behavior:
        if (smaller < bigger) {
                printf("%d < %u\n", smaller, bigger);
        } else {
                printf("%d > %u\n", smaller, bigger);
        }

        return 0;
}
