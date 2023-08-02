#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int main(int argc, char *argv[])
{
        int *px = NULL;

        px = malloc(4200000000);
        if ((px==NULL) || (errno != 0)) {
                perror("malloc failed");
                printf("file %s, line %d\n", __FILE__, __LINE__);
        }

        return 0;
}
