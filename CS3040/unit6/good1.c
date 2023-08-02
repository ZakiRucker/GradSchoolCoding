#include <stdio.h>

int main(void)
{
        int x[3] = {42, 86, 99};

        int *y = x;

        *(y + 1) = 100;   // The left resolves to a location

        for (int i=0; i<3; ++i) {
                printf("x[%d] = %d\n", i, x[i]);
        }

        return 0;
}
