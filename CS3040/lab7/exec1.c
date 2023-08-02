#include <stdio.h>
#include <errno.h>
#include <sys/types.h>
#include <unistd.h>

int main(void)
{
        int pid;
        int result;

        pid = fork();
        if (pid == 0) {
                printf("\nChild is running now with pid %d\n", getpid()); 
                printf("Child is about to exec 'ls -l'\n");
                fflush(stdout);
                errno = 0;
                result = execlp("ls", "ls", "-l", NULL);
                if (result != 0) {
                        perror("exec failed");
                }
                printf("If you got here, things didn't go well\n");
        }

        // bad practice to not find out how child did -- more later

        fflush(stderr);
        fflush(stdout);
        return 0;
}
