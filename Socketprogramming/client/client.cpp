#include <iostream>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#define _OPEN_SYS_SOCK_IPV6
#include <arpa/inet.h>
#include <unistd.h>
#define PORT 8080
#define _TEXT(x)    __T(x)

int main(){
    int sockfd, connfd;
    struct sockaddr_in server;


    // Socket Creation
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if(sockfd == -1){
        std::cout<<"Socket creation failed\n";
        return 0;
    }
    else{
        std::cout<<"Socket successfully created\n";
    }
    bzero(&server, sizeof(server));

    server.sin_family = AF_INET;
    inet_pton(AF_INET, "127.0.0.1", &server.sin_addr.s_addr);
    server.sin_port = htons(PORT);

    if(connect(sockfd, (struct sockaddr*) &server, sizeof(server)) != 0){
        std::cout<<"connection failed\n";
        return 0;
    }else{
        std::cout<<"Connected to the server..\n";
    }

    close(sockfd);

}