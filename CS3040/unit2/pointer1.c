#include <stdio.h>

int main()
{
        int x = 3;
        int y = 5;
        int z;
        int *px;
        int *py;

        px = &x;
        py = &y;

        z = *px * *py;                       // counting on precedence
        printf("%d x %d = %d\n", x, y, z);

        z = (*px) * (*py);                   // explicit order
        printf("%d x %d = %d\n", x, y, z);

        return 0;
}

