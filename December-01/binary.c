#include<stdio.h>

int main(void)

{
    int i,a[10],search,n,first,last,middle;
    printf("Enter the number of elements:\n");
    scanf("%d",&n);
    printf("Enter the elements:\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("Enter the search element:\n");
    scanf("%d",&search);
    first=0;
    last=n-1;
    while(first<=last)
    {
        middle=(first+last)/2;
        if(a[middle]>search)
        {
            last=middle-1;
        }
        else if(a[middle]<search)
        {
            first=middle+1;
        }
        else
        {
            printf("The search element is found at location %d",middle+1);
            break;
        }
    }
    
    if(first>last)
    {
        printf("The search element is not present in the array");
    }
    printf("\n");
    
}
