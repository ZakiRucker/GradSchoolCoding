#include <stdio.h>

int main(int argc, char *argv[])
{
        unsigned int  x = 7040;
        unsigned char y;

        y = x;
        printf("x is %u, y is %d\n", x, (int) y);

        return 0;
}
