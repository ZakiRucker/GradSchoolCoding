#include <stdio.h>

int main(void)
{
        int x;

        printf("x is located at address    '%u'\n", (unsigned int) &x);
        printf("main is located at address  '%u'\n", (unsigned int) &main);

        return 0;
}
