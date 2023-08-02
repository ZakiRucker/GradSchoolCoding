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
                printf("Child is about to exec 'ls'\n");
                fflush(stdout);
                errno = 0;
                result = execlp("ls", "ls", NULL);
                if (result != 0) {
                        perror("exec failed");
                }
                printf("If you got here, things didn't go well\n");
        } else {
                // parent will pause so zombie state of child can be seen
                printf("Press CR to continue\n");
                fflush(stdout);
                getc(stdin);
        }

        // bad practice to not find out how child did -- more later

        fflush(stderr);
        fflush(stdout);
        return 0;
}
