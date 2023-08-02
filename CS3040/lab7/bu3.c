//---------------------------------------------------------------------
//File: shell.c
//
//Description:  shell.c opens a shell 
//
//Syntax:       
//
//Created:      17 November 2017
//              Rucker, Zaki
//---------------------------------------------------------------------

#include <stdio.h>
#include <string.h> // fgets
#include <sys/types.h> // pid
#include <unistd.h> // fork,pid, execvp
#include <errno.h>

#define MAX_COMMANDS 10
#define MAX_ARGS 80

int main (void)
{
        char *token = NULL;
        char arguments[MAX_ARGS + 1];
        int pid;  
        int result;        

        // get user input
        printf("prompt=>");

        fgets(arguments, MAX_ARGS, stdin);
        token = strtok(arguments," \n");
        
        


        while (token != NULL) {
                printf("%s\n", token);
                token = strtok(NULL," \n");
        }

        //printf("Parent pid is %d\n", getpid());
        //printf("Parent about to fork a child\n");
        //fflush(stdout);
        
        pid = fork();
        if (pid == 0) {
                printf("\nChild is running now with pid %d\n", getpid());
                printf("Child is about to exec 'ls -l'\n");
                fflush(stdout);
                errno = 0;
                result = execvp("ls","ls", "-l", "-a", NULL);
                if (result != 0) {
                        perror("exec failed");
                }
                printf("If you got here, things didn't go well\n");
        } else {
                printf("Parent is running: child pid is %d\n", pid);
                fflush(stdout);
        }

        printf("Process with PID %d Exiting\n", getpid());
        
        // verify the input
                // fork / exec
        
                // error check fork & exit
                // error check exec, if child fails kill it or weird things will happen
                // explode
                // exit

        // create an history file (cat arguments into the file)
        //printf(token);
        //printf("input = %s\n", arguments);
        
        // create sigalrm with alarm
        // close the file when sigalrm is received

        fflush(stderr);
        fflush(stdout);
        return 0;
}
