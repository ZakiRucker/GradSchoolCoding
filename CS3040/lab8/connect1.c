#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <strings.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>

#define BUF_SIZE 32
#define HOST_NAME "tor.ern.nps.edu"

// This tries to resolve a domain name to an IP address using getaddrinfo()
int main(int argc, char *argv[]) {
        int result = 0;
        int fd_sock;
        struct addrinfo *start = NULL;
        struct addrinfo *current = NULL;
        struct addrinfo hints;

        // Fill out the 'hints' with the kind of answers we want.
        bzero(&hints,sizeof(hints));
        hints.ai_family   = AF_INET;     // we want IPv4
        hints.ai_socktype = SOCK_STREAM; // we're going to use TCP

        // Resolve DNS...
        result = getaddrinfo(HOST_NAME, "80", &hints, &start);
        if ((result != 0) || (start == NULL)) {
                fprintf(stderr,
                        "DNS resolution failed for %s: %s\n", 
                        HOST_NAME, gai_strerror(result));
                exit(-1);
        }

        // getaddrinfo returns a linked list of DNS results.
        // Go thru the list looking for an IPv4 address.
        // When I find one, I've got a completed sockaddr_in.
        for (current=start; current != NULL; current = current->ai_next) {
                if (current->ai_family == AF_INET) {
                        // I found an IPv4 address.
                        // "current" now points to a completed addrinfo 
                        // type, (see "man getaddrinfo"), which contains a 
                        // completed sockaddr.
                        break;
                } 
        }
        if (current == NULL) {
                fprintf(stderr, "Could not find an IPv4 address");
                exit(-1);
        }

        // Get a descriptor
        errno = 0;
        fd_sock = socket(current->ai_family, current->ai_socktype, 0);
        if ((fd_sock < 0) || (errno != 0)) {
                perror("Unable to get a descriptor");
                exit(-1);
        }

        // Try to connect to the server
        result = connect(fd_sock, current->ai_addr, current->ai_addrlen);
        if (result == 0) {
                printf("Connection made\n");
        } else {
                perror("Unable to connect to server");
        }

        // If connection was made, then make our request of the server.

        // When done...
        if (fd_sock > 0) {
                // Close the TCP connection
                shutdown(fd_sock, SHUT_RDWR);
                printf("Connection closed\n\n");
        }
        
        // Free up linked list
        if (start != NULL) {
                freeaddrinfo(start);
                start = NULL;
                current = NULL;
        }

        fflush(stderr);
        fflush(stdout);
        return result;
}
