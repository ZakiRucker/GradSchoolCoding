#include <stdio.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
        int fd = 0;
        int num =0;
        unsigned int test = 411111111;

        errno = 0;
        fd = open("test.txt", O_WRONLY | O_CREAT, 0600);
        if ((fd > 0) && (errno == 0)) {
                num = write(fd, (char *) &test, sizeof(test));
                if (num <= 0) {
                        perror("Write failure");
                }
                close(fd);
        } else {
                perror("File open error");
        }

        return 0;
}
