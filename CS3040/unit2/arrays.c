#include <stdio.h>

int main()
{
        char foo[10];
        char *p;

        foo[4] = 'R';

        p = foo;
        // p = &foo;      // same result - not necssary
        // p = (&foo[0]); // same result - not necssary

        printf("foo[4] = %c\n", p[4]);
        printf("foo[4] = %c\n", foo[4]);

        return 0;
}
