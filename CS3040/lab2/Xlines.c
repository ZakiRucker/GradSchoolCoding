//---------------------------------------------------------------------
//File: lines.c
//
//Description:  lines will draw a prescribed number of lines,
//              of prescribed length based on input from the
//              operator on the command line.
//
//Syntax: The command line inputs will draw lines on the command prompt
//
//plan:
//      1. verify valid input/convert to #s
//      2. get random coordinates
//              a. get the terminal size
//              b. allocate memory
//              c. seed the generator
//              d. get all coordinates needed
//                      i. print to screen
//      3. clear screen
//      4. display each line (for loop to print dashes)
//      5. move cursor to bottom of the screen & return 0
//---------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <sys/ioctl.h>
#include <time.h>
#include <string.h>
#include <ctype.h>

//definitions
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

//global variables
int Max_rows = ZIP;
int Max_cols = ZIP;

//functions

//after line is printed
//fflush (stdout);


//move the cursor
//printf("\033[%d;%dH",y,x);
/*
//define display_line function
for (){
        int display_line(int col, int row, int length);
        printf("the number of lines to print is %d\n", argv[1]);
        printf("the length of the lines to print is %d\n", argv[2]);
        return
}        
//print range
int x;
x = (random () % Max_col) +1;

//store the variables
int *x = NULL;
x = malloc (sizeof(int) *num);

OR

struct location{
      int x;
      int y;
}
struct location *coords;
coords = malloc (sizeof(struct location) * num);
coords [i].x = (random () % Max_cols) +1;

*/
int main (int argc, char *argv[])
{
        int num_lines = ZIP;
        int len_lines = ZIP;
        int i = ZIP;
        int arg_len = ZIP;

        //1. Verify inputs and convert to integers.
        //verify the number of arguments
        if (argc != VALID_ARGS){
                printf("Please provide %d valid inputs\n", VALID_ARGS);
                exit(-1);
        }
        //convert argv[1] and argv[2] to ints
        num_lines = strtol (argv[NUM_OF_LINES], NULL, BASE);
        len_lines = strtol (argv[LEN_OF_LINES], NULL, BASE);


/*        //check argv[1] and argv[2] for digits
        arg_len = strlen(num_lines);
        for (i = ZIP; i == (arg_len - 1); i++){
                if (isdigit(argv[NUM_OF_LINES][i]) != ZIP){
                        printf("%d is not a valid digit\n", argv[NUM_OF_LINES][i]);
                        exit (-1);
                }
        }        
        
        //verify the number of lines is valid
        if ((num_lines < MIN_NUM_LINES)||(num_lines > MAX_NUM_LINES)){
                printf("Please adjust %s to a number from 1 to 1000\n", argv[1]);
                exit (-1);
        }      
        //verify the length of lines is valid
        if ((len_lines < MIN_LEN_LINE)||(len_lines > MAX_LEN_LINE)){
                printf("Please adjust %s to a number from 1 to 40\n", argv[2]);
                exit (-1);
        }

        //random number generator
        srandom (time (NULL));

        //store line start position in the heap
        //malloc

        //clear the screen
        printf("\033[2J");

        //determine the size of the terminal
        struct winsize win;
        ioctl (0, TIOCGWINSZ, &win);
        Max_rows = win.ws_row;
        Max_cols = win.ws_col;
      
        //call display_line function
      
        //sleep
*/
return 0;
}
