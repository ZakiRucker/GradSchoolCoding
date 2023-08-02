#include <stdio.h>

int main(int argc, char *argv[])
{
#ifdef DEBUG
        printf("argc=%d\n", argc);
#endif
        for (unsigned int i=0; i<argc; ++i) {
                printf("argv[%d] = %s\n", i, argv[i]);
        }

        return 0;
}
