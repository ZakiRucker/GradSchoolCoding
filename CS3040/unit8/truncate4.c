#include <stdio.h>
#include <limits.h>
#include <math.h>

int main(int argc, char *argv[])
{
        float f1 = 3.14159;
        float rf1 = roundf(f1);
        if (rf1 <= UINT_MAX) {
                int x1 = (int) rf1;
                printf("f1=%f, x1=%d\n", f1, x1);
        } else {
                printf("float can't fit into int\n");
        }

        float f2 = 9.9;
        float rf2 = roundf(f2);
        if (rf2 <= UINT_MAX) {
                int x2 = (int) rf2;
                printf("f2=%f, x2=%d\n", f2, x2);
        } else {
                printf("float can't fit into int\n");
        }

        return 0;
}
