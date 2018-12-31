void gensquare(int n) 
{ 
    int magic[n][n]; 
    memset(magic, 0, sizeof(magic)); 
    int i = n / 2; 
    int j = n - 1; 
    for (int num = 1; num < = n*n; ) 
    { 
        if (i == -1 && j == n) 
        { 
            j = n-2; 
            i = 0; 
        } 
        else
        { 
             if (j == n) 
                 j = 0; 
             if (i < 0) 
                 i = n - 1; 
        } 
        if (magic[i][j]) 
        { 
            j = j - 2; 
            i++; 
            continue; 
        } 
        else
            magic[i][j] = num++; 
  
        j++;
        i--;
    } 
    printf("The Magic Square for n = %d:\n",n)
    printf("Sum of each row or column %d:\n\n",n,n*(n*n+1)/2); 
    for (i=0; i<n; i++) 
    { 
        for (j=0; j<n; j++) 
            printf("%d", magic[i][j]); 
        printf("\n"); 
    } 
} 
int main(void) 
{ 
    int n = 7;
    gensquare (n); 
    return 0; 
} 
