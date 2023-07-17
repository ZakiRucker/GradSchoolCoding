#include <stdio.h>

int main()
{
        enum days_of_week { Sun=1, Mon, Tue, Wed, Thu, Fri, Sat };

        enum days_of_week day;

        day = Mon;
        printf("Workday starts on = %d\n", day);

        day = day + 1;
        printf("And then comes %d\n", day);

        day = 42;

        return 0;
}
