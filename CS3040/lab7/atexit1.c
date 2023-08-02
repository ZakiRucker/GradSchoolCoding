#include <stdio.h>
#include <stdlib.h>


void cleanup2(void)
{
        printf("cleanup2() called\n");
        fflush(stdout);
}


void cleanup1(void)
{
        printf("cleanup1() called\n");
        fflush(stdout);
}



int main(void)
{
        int result;

        printf("About to register 'cleanup1()'\n");
        result = atexit(cleanup1);
        if (result != 0) {
                printf("atexit failed with cleanup1()\n");
        } else {
                printf("About to register 'cleanup2()'\n");
                result = atexit(cleanup2);
                if (result != 0) {
                        printf("atexit failed with cleanup2()\n");
                }
        }

        printf("About to exit\n");
        fflush(stdout);
        fflush(stderr);

        return 0;
}
