#include<stdio.h>
#define N 7
int main()
{
    int i, j, temp, a[N]={1, 2, 3, 4, 5, 6, 7}
    for(i=0;i<N/2;i++)
    {
        j=N-i-1;
        temp=a[i];
        a[i]=a[j];
        a[j]=temp;
    }
    for(i=0;i<N;i++)
        printf("%2d", a[i]);
    return 0
}
