//---------------------------------------------------------------------
//File:         main.c
//
//Description:  main.c generates an array of random numbers. After the
//              array is allocated and filled with numbers, a function
//              is called to display all elements of the array, as well
//              as the running subtotal.
//
//Syntax:       
//---------------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_NUMS 100
#define JUSTIFIED 13
#define ADJUSTIFIED (JUSTIFIED + 1)
#define SUBJUSTIFIED (JUSTIFIED - 1)
#define MAX_UI 2147483647
#define RED "\x1b[31m"
#define RESET_COLOR "\x1b[0m"

void display(int num, int* num_array);

void display(int num, int* num_array)
{
        int i = 0;
        unsigned int ui_sum = 0;
        unsigned int ui_sum_r = 0;
        long long int sum = 0;
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

        printf("\n\n%*s %*s %*s %*s\n",JUSTIFIED, silence, JUSTIFIED, header_1, JUSTIFIED, header_1, JUSTIFIED, header_1); 
        printf("%*s %*s %*s %*s\n",JUSTIFIED, silence, JUSTIFIED, header_2, JUSTIFIED, header_2, JUSTIFIED, header_3); 
        printf("%*s %*s %*s %*s\n",JUSTIFIED, silence, JUSTIFIED, header_4, JUSTIFIED, header_4, JUSTIFIED, header_4);
        printf("%*s %*s %*s %*s\n",JUSTIFIED, header_5, JUSTIFIED, header_6, JUSTIFIED, header_7, JUSTIFIED, header_7); 
        printf("%*s %*s %*s %*s\n",JUSTIFIED, header_8, JUSTIFIED, header_9, JUSTIFIED, header_9, JUSTIFIED, header_9);
        printf("%*s %*s %*s %*s\n",JUSTIFIED, header_10, JUSTIFIED, header_10, JUSTIFIED, header_10, JUSTIFIED, header_10);

        for (i=0; i < num; i++){
                ui_sum += num_array[i];
                sum += num_array[i];
                if (ui_sum_r > MAX_UI - num_array[i]){
                        printf("%*u", JUSTIFIED, num_array[i]);
                        printf(RED "%*s", ADJUSTIFIED, rej);
                        printf(RESET_COLOR"%*u %*lli \n", ADJUSTIFIED, ui_sum, JUSTIFIED, sum);
                } else {
                        ui_sum_r += num_array[i];
                        printf("%*u %*u %*u %*lli \n", JUSTIFIED, num_array[i], JUSTIFIED, ui_sum_r, JUSTIFIED, ui_sum, JUSTIFIED, sum);
                }
        }
        printf("\n");
        return;
}//display()
        

int main (void)
{
        int i = 0;
        int num = 0;

        //1)determine length of list
        srandom (time (NULL));
        num = ((random()) %MAX_NUMS + 1);

        //2)allocate memory for list
        int *num_array = malloc(num * sizeof(int));
        
        //3)fill memory with random numbers
        for (i = 0; i < num; i++){
                num_array[i] = random();
        }
        
        //4)call display function
        display(num, num_array);
        
        //5)free memory
        free (num_array);

        return 0;
}//main()
