#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>

int main(int argc, char *argv[])
{
        int sock_fd = 0;
        int result = 0;

        errno = 0;
        sock_fd = socket(AF_INET, SOCK_STREAM, 0);
        if ((errno != 0) || (sock_fd < 0)) {
                perror("Unable to open socket");
        } else {
                printf("\nSocket opened with fd of '%d'\n", sock_fd);

                // NO 'shutdown' is needed because no 
                // connection was established.
                result = close(sock_fd);
                if ((result != 0) || (errno != 0)) {
                        perror("Unable to close socket");
                } else {
                        printf("Socket closed\n\n");
                }
        }

        return 0;
}
