#include <stdio.h>

int foo()
{
        return 42;
}

int main(void)
{
        &foo(); // ??

        return 0;
}
