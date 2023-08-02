#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void)
{
        int pid;
        int status;

        pid = fork();
        if (pid == 0) {
                // the child -- about to list the directory
                errno = 0;
                printf("In child, about to exec\n");
                status = execlp("ls", "ls", "-l", NULL);
                perror("exec failed");
                printf("If you got here, things didn't go well\n");
                exit(-1);
        }  else {
                // the parent -- wait for child to finish
                pid = waitpid(pid, &status, 0);
                if (WIFEXITED(status)) {
                        printf("Parent: the child has terminated. "
                               "Result was %d\n",
                               WEXITSTATUS(status));
                }
        }

        fflush(stdout);
        fflush(stderr);
        return 0;
}
