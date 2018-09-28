#include<stdio.h>
#include<stdlib.h>
//memory management in c
int main(){
  int *ptr;
  ptr=(int*)malloc(1*sizeof(int));
  printf("Enter a value");int a;
  scanf("%d",&a);
  ptr=&a;
  printf("%d\n",*ptr );
  return 0;
}
