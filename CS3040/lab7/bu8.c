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
#include <stdlib.h> //exit
#include <string.h> // fgets
#include <sys/types.h> // pid
#include <unistd.h> // fork,pid, execvp
#include <errno.h>
#include <sys/wait.h>

#define HIST_PATH 
#define MAX_COMMANDS 10
#define MAX_CHARS 80
#define TIMER 3000

FILE *History = NULL;
const char *Hist = "shell-history.txt";

void clean (void);

void clean (void) 
{
        if (History != NULL) {
                if ((fclose(History)) != 0) {
                        perror ("Unable to close History");
                        exit(-1);
                }
                History = NULL;
        }
}

int main (void)
{
        char *token = NULL;
        char *arg[MAX_CHARS];
        char arguments[MAX_COMMANDS + 1];
        char cmd[1];
        int pid;  
        int i = 0;
        int result = 0;
        unsigned int length = 0;        
        
        atexit(clean);

        alarm(TIMER);
        
        printf("prompt>");
        
        // get user input
        fgets(arguments, MAX_CHARS, stdin);
/*
        if (strcmp(arguments, "\n") == 0) {
                printf("prompt>");
        }
*/        
        // open History
        if ((History = fopen(Hist,"a")) == NULL) {
                perror("Unable to open history file\n");
                exit(-1);
        }
        
        // write command to History
        length = strlen(arguments);
        if (length > 1) {
                fwrite (arguments, length, length, History);
        }

        // figure out the token (somehow)
        token = strtok(arguments," \n");
        
        do {
                arg[i] = token;
                token = strtok(NULL," \n");
                ++i;        
        } while ((token != NULL) && (i < MAX_COMMANDS));

        strcpy (cmd, arg[0]);        

        if (strcmp(arg[0], "exit") == 0) {
                exit(-1);
        }
        
        if (strcmp(arg[0], "explode") == 0) {
                int *bomb = NULL;
                *bomb = 42;
        }
        
        pid = fork();
        
        if (pid == 0) {
                errno = 0;
                result = execvp(arg[0], arg);
                
        if (result != 0) {
                perror("exec failed");
        }
                
                printf("If you got here, things didn't go well\n");
        } else {
                //printf("Parent is running: child pid is %d\n", pid);
                pid = waitpid(pid, &result, 0);
                if (WIFEXITED(result)) {
                        WEXITSTATUS(result);
                }
        }
         
        //printf("Process with PID %d Exiting\n", getpid());
        fflush(stderr);
        fflush(stdout);
        return 0;
}
