#include <iostream>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include "socketheader.h"
#include <thread>
#define _OPEN_SYS_SOCK_IPV6
#include <arpa/inet.h>
#include <vector>
#include <unistd.h>
#define PORT 8080
#define _TEXT(x)    __T(x)
#define MAX 80
#define SA struct sockaddr
#define BACKLOG 10
#define size_t socklen_t

void *requestHandler(void *arguments);
void * receiverThreadFn(void *arg);
void * senderThread();
struct beetleRawData{
    int id;
};

struct arg_struct {
    int arg1;
    int arg2;
};


int main(){
    int ret;
    pthread_t receiverThread;
    void * ret_join;
    std::vector<beetleRawData> dataBuffer;

    ret = pthread_create(&receiverThread, NULL, receiverThreadFn, NULL);
    if(ret != 0){
        std::cout<<"thread creation has failed\n";
        exit(EXIT_FAILURE);
    }
    ret = pthread_join(receiverThread, &ret_join);
    if(ret != 0){
        std::cout<<"thread failed to join";
        exit(EXIT_FAILURE);
    }
    std::cout<<"Thread joined, it returned";
    exit(EXIT_SUCCESS);
};

void * receiverThreadFn(void *arg){
    size_t sockfd, connfd, len;
    struct sockaddr_in servaddr, client;
    
    // socker create and verification
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if(sockfd == -1){
        std::cout<<"Socket creation failed ....\n";
        pthread_exit((void*) "Exit");
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
        pthread_exit((void*) "Exit");
    }else{
        std::cout<<"socket successfully binded..\n";
    };

    if((listen(sockfd, 5)) != 0){
        std::cout<<"Listen Failed";
        pthread_exit((void*) "Exit");
    }else{
        std::cout<< "Listening...";
    };

    len = sizeof(client);
    std::vector<int> test = {1,2};
    while (1)
	{
		printf("waiting for data\n");
		connfd = accept(sockfd, (struct sockaddr *) &client, &len);           //accept the packet
		if(connfd < 0){
            std::cout<<"Server acceptance Failed";
            pthread_exit((void*) "Exit");
        }else{
            std::cout<<"Server has accepted the client...\n";
        };

        // struct arg_struct args;
        // args.arg1 = sockfd;
        // args.arg2 = connfd;
        pid_t pid;
        if((pid = fork()) == 0){
            requestHandler(sockfd, connfd)
        }

        // int ret;
        // pthread_t handlerThread;
        // void * ret_join;
        // ret = pthread_create(&handlerThread, NULL, &requestHandler, (void *)&args);                                       //receive packet and response      
	}

    close(sockfd);
    pthread_exit((void*) EXIT_FAILURE);
};

void* requestHandler(int sockfd, int connfd)
{   
    // struct arg_struct *args = arguments;
    // socklen_t sockfd = args->arg1;
    // socklen_t connfd = args->arg2;

    close(sockfd);
	char buf[BUFSIZE];
	FILE *fp;
	char recvs[DATALEN];
	struct ack_so ack;
	int end = 0, n = 0;
	long lseek=0;
	
	printf("receiving data!\n");

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
	ack.num = 1;
	ack.len = 0;
	if ((n = send(connfd, &ack, 2, 0))==-1)
	{
			std::cout<<"ERROR";								//send the ack
			pthread_exit((void*) EXIT_FAILURE);
	}

	std::cout<<buf;
	std::cout<<"a file has been successfully received!\nthe total data received is " << (int)lseek << "\n";
    close(connfd);
}