#include <stdio.h>

int main(void) 
{
        int *foo1[10];
        int **foo2[10];
        int (*foo3)[];
        int *(*foo4)[4][5]; // won't compile w/o array sizes. Odd.

        printf("sizeof(foo) when 'int *foo[10]'    = %d\n", sizeof(foo1));
        printf("sizeof(foo) when 'int **foo[10]'   = %d\n", sizeof(foo2));
        printf("sizeof(foo) when 'int (*foo)[]'    = %d\n", sizeof(foo3));
        printf("sizeof(foo) when 'int *(*foo)[][]' = %d\n", sizeof(foo4));

        return 0;
}
