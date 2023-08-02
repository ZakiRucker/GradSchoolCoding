//---------------------------------------------------------------------
//File:         main.c
//
//Description:  main.c generates an array of random numbers. After the
//              array is allocated and filled with numbers, a function
//              is called to display all elements of the array, as well
//              as the running subtotal.
//
//Syntax:       In main a pseudo-random generator is used to fill the 
//              array. The display function prints the random numbers
//              along-side three other columns with various types. This
//              allows us to compare how numbers are handled in overflow.
//
//Author:       Z. Rucker              
//---------------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_NUMS 100
#define JUSTIFIED 13
#define ADJUSTIFIED (JUSTIFIED + 1)
#define SUBJUSTIFIED (JUSTIFIED - 1)
#define MAX_UI 4294967295
#define MAX_RANDOM_VALUE 1234567891
#define RED "\x1b[31m"
#define RESET_COLOR "\x1b[0m"

void display(unsigned int* values, unsigned int num_values);

void display(unsigned int* values, unsigned int num_values)
{
        int i = 0;
        unsigned int ui_sum = 0;
        unsigned int ui_sum_r = 0;
        unsigned long long int sum = 0;
        char* rej = "REJECTED";
        char* silence = " ";

        char* header_1 = "Unsigned";
        char* header_2 = "int";
        char* header_3 = "long long";
        char* header_4 = "Subtotal";
        char* header_5 = "Random";
        char* header_6 = "w/ Rollover";
        char* header_7 = "w/o Rollover";
        char* header_8 = "Number";
        char* header_9 = "Detection";
        char* header_10 = "-------------";

        if ((values == 0) || (num_values == 0)){
                printf("Invalid number was generated. Notify tech support at 415-867-5309");
                exit (-1);
        }
        printf("\n\n%*s %*s %*s %*s\n",JUSTIFIED, silence, JUSTIFIED, header_1, JUSTIFIED, header_1, JUSTIFIED, header_1); 
        printf("%*s %*s %*s %*s\n",JUSTIFIED, silence, JUSTIFIED, header_2, JUSTIFIED, header_2, JUSTIFIED, header_3); 
        printf("%*s %*s %*s %*s\n",JUSTIFIED, silence, JUSTIFIED, header_4, JUSTIFIED, header_4, JUSTIFIED, header_4);
        printf("%*s %*s %*s %*s\n",JUSTIFIED, header_5, JUSTIFIED, header_6, JUSTIFIED, header_7, JUSTIFIED, header_7); 
        printf("%*s %*s %*s %*s\n",JUSTIFIED, header_8, JUSTIFIED, header_9, JUSTIFIED, header_9, JUSTIFIED, header_9);
        printf("%*s %*s %*s %*s\n",JUSTIFIED, header_10, JUSTIFIED, header_10, JUSTIFIED, header_10, JUSTIFIED, header_10);

        for (i=0; i < num_values; i++){
                ui_sum += values[i];
                sum += values[i];
                if (ui_sum_r > MAX_UI - values[i]){
                        printf("%*u", JUSTIFIED, values[i]);
                        printf(RED "%*s", ADJUSTIFIED, rej);
                        printf(RESET_COLOR"%*u %*lli \n", ADJUSTIFIED, ui_sum, JUSTIFIED, sum);
                } else {
                        ui_sum_r += values[i];
                        printf("%*u %*u %*u %*lli \n", JUSTIFIED, values[i], JUSTIFIED, ui_sum_r, JUSTIFIED, ui_sum, JUSTIFIED, sum);
                }
        }
        printf("\n");
        return;
}//display()
        
int main (void)
{
        unsigned int i = 0;
        unsigned int num_values = 0;

        //1)determine length of list
        srandom (time (NULL));
        num_values = ((random()) %MAX_NUMS + 1);

        //2)allocate memory for list
        unsigned int *values = malloc(num_values * sizeof(unsigned int));
        
        //3)fill memory with random numbers
        for (i = 0; i < num_values; i++){
                values[i] = (random() %MAX_RANDOM_VALUE);
        }
        
        //4)call display function
        display(values, num_values);
        
        //5)free memory
        free (values);

        return 0;
}//main()
