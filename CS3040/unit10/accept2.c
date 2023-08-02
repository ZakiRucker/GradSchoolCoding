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
// echo client connects to port 8000 on localhost
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
        myaddr.sin_port = htons(8000); 
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
                perror("Connection failed");
        } else {
                printf("Connection made\n");

                // prompt for data to send to server
                printf("Enter text to send: ");
                fgets(buf, MYBUFSIZE, stdin);
                if (strlen(buf) == 0) {
                        printf("No data provided. Exiting.\n");
                        exit(0);
                }
                buf[strlen(buf)-1] = '\0'; // get rid of last CR

                // Send the data to the server
                num = write(sockfd, buf, strlen(buf));
                if ((num > 0) && (errno == 0)) {
                        printf("Sent '%s'\n", buf);

                        // Read the server's response.
                        // I'm assuming I get full response in one read,
                        // which is a bad assumption.
                        num = read(sockfd, buf, MYBUFSIZE);
                        if ((errno ==0) && (num > 0)) {
                                buf[num] = '\0';
                                printf("Received '%s'\n", buf);
                        } else if ((errno == 0) && (num == 0)) {
                                printf("No data received\n");
                        } else {
                                perror("Read failure");
                        }

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

