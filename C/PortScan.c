#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>

int main(int argc, char **argv){

  int mysocket;
  int connecta;
  int start = 0;
  int end = 65535;
  int port;
  char *dest = argv[1];
  struct sockaddr_in target;
  
  if(argc < 2){
    printf("PORT SCANNING - EWERTON FELIPE\n");
    printf("This Port Scanning will go pass for all ports\n"); 
    printf("Usage Example: ./program target\n");
  }
  else{  
    for(port=start; port<end; port++){
      mysocket = socket(AF_INET, SOCK_STREAM, 0); // 0 ip protocol code
      target.sin_family = AF_INET;
      target.sin_port = htons(port);
      target.sin_addr.s_addr = inet_addr(dest);

      connecta = connect(mysocket, (struct sockaddr *)&target, sizeof target);
  
      if(connecta == 0){
        printf("Open Port: %d\n", port);
        close(mysocket);
        close(connecta);
      }
      else{
        close(mysocket);
        close(connecta);
      }
    
    }
  }
  
  return 0;
  
}
