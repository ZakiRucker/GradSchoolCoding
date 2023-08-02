#include <stdio.h>
#include <limits.h>

int main(int argc, char *argv[])
{
        unsigned int i = 70000;
        unsigned short j;

        if (i > USHRT_MAX) {
                printf("Averted truncation error\n");
        } else {
                j = (short) i;
                printf("i and j should both be %d\n", i);
                printf("i=%d, j=%d\n", i, j);
        }

        return 0;
}
