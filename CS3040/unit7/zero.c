#include <stdio.h>

int main(int argc, char *argv[])
{
        unsigned int i;

        for (i=5; i >= 0; --i) {
                printf("5/%d = %d\n", i , 5/i);
        }

        return 0;
}
