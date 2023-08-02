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
#define JUSTIFIED 16
#define MAX_UI 2147483647


void display(int num, int* num_array);

void display(int num, int* num_array)
{
        int i = 0;
        unsigned int ui_sum = 0;
        unsigned int ui_sum_r = 0;
        long long int sum = 0;
        char* rej = "REJECTED";

/*        char* header_1 = "Unsigned Unsigned Unsigned";
        char* header_2 = "Unsigned \n int \n Subtotal \n w Rollover \n Detection \n ------------- \n ";
        char* header_3 = "Unsigned \n int \n Subtotal \n wo Rollover \n Detection \n ------------- \n ";
        char* header_4 = "Unsigned \n long long \n Subtotal \n wo Rollover \n Detection \n ------------- \n ";
        
        printf("%15s %15s %15s %15s", header_1, header_2, header_3, header_4);
*/      
        for (i=0; i < num; i++){
                ui_sum += num_array[i];
                sum += num_array[i];
                if (ui_sum_r > MAX_UI - num_array[i]){
                        //overflow
                        printf("%20u %20s %20u %20lli \n", num_array[i], rej, ui_sum, sum);
                } else {
                        ui_sum_r += num_array[i];
                        printf("%20u %20u %20u %20lli \n", num_array[i], ui_sum_r, ui_sum, sum);
                }
        }
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
