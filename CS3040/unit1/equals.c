// This is an example of something that doesn't work as expected
#include <stdio.h>

int main()
{
        int x = 42;
        int y = 43;

        if (x = y) {
                printf("x=%d, y=%d\n", x, y);
        }

        return(0);
}
