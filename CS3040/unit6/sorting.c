#include <stdio.h>

#define NUM_EMPLOYEES 10
#define NAME_MAX 16

struct employee_t {
        char last[NAME_MAX];
        char first[NAME_MAX];
        float salary;
} employees[NUM_EMPLOYEES] = {
        {"Abarnathy", "Alice",  123000.45},
        {"Berry",     "Bob",    39299.44},
        {"Cougar",    "Carol",  132654.55},
        {"Davis",     "David",  44443.99},
        {"Ernest",    "Eddie",  88776.33},
        {"Faulk",     "Frank",  67332.31},
        {"Gobert",    "George", 99292.33},
        {"Hughes",    "Harry",  77773.50},
        {"Irving",    "Ingrid", 99999.99},
        {"Julius",    "Jack",   93939.11}
};

int main(void)
{
        int i;

        for (i=0; i < NUM_EMPLOYEES; ++i) {
                printf("%2d. %-*s = %10.2f\n", 
                       i+1,
                       NUM_EMPLOYEES, 
                       employees[i].last, 
                       employees[i].salary);
        }
        return(0);
}
