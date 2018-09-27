#include<stdlib.h>
#include<stdio.h>
#include<iostream>
using namespace std;
void adddestination(char vertex[5],int distance[5],char destination){
  FILE *fptr;
  fptr=fopen("Vertices.txt","a");
  for (int i=0;i<=4;i++)
  { if (distance[i]!=0){
      fprintf(fptr,"\n '%c' - '%c' [%d]",destination,vertex[i],distance[i]);
    }
  }
  fclose(fptr);
}
int main(){
  //choose whether to add a destination or create a map;
  cout<<"1.Create Map\n2.Add a vertex to previous map\n"<<endl;
  int ans;cin>>ans;
  if (ans==1){
    cout<<"Enter the number of destinations must be less than or equal to 5\n"<<endl;
    int d;cin>>d;char vertex[5];
    cout <<"Enter the destinations one by one press enter after each"<<endl;
    for(int i=0;i<d;i++){
      cin>>vertex[i];
    }
    cout<<"Now take the first destination and enter its distance to the next destination\n if not connected put 0(zero)\nand so on"<<endl;
    int visitedV=0;
    for (int i=0;i<=d;i++){
      char current=vertex[i];
        for(int j=0;j<=d;j++){
          int distance[5];
          if(j!=i and i<j){
            cout<<"Distance from "<<current<<" to "<<vertex[j]<<endl;
            cin>>distance[j];
            if (j==d){adddestination(vertex,distance,current);}
          }else{
            distance[j]=0;
          }
        }
    }
  }else if(ans==2){

    //adddestination(vertex,distance,destination);
  }else{
    cout<<"Unkown choice\n\n"<<endl;
  }
  //char vertex[5]={'A','B','D'};int distance[5]={10,5,76};char destination='C';
  return 0;
}
