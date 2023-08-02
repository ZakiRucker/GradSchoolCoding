#include <stdio.h>
#include <errno.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
        char *ptr = NULL;

        errno = 0;
        ptr = malloc(4000000000);
        if ((ptr==NULL) || (errno != 0)) {
                perror("malloc error");
        } else {
                printf("malloc() worked\n");
                free(ptr);
                ptr = NULL;
        }

        return 0;
}
