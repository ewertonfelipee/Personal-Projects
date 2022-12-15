#include <stdio.h>
#include <netdb.h>
#include <arpa/inet.h>

int main(int argc, char **argv){

    if(argc < 2){
        printf("Dns Resolver\n");
        printf("Usage: ./program target\n");
    }
    else{
        struct hostent *target = gethostbyname(argv[1]); // get hostname
        if(!target){
            printf("ERROR\n");
        }
        else{
            printf("Enter with IP: %s\n", inet_ntoa(*(struct in_addr *)target->h_addr)); // convert to host in ip address
        }
    }
    return 0;
}
