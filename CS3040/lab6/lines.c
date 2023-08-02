//---------------------------------------------------------------------
//File: lines.c
//
//Description:  lines will draw a prescribed number of lines,
//              of prescribed length based on input from the
//              operator on the command line.
//
//Syntax: The command line inputs will draw lines on the command prompt
//---------------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <sys/ioctl.h>
#include <time.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>

#define ZIP 0
#define VALID_INT 4
#define BASE 10
#define VALID_ARGS 3
#define MIN_NUM_LINES 1
#define MAX_NUM_LINES 1000
#define MIN_LEN_LINE 1
#define MAX_LEN_LINE 40
#define NUM_OF_LINES 1
#define LEN_OF_LINES 2
#define DISPLAY_DELAY 1
#define OFFSET_1 1
#define OFFSET_2 2
#define OFFSET_3 3
#define OFFSET_4 4
#define COLOR_SCALE 9

void display_line(int px[], int py[], int len_lines);

//global variables
int Max_rows = ZIP;
int Max_cols = ZIP;

//display_line function
int i = ZIP;
void display_line(int px[i], int py[i], int len_lines)
{
        //random color generator
        int z = (random() %COLOR_SCALE);
        printf("\x1b[3%dm", z);
        
        printf("\x1b[?7l");  //turn off word wrap
        printf("\033[%d;%dH", px[i],py[i]); //set cursor in random location
        for (int i=ZIP; i<len_lines; ++i){
                printf("-");
        }
        fflush(stdout);
        sleep(DISPLAY_DELAY);
        printf("\x1b[?7l");  //word wrap reset
        printf("\x1b[0m");  //color reset
        return;
}
        

int main (int argc, char *argv[])
{
        int num_lines = ZIP;
        int len_lines = ZIP;
        int i = ZIP;

        // Verify inputs
        if (argc != VALID_ARGS){
                printf("Please provide %d valid inputs\n", VALID_ARGS);
                exit(-1);
        }

        //check argv[1] and argv[2] for digits
        if (isdigit(argv[NUM_OF_LINES][i]) == ZIP){
                printf("%s is not a valid digit\n", argv[NUM_OF_LINES]);
                exit (-1);
        } if (strlen(argv[NUM_OF_LINES])>= OFFSET_2){
                if (isdigit(argv[NUM_OF_LINES][i + OFFSET_1]) == ZIP){
                        printf("%s is not a valid digit\n", argv[NUM_OF_LINES]);
                        exit (-1);
                } 
        } if (strlen(argv[NUM_OF_LINES])>= OFFSET_3){
                if (isdigit(argv[NUM_OF_LINES][i + OFFSET_2]) == ZIP){
                        printf("%s is not a valid digit\n", argv[NUM_OF_LINES]);
                        exit (-1);
                } 
        } if (strlen(argv[NUM_OF_LINES])==OFFSET_4){
                if (isdigit(argv[NUM_OF_LINES][i + OFFSET_3]) == ZIP){
                        printf("%s is not a valid digit\n", argv[NUM_OF_LINES]);
                        exit (-1);                
                }
        }
        
        //convert argv[1] and argv[2] to ints
        num_lines = strtol (argv[NUM_OF_LINES], NULL, BASE);
        len_lines = strtol (argv[LEN_OF_LINES], NULL, BASE);
        
        //verify the number of lines is valid
        if ((num_lines < MIN_NUM_LINES)||(num_lines > MAX_NUM_LINES)){
                printf("Please adjust %s to a number from 1 to 1000\n", argv[NUM_OF_LINES]);
                exit (-1);
        }      
        
        //verify the length of lines is valid
        if ((len_lines < MIN_LEN_LINE)||(len_lines > MAX_LEN_LINE)){
                printf("Please adjust %s to a number from 1 to 40\n", argv[LEN_OF_LINES]);
                exit (-1);
        }
        
        //determine the size of the terminal
        struct winsize win;
        ioctl (ZIP, TIOCGWINSZ, &win);
        Max_rows = win.ws_row;
        Max_cols = win.ws_col;
        
        //store line start position in the heap
        int *px = malloc((num_lines) * sizeof(int));
        int *py = malloc((num_lines) * sizeof(int));
        
        srandom (time (NULL));
        for (i = ZIP; i < num_lines; i++){
                px[i] = ((random()) %Max_rows);
                py[i] = (((random()) %Max_cols) + OFFSET_1);
        }
        //clear the screen
        printf("\033[2J");
        
        //call display_line function
        for (i=ZIP; i<num_lines; ++i){
                display_line(&px[i],&py[i],len_lines);
        }
        
        //free memory
        free (px);
        free (py);

        //return pointer
        printf("\033[%d;%dH",Max_rows,ZIP);

        return 0;
}
