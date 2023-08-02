#include <stdio.h>

void inc(int *number);


int main(void)
{
        int x = 42;
        printf("The number after %d is ", x);

        inc(&x);
        printf("%d\n", x);

        return 0;
}


void inc(int *number)
{
        *number = *number + 1;
}
