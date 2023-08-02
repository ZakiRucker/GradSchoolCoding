#include <stdio.h>

int main(int argc, char *argv[])
{
        char ch[4] = {0, 0, 0, 'z'};
        char *pch = ch;
        unsigned int  x;

        x = *((unsigned int *)pch);

        printf("x = %u\n", x);

        return 0;
}
