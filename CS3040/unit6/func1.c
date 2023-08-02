#include <stdio.h>

void display(char *msg)
{
        printf("%s\n", msg);
}

int main(void)
{
        void (*foo)(char *string) = NULL;

        foo = display;

        (*foo)("Hello World");
        foo("Hello World");

        return 0;
}
