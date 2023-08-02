#include <stdio.h>

void waste(double input[]) {
        double array[1000];
        array[0] = input[0];
        waste(array);
}


int main(void) {
        double start[1000];
        start[0] = 42;
        waste(start);
        return 0;
}
