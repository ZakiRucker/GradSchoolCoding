#include <stdio.h>

int main()
{
        char ch   = 'Z';
        char *p1  = &ch;
        char **p2 = &p1;

        printf("ch = %c\n", ch);
        printf("ch = %c\n", *p1);
        printf("ch = %c\n", **p2);

        return 0;
}

