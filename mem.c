#include<stdio.h>
#include<stdlib.h>
//memory management in c
//to be continued
int main(){
  int *ptr;
  ptr=(int*)malloc(1*sizeof(int));
  printf("Enter a value\n");int a;
  scanf("%d",&a);
  ptr=&a;
  printf("%d\n",*ptr );
  printf("Now for the array \n enter only 3 elements\n");
  int *arr[3];int b[3];
  for (int i=0;i<=2;i++){
    scanf("%d\n",&b[i]);
    arr[i]=(int*)malloc(1*sizeof(int));
    arr[i]=&b[i];
  }
  for (int i=0;i<=2;i++){
    printf("%d \n",*arr[i]);
  }
  return 0;
}
