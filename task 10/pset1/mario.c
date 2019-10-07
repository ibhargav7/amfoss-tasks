#include <stdio.h>

int main(void)
{
    int n ,i=0,j=0,k=0;
    printf("enter a height: ");
    scanf("%d",&n);
    for (i=0;i<=n;i++)
    {
        for (k=0;k<=n-i;k++){
            printf(" ");
        }
        for (j=0;j<=i;j++){
            printf("#");
        }
        printf("\n");
    }
}
