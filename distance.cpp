#include<stdlib.h>
#include<stdio.h>
using namespace std;
void adddestination(char vertex[5],int distance[5],char destination){
  FILE *fptr;
  fptr=fopen("Vertices.txt","a");
  for (int i=0;i<=4;i++)
  { if (distance[i]!=0){
      fprintf(fptr,"\n %c - %c [%d]",destination,vertex[i],distance[i]);
    }
  }
  fclose(fptr);
}
int main(){
  char vertex[5]={'A','B','D'};int distance[5]={10,5,76};char destination='C';
  adddestination(vertex,distance,destination);
  return 0;
}
