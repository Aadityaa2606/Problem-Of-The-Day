#include <stdio.h>
#include <stdbool.h>
int main(){
    int i,n,j=1,k=1,l=1,m=1,p;
    bool start=true;
    scanf("%d", &n);
    i = n-1;
    while (i > -1){
        while (j < i+1){
            printf(". ");
            j++;
        }
        j=1; 
        if (start){
            printf("* ");
            for (p= 1; p < n; p++){
                if (p == n-1){
                    printf(".");
                }
                else{
                    printf(". ");
                }
            }
            
        }
        else{
            while (k < (2*n)-2){
            printf("* ");
            while (l<k+1){
                printf(". ");
                l++;
            }   
            l=1;
            printf("* ");
            k+=2;
            break;
            }
        while (m < i+1){
            if (m == i){
                printf(".");
            }
            else{
                printf(". ");
            }
            m++;
        }
        m=1;        
        }
        printf("\n");
        i--;
        start = false;
    }
    return 0;
}
