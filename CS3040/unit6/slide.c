#include <stdio.h>

int main(int argc, char *argv[])
{
        int ff()();       // bad
        int fa()[5];      // bad
        int af[5]();      // bad, but almost makes sense
        int (*af[5])();   // this makes sense

        printf("Hello\n");

        return 0;
}
