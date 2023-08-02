#include <stdio.h>
#include <limits.h>  // IMPORTANT <----------------


int main(int argc, char *argv[])
{
        unsigned char ch1 = 250;
        unsigned char ch2 = 10;
        unsigned char tot = 0;

        if ((ch1>0) && (ch1 > (UCHAR_MAX-ch2))) {
                // if (250>0) && (250 > 245)...which is true...therefore
                printf("Alert: Unable to add numbers due to overflow\n");
        } else {
                tot = ch1 + ch2; // answer is correct
                printf("%u + %u = %u\n", ch1, ch2, tot);
        }

        return 0;
}
