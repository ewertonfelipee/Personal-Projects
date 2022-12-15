#include <stdio.h>
#include <netdb.h>
#include <arpa/inet.h>

int main(int argc, char **argv){

    char *ip;
    ip = argv[1];

    if(argc < 2){
        printf("Dns Resolver\n");
        printf("Usage: ./program target\n");
    }
    else{
        struct hostent *target = gethostbyname(ip); // get hostname
        if(!target){
            printf("ERROR\n");
        }
        else{
            char *host = inet_ntoa(*(struct in_addr *)target->h_addr);// convert to host in ip address
            printf("IP: %s\n", host); 
        }
    }
    return 0;
}
