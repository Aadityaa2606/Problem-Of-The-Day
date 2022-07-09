#include <stdio.h>
int main(){
    char move[1];
    float n,m,thick;
    scanf("%s", &move);
    scanf("%f", &n);
    scanf("%f", &m);
    scanf("%f", &thick);
    if (move == "l")
        printf("%.2f",((m-n-1)*thick));
    else
        printf("%.2f",((m-n+1)*thick));  

    return 0;
}