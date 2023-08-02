#include <stdio.h>
#include <limits.h>


int main(int argc, char *argv[])
{
        unsigned char ch1 = 250;
        unsigned char ch2 = 10;
        unsigned char tot = 0;

        tot = ch1 + ch2; // answer is wrong
        printf("%u + %u = %u\n", ch1, ch2, tot);

        return 0;
}
