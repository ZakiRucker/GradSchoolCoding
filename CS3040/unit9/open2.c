#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
        int fd = -1;

        // Try to open password file with R/W access
        printf("---------------------------------------------------\n");
        errno = 0;
        fd = open("/etc/passwd", O_RDWR | O_APPEND);
        if (errno) {
                perror("Error: tried to open /etc/passwd with R/W access");
        } else {
                printf("Success: opened /etc/passwd with R/W access.\n");
                close(fd);
        }

        printf("---------------------------------------------------\n");
        return 0;
}
