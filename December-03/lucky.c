#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>

bool lucky(int sumf,int suml);

int n,i=0,count = 0,a[100],sumf=0,suml=0,temp;

int main(void)
{
    
    printf("Enter a ticket number:");
    scanf("%d",&n);
    temp = n;
    
    
    while(n>0)
    {
        a[i] = n % 10;
        i++;
        count++;
        n = n / 10;
        
    }
    
    if(count % 2 == 0)
    {
        for(i=0;i<(count/2);i++)
        {
            sumf = sumf + a[i];
        }
        for(i=(count/2);i<count;i++)
        {
            suml = suml + a[i];
        }
    }
    lucky(sumf,suml);
}
    
bool lucky(int sumf,int suml)
{
    if(sumf == suml)
    {
        printf("isLucky(n) =  true\n");
            
    }
    else
    {
        
        printf("isLucky(n) =  false\n");
    }
}
    

