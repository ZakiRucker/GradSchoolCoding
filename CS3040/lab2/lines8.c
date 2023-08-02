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

//after line is printed
//fflush (stdout);

//move the cursor
//printf("\033[%d;%dH",y,x);

//define display_line function
int display_line(int col, int row, int length);
        for (i=ZIP; i < (num_lines - 1); ++i){
                for (i=1; i< len_lines; ++i){
                        printf("-");
                }
        }
return
}        

int main (int argc, char *argv[])
{
        int num_lines = ZIP;
        int len_lines = ZIP;
        int i = ZIP;
        Max_rows = num_lines;

        //1. Verify inputs and convert to integers.
        //verify the number of arguments
        if (argc != VALID_ARGS){
                printf("Please provide %d valid inputs\n", VALID_ARGS);
                exit(-1);
        }

        //check argv[1] and argv[2] for digits
        
        if (isdigit(argv[NUM_OF_LINES][i]) == ZIP){
                printf("%c is not a valid digit\n", argv[NUM_OF_LINES][i]);
                exit (-1);
        } if (strlen(argv[NUM_OF_LINES])>=2){
                if (isdigit(argv[NUM_OF_LINES][i + 1]) == ZIP){
                        printf("%c is not a valid digit\n", argv[NUM_OF_LINES][i +1]);
                        exit (-1);
                } 
        } if (strlen(argv[NUM_OF_LINES])>=3){
                if (isdigit(argv[NUM_OF_LINES][i + 2]) == ZIP){
                        printf("%c is not a valid digit\n", argv[NUM_OF_LINES][i + 2]);
                        exit (-1);
                } 
        } if (strlen(argv[NUM_OF_LINES])==4){
                if (isdigit(argv[NUM_OF_LINES][i + 3]) == ZIP){
                        printf("%c is not a valid digit\n", argv[NUM_OF_LINES][i + 3]);
                        exit (-1);                
                }
        }
        //convert argv[1] and argv[2] to ints
        num_lines = strtol (argv[NUM_OF_LINES], NULL, BASE);
        len_lines = strtol (argv[LEN_OF_LINES], NULL, BASE);
        
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
                px[i] = (((random()) %num_lines) + 1);
                py[i] = (((random()) %num_lines) + 1);
        }
        //clear the screen
        printf("\033[2J");
      
        //call display_line function
        display_line(*px, *py);     

        //sleep
        //free malloc
        free (px);
        free (py);

return 0;
}
