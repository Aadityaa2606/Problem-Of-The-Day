#include <stdio.h>
void main(){
    char move;
    float n,m,thick;
    scanf("%c\n%f\n%f\n%f", &move, &n, &m, &thick);
    if (move == 'l')
        printf("%.2f",(((m-n)-1.00)*thick));
    else
        printf("%.2f",((m-n+1.00)*thick));  
}