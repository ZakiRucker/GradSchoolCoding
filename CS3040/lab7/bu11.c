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
#include <stdlib.h> // exit
#include <string.h> // fgets
#include <sys/types.h> // pid
#include <unistd.h> // fork,pid, execvp
#include <errno.h>
#include <sys/wait.h> // wait

#define HIST_PATH 
#define MAX_COMMANDS 11
#define MAX_CHARS 80
#define TIMER 300000

FILE *History = NULL;
const char *Hist = "shell-history.txt";
char *Arg[MAX_CHARS];
char Arguments[MAX_COMMANDS];

void clean (void);

void clean (void) 
{
        if (History != NULL) {
                if ((fclose(History)) != 0) {
                        perror ("Unable to close History");
                }
                History = NULL;
        }
        
        // set arrays to zero
        bzero(Arguments, MAX_COMMANDS);
        bzero(Arg, (sizeof(char *)*MAX_CHARS));

}

int main (void)
{
        char *token = NULL;
        unsigned int pid;  
        unsigned int i;
        int result;
        unsigned int length;        
        
        atexit(clean);

        alarm(TIMER);
        
        // loop
        while (1) {
                printf("prompt>");
                bzero(Arguments, MAX_COMMANDS);
                bzero(Arg, (sizeof(char *)*MAX_CHARS));
                length = 0;
                pid = 0;
                i = 0;
                result = 0;

                // get user input
                fgets(Arguments, MAX_CHARS, stdin);

                if ((strlen(Arguments)) == 1) {
                        continue;
                }
               
                // open shell-history.txt
                if ((History = fopen(Hist,"a")) == NULL) {
                        perror("Unable to open history file\n");
                        exit(-1);
                }
                
                length = strlen(Arguments);

                // set command string
                token = strtok(Arguments," \n");
                do {
                        Arg[i] = token;
                        token = strtok(NULL," \n");
                        ++i;        
                } while ((token != NULL) && (i < MAX_COMMANDS));
                Arg[i] = token;

                // write to shell-history.txt
                fwrite (Arg, (length * sizeof(char)), length, History);
                
                // close shell-history.txt
                if ((fclose(History)) != 0) {
                        perror ("Unable to close History");
                }
                History = NULL;

                // check escape commands
                if (strcmp(Arg[0], "exit") == 0) {
                        exit(-1);
                }
                
                if (strcmp(Arg[0], "explode") == 0) {
                        int *bomb = NULL;
                        *bomb = 42;
                }
       
                // fork and exec
                pid = fork();
                if (pid == 0) {
                        errno = 0;
                        result = execvp(Arg[0], Arg);
                if (result < 0) {
                        perror("exec failed, enter a valid shell command");
                        perror ("exec failed");
                        exit (-1); 
                }
                } else {// let the parent wait
                        pid = waitpid(pid, &result, 0);
                        if (WIFEXITED(result)) {
                                WEXITSTATUS(result);
                        }
                }
        }
        
        fflush(stderr);
        fflush(stdout);
        return 0;
}
