#include<stdio.h>
void main()
{
	int a[10][10],i,j,r,c,x=0;
	printf("\n Enter the number of rows and columns");
	scanf("%d %d",&r,&c);
	printf("\n Enter the elements");
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		   scanf("%d",&a[i][j]);
	}
  for(i=0;i<r-1;i++)
	{
		for(j=0;j<c-1;j++)
		{
		if(a[i][j]==a[i+1][j+1])
		  continue;
		else
		{
		  x=1;
		  break;
	   }
	  }
   }
	if(x==0)
	  printf("\n \t Diagonal elements are identical");
	else
	  printf("\n \t Diagonal elements are not identical");  
}
