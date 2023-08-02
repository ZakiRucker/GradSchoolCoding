#include <stdio.h>

int main(int argc, char *argv[])
{
        unsigned int x = 1000;
        unsigned int z;
        int y = -2;

        printf("x=%u\n", x);
        printf("y=%d\n", y);

        // Unexpected behavior:
        z = x / y;
        printf("x / y = %u\n", z);
        printf("y interpreted as unsigned = %u\n", (unsigned int) y);

        return 0;
}
