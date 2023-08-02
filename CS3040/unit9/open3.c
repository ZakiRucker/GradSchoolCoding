#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>

#define MYFILE "/etc/passwd"

int main(int argc, char *argv[])
{
        int fd = -1;

        printf("Will try to open '%s' read-only\n", MYFILE);
        fd = open(MYFILE, O_RDONLY);
        if (errno) {
                perror("Unexpected error opening file");
                exit(-1);
        }
        
        printf("Success: descriptor = %d\n", fd);
        close(fd);

        return 0;
}
