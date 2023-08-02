#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <strings.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>

#define BUF_SIZE 32
#define HOST_NAME "nps.edu"

// This tries to resolve a domain name to an IP address using getaddrinfo()
int main(int argc, char *argv[]) {
        int result = 0;
        char buf[BUF_SIZE];
        struct addrinfo *start = NULL;
        struct addrinfo *current = NULL;
        struct addrinfo hints;
        struct sockaddr_in *saddr = NULL;

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
                        saddr = (struct sockaddr_in *) current->ai_addr;
                        break;
                } 
        }
        if (current == NULL) {
                fprintf(stderr, "Could not find an IPv4 address");
                exit(-1);
        }

        // Convert and print out the IP address stored in sockaddr_in.
        printf("\nIPv4 address for %s  = %u\n", 
               HOST_NAME,
               ntohl(saddr->sin_addr.s_addr));
        printf("In dotted decimal = %s\n", 
               inet_ntop(AF_INET, &saddr->sin_addr, buf, BUF_SIZE));

        // Free up linked list
        if (start != NULL) {
                freeaddrinfo(start);
                start = NULL;
                current = NULL;
                saddr = NULL;
        }

        fflush(stderr);
        fflush(stdout);
        return result;
}
