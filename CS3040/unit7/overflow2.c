#include <stdio.h>


int main(int argc, char *argv[])
{
        unsigned char ch1 = 250;
        unsigned char ch2 = 10;
        unsigned char tot = 0;

        // this test fails 
        if (((ch1 + ch2) < ch1) || ((ch1 + ch2) < ch2)) {
                printf("Error: integer overflow\n");
        } else {
                tot = ch1 + ch2;
                printf("%u + %u = %u\n", ch1, ch2, tot);
        }

        return 0;
}
