#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <strings.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>


int main(int argc, char *argv[]) {
        int sockfd = 0;
        int result = 0;
        struct sockaddr_in myaddr;

        // Open a socket
        sockfd = socket(AF_INET, SOCK_STREAM, 0);
        if (sockfd < 0) {
                fprintf(stderr, "\nsocket() failed.\n");
                exit(-1);
        } 
        printf("\nsocket() successful. fd=%d\n", sockfd);

        // build sockaddr
        bzero(&myaddr, sizeof(struct sockaddr_in));
        myaddr.sin_family = AF_INET;
        myaddr.sin_port = htons(80);        // I will listen on this port
        myaddr.sin_addr.s_addr = htonl(INADDR_ANY);

        // Bind
        result = bind(sockfd, (struct sockaddr *) &myaddr, sizeof(myaddr));
        if ((result != 0) || (errno != 0)) {
                perror("bind() failure");
                fprintf(stderr, "Are you running as root?\n\n");
        } else {
                printf("bind success\n\n");
        }

        // close socket
        if (sockfd > 0) {
                close(sockfd);
        }

        return result;
}
