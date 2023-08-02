#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(void)
{
        int pid;

        printf("Parent pid is %d\n", getpid());
        printf("Parent about to fork a child\n");
        fflush(stdout);
        pid = fork();
        if (pid == 0) {
                printf("Child is running now with pid %d\n", getpid()); 
                fflush(stdout);
        } else {
                printf("Parent is running: child pid is %d\n", pid);
                fflush(stdout);
        }

        printf("Process with PID %d Exiting\n", getpid());
        // bad practice to not find out how child did -- more later

        fflush(stderr);
        fflush(stdout);
        return 0;
}
