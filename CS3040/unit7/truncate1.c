#include <stdio.h>

int main(int argc, char *argv[])
{
        int x = 10;
        short y = (short) x;
        
        printf("----------------------------\n");
        printf("sizeof short = %d\n", sizeof(short));
        printf("sizeof int   = %d\n", sizeof(int));

        printf("----------------------------\n");
        printf("x and y should both be %d\n", x);
        printf("x=%d, y=%d\n", x, y);

        int i = 70000;
        short j = (short) i;
        printf("----------------------------\n");
        printf("i and j should both be %d\n", i);
        printf("i=%d, j=%d\n", i, j);

        return 0;
}
