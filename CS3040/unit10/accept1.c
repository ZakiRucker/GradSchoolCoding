#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <strings.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#define MYBUFSIZE 1024

void echo(const int fd);


// echo server listening on port 8000
int main(int argc, char *argv[]) {
        int sockfd = 0;
        int newfd = 0;
        int result = 0;
        int listening = 0;
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
        myaddr.sin_port = htons(8000);        // I will listen on this port
        myaddr.sin_addr.s_addr = htonl(INADDR_ANY);

        // Bind
        result = bind(sockfd, (struct sockaddr *) &myaddr, sizeof(myaddr));
        if ((result != 0) || (errno != 0)) {
                perror("bind() failure");
        } else {
                printf("bind success\n");
                result = listen(sockfd, 10);
                if ((result != 0) || (errno != 0)) {
                        perror("listen() failure");
                }
        }

        if (result == 0) {
                printf("listen success\n");
                listening = 1;
                printf("Will try an infinite loop on accept()\n");
                while (1) {
                        newfd = accept(sockfd, NULL, NULL);
                        if ((result < 0) || (errno != 0)) {
                                perror("accept() failure");
                        } else {
                                echo(newfd);
                                close(newfd);
                        }
                }
        }

        if (listening) {
                // Close the TCP connection
                shutdown(sockfd, SHUT_RDWR);
                printf("Connection closed\n\n");
                listening = 0;
        }

        // close socket
        if (sockfd > 0) {
                close(sockfd);
                sockfd = -1;
        }

        fclose(stderr);
        fclose(stdout);
        return result;
} // main()



void echo(const int fd)
{
        int num;
        int result;
        char buf[MYBUFSIZE];

        printf("Received request\n");

        // Echo what was sent to us
        do {
                num = read(fd, buf, MYBUFSIZE);
                if ((num > 0) && (errno == 0)) {
                        buf[num] = '\0';
                        printf("Received '%s'\n", buf);
                        result = write(fd, buf, num);
                        if ((result == 0) || (errno != 0)) {
                                perror("Write error");
                                break;
                        }
                } else if (errno != 0) {
                        perror("Read error");
                        break;
                }
        } while (num > 0);
} 

