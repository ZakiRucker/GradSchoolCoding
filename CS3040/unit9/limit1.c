#include <sys/time.h>
#include <sys/resource.h>
#include <stdio.h>
#include <errno.h>

int main(int argc, char *argv[])
{
        struct rlimit resource;

        errno = 0;
        getrlimit(RLIMIT_NOFILE, &resource);
        if (errno) {
                perror("Error: unable to get file limits");
        } else {
                printf("Hard limit = %u\n", (unsigned)resource.rlim_max);
                printf("Soft limit = %u\n", (unsigned)resource.rlim_cur);
        }

        return 0;
}
