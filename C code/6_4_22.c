#include <stdio.h>
#include <string.h>

void main(){
    int N,M,i,j;
    scanf("%d", &N);
    scanf("%d", &M);
    char mat[N][M];
    for (i = 0; i < N; i++){
        for (j = 0; j < M; j++){
            char tem;
            scanf("%c", &tem);
            strcpy(mat[i][j], tem);            
        }
    }
    for (i = 0; i < N; i++){
        for (j = 0; j < M; j++){
            printf("%c", mat[i][j]);           
        }
    }
}
