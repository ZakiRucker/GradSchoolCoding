#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <time.h>

#define MYFILE "/etc/passwd"
#define BUFSIZE 80

void perms(const unsigned char bits);

int main(void)
{
        struct stat metadata;
        char errmsg[80] = "Error: Could not open " MYFILE;
        struct tm *newtime = NULL;
        char chartime[BUFSIZE];

        // Get the metadata
        stat(MYFILE, &metadata);
        if (errno) {

                perror(errmsg);
                exit(-1);
        }

        // Display the permissions
        printf("%s\n" "permissions = ", MYFILE);
        perms((metadata.st_mode & 00700)>>6);  // owner bits
        perms((metadata.st_mode & 00070)>>3);  // group bits
        perms(metadata.st_mode & 00007);       // other 
        printf("\n");

        // Display last mod time
        newtime = localtime(&(metadata.st_mtim.tv_sec)); // breakdown secs
        if (newtime == NULL) {
                perror("Error converting time");
                exit(-1);
        }
        strftime(chartime, BUFSIZE, "%F %T", newtime); // convert to string
        printf("last mod.   = %s\n", chartime);

        return 0;
}


void perms(const unsigned char bits)
{
        if (bits & 0b100) {
                printf("r");
        } else {
                printf("-");
        }
        if (bits & 0b010) {
                printf("w");
        } else {
                printf("-");
        }
        if (bits & 0b001) {
                printf("x");
        } else {
                printf("-");
        }
}
