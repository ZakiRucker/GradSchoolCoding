#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <strings.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>



// Provide an IP address on command-line, and it will create a sockaddr
// for a port 80 socket "by hand".
int main(int argc, char *argv[]) {
        int result = 0;
        struct sockaddr_in myaddr;

        if (argc != 2) {
                fprintf(stderr,"Improper syntax. Provide an IP address\n");
                exit(-1);
        }

        bzero(&myaddr, sizeof(struct sockaddr_in));

        errno = 0;
        myaddr.sin_family = AF_INET;
        myaddr.sin_port = htons(80);
        result = inet_pton(AF_INET, argv[1], &myaddr.sin_addr);
        if ((result < 0) || (errno != 0)) {
                perror("pton error");
                result = -1;
        } else if (result == 0) {
                fprintf(stderr, "Invalid IP address string.\n");
                result = -1;
        } else {
                printf("\nSuccessfull conversion of string '%s' "
                       "to a 32-bit IP address.\n", argv[1]);
                printf("IP address in number form = %u\n\n", 
                        ntohl(myaddr.sin_addr.s_addr));
        }

        return result;
}
