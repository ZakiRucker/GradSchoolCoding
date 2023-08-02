#include <stdio.h>


void func1(void)
{
        int x = 99;

        printf("func1 x = %d\n", x);
}



int main(void)
{
        int x = 42;

        func1();
        printf("main x = %d\n", x);

        return 0;
}
