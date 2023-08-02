#include <stdio.h>

int main(int argc, char *argv[])
{
        int f[8] = {10, 20, 30, 40, 50, 60, 70, 80};
        int *p = &(f[0]);
        int q = *p++;

        printf("(%d,%d,%d)\n", f[0], *p, q);

        return 0;
}
