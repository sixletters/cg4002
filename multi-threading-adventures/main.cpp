#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <unistd.h>

void *thread_fnc(void * arg);

char thread_msg[] = "HELLO THREAD!";

int main(){
    int ret;
    pthread_t my_thread;
    void * ret_join;

    ret = pthread_create(&my_thread, NULL, thread_fnc, (void*) thread_msg);
    if(ret != 0){
        std::cout<<"thread creation has failed\n";
        exit(EXIT_FAILURE);
    }
    std::cout<<"Waiting for thread to finish...\n";
    ret = pthread_join(my_thread, &ret_join);
    if(ret != 0){
        std::cout<<"thread failed to join";
        exit(EXIT_FAILURE);
    }
    std::cout<<"Thread joined, it returned";
    std::cout<<"New thread Message" << thread_msg;
    exit(EXIT_SUCCESS);

}

void * thread_fnc(void *arg){
    std::cout<<"THIS IS A THREAD FNC"<< (char *) arg;
    strcpy(thread_msg, "BYE!");
    pthread_exit((void*) "Exit");
}