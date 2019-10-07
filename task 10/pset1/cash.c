#include <stdio.h>
int main(void){
    float n;
    int a,b,c,d;
    printf("enter the change need to be  owed: ");
    scanf("%f",&n);
    a = n/0.25;
    b=(n-(a*0.25))/0.1;
    c=(n-(a*0.25)-(b*0.1))/0.05;
    d=(n-(a*0.25)-(b*0.1)-(c*0.05))/0.01;
    printf("%d of 25 cents,\n%d of 10 cents,\n%d 0f  5 cents,\n%d of 1 cent\n ", a,b,c,d);
}