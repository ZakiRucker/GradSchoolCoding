#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

#define INPUT_FILE "/etc/passwd"
#define BUFSIZE 128

int main(int argc, char *argv[])
{
        char buf[BUFSIZE];
        FILE *fd = NULL;

        errno = 0;
        fd = fopen(INPUT_FILE, "r");

        // ???

        // clean up
        if (fd != NULL) {
                fclose(fd);
                fd = NULL;
        }
        return 0;
}
