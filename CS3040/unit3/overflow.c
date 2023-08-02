#include <stdio.h>

int buggy(void) {
        int i;
        int total = 0;
        int array[12];

        for (i=0; i<21; ++i) {      // I was dislyexic?
                array[i] = i;
        }
        for (i=0; i<12; ++i) {
                total += array[i];
        }

        return total;
}


int main()
{
        printf("total = %d\n", buggy());
        return(0);
}
