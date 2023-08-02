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
#define MAX_CHARS 80
#define TIMER 3000

int main (void)
{
        char *token = NULL;
        char *arg[MAX_CHARS];
        char arguments[MAX_CHARS + 1];
        char cmd[MAX_CHARS];
        int pid;  
        int i = 0;
        int result = 0;        

        // get user input
        alarm(TIMER);
        printf("prompt>");
        fgets(arguments, MAX_CHARS, stdin);
        
        token = strtok(arguments," \n");
        
        while (token != NULL) {
                if (strcmp(token, "exit") == 0) {
                        break;
                }
                if (strcmp(token, "explode") == 0) {
                        int *bomb = NULL;
                        *bomb = 42;
                }
                for (i =0; i <= MAX_COMMANDS; i++) {
                        arg[i] = strtok(token, " \n");
                }
                if (arg[i] != NULL) {
                        strcpy(cmd, arg[i]);
                }
         
                pid = fork();
                if (pid == 0) {
                        errno = 0;
                        result = execvp(cmd, arg);
                                if (result != 0) {
                                perror("exec failed");
                                }
                        printf("If you got here, things didn't go well\n");
                } else {
                        //printf("Parent is running: child pid is %d\n", pid);
//                        pid = waitpid(pid, &result, 0);
//                        if (WIFEXITED(status)) {
//                                WEXITSTATUS(result);
//                        }
                }
        }
        //printf("Process with PID %d Exiting\n", getpid());
        
        fflush(stderr);
        fflush(stdout);
        return 0;
}
