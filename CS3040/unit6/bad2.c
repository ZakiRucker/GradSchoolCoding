#include <stdio.h>

int foo()
{
        return 42;
}

int main(void)
{
        foo() = 100;  // ??

        return 0;
}
