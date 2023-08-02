#include <stdio.h>

int main(void)
{
        int i;

        for (i=0; i < 10; ++i) {
                if (i == 5) {
                        continue;
                }
                printf("i = %d\n", i);
        }

        return 0;
}
