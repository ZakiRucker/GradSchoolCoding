#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
        int fd;
        char buf[65];
        int out = 1;
        int i;

        errno = 0;
        fd = open("/etc/passwd", O_RDONLY);
        if (errno) {
                perror("Error: tried to open /etc/passwd with R/O access");
        } else {
                for (i=0; i<10; ++i) {
                        lseek(fd, 0, SEEK_SET);
                        out = read(fd, buf, 64);
                        if (out > 0) {
                                buf[out] = '\0';
                                printf("%s\n", buf);
                        }
                }
                errno = 0;
                close(fd);
                perror("close fd");
                close(fd);
                perror("close fd again");
        }

        return 0;
}
