#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

#define NUMBER_ARG 1
#define BASE10 10


unsigned long factorial(const unsigned long number)
{
        unsigned long i;
        long result = 0;

        for (i = 1; i <= number; ++i) {
                result *= i;
        }

        return result;
}



int main(int argc, char *argv[])
{
        long num;
        unsigned long result;
        char *endptr = NULL;

        // check input
        if (argc != 2) {
                printf("Invalid number of inputs\n");
                exit(-1);
        }

        // convert input to a number
        errno = 0;
        num = strtol(argv[NUMBER_ARG], &endptr, BASE10);
        if ((errno !=0) || (*endptr != '\0')) {
                printf("Invalid number was provided\n");
                exit(-1);
        }
        if (num < 0) {
                printf("Error: negative numbers cannot be used\n");
                exit(-1);
        }

        // calculate the factorial of the input number (and display it)
        result = factorial(num);
        printf("factorial(%ld)=%lu\n", num, result);

        return(0);
}
