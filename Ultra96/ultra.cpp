#include <iostream>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <thread>
#define _OPEN_SYS_SOCK_IPV6
#include <arpa/inet.h>
#include <unistd.h>
#define PORT 8080
#define _TEXT(x)    __T(x)
void receiverThread();
void senderThread();
void predictorThread();

int main(){
    
}