#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <iostream>
#include <sys/types.h>
#include <unistd.h>
#define MAX 80
#define PORT 8090
#define SA struct sockaddr
#define BACKLOG 10
#define size_t socklen_t

int main(){    
    size_t sockfd, connfd, len;
    struct sockaddr_in servaddr, client;
    
    // socker create and verification
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if(sockfd == -1){
        std::cout<<"Socket creation failed ....\n";
        return 0;
    }else{
        std::cout << "Socket successfully created...\n";
    }
    bzero(&servaddr, sizeof(servaddr));

    //assign IP, PORT
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);
    if(bind(sockfd, (struct sockaddr *) &servaddr, sizeof(struct sockaddr)) != 0){
        std::cout<<"socket bind failed\n";
        return 0;
    }else{
        std::cout<<"socket successfully binded..\n";
    };

    if((listen(sockfd, 5)) != 0){
        std::cout<<"Listen Failed";
        return 0;
    }else{
        std::cout<< "Listening...";
    };
    while(true){
        std::cout<< "LISTENING";
       cl
        while(!end)
	    {
		if ((n= recv(connfd, &recvs, DATALEN, 0))==-1)                                   //receive the packet
		{
			printf("error when receiving\n");
			exit(1);
		}
		if (recvs[n-1] == '\0')									//if it is the end of the file
		{
			end = 1;
			n --;
		}
		memcpy((buf+lseek), recvs, n);
		lseek += n;
	    }
        if(connfd < 0){
            std::cout<<"Server acceptance Failed";
            return 0;
        }else{
            std::cout<<"Server has accepted the client...\n";
        };
        close(connfd);
    }
    close(sockfd);

    exit(0);

}