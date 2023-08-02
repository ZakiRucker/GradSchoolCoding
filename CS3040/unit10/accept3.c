#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <unistd.h>
#include <strings.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>

#define MYBUFSIZE 1024


// ******************************* M A I N ********************************
// client connects to port 7000 on localhost
int main(void)
{
        int num;
        int sockfd;
        int result;
        char buf[80];
        struct sockaddr_in myaddr;

        // Get a handle to a new socket
        errno = 0;
        sockfd = socket(AF_INET, SOCK_STREAM, 0);
        if ((errno != 0) || (sockfd < 0)) {
                perror("Unable to open socket");
                exit(-1);
        }

        // Prepare the sockaddr 
        bzero(&myaddr, sizeof(myaddr));
        myaddr.sin_family = AF_INET;
        myaddr.sin_port = htons(7000);
        errno = 0;
        result = inet_pton(AF_INET, "127.0.0.1", &myaddr.sin_addr);
        if ((result < 0) || (errno != 0)) {
                perror("pton error");
                exit (-1);
        } else if (result == 0) {
                fprintf(stderr, "Invalid IP address string");
                exit(-1);
        } 

        // connect to the server
        result = connect(sockfd, 
                        (struct sockaddr *) &myaddr, 
                        sizeof(myaddr));
        if (result != 0) {
                printf("Connection failed\n");
        } else {
                printf("Connection made\n");

                // prompt for data to send to server
                strcpy(buf, "TIME");

                // Send the data to the server
                num = write(sockfd, buf, strlen(buf));
                if ((num > 0) && (errno == 0)) {
                        printf("Sent '%s'\n", buf);

                        // Read the server's response
                        // Bad assumption that I can read the entire
                        // response in one call
                        num = read(sockfd, buf, MYBUFSIZE);
                        printf("%s\n", buf);

                        // Close the TCP connection
                        shutdown(sockfd, SHUT_RDWR);
                        printf("Connection closed\n\n");
                } else {
                        perror("Write request failed");
                }
        }        

        // **** CLEAN UP ****

        // Close socket
        if (sockfd > 0) {
                close(sockfd);
        }

        fflush(stdout);
        fflush(stderr);
        return(0);
}

