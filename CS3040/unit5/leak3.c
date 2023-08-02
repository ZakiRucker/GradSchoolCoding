#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_BYTES 20

int main(void)
{
        char *ptr = NULL;

        ptr = malloc(NUM_BYTES);

        strncpy(ptr, "hello world", NUM_BYTES);

        printf("%s\n", ptr);

        free(ptr);

        strncpy(ptr, "goodbye world", NUM_BYTES); // changing after freeing
        printf("%s\n", ptr);                      // reading after freeing

        return 0;
}
