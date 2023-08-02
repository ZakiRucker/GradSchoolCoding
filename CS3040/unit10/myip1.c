#include <stdio.h>
#include <strings.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>


int main(void)
{
        struct sockaddr_in myaddr;
        unsigned int ip = 3232261121u;

        bzero(&myaddr, sizeof(struct sockaddr_in));
        myaddr.sin_family = AF_INET;
        myaddr.sin_port = htons(80);
        myaddr.sin_addr.s_addr = htonl(ip); // I got this somehow

        // Continue with your networking stuff here....

        return 0;
}
