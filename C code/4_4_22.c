// #include <stdio.h>
// void sort(int n,int* arr[]){
//     int i;
//     for (i = 0; i < n; i++){
//         int temp = 0;
//         if (arr[i] > arr[i+1]){
//             temp = *arr[i];
//             *arr[i] = *arr[i+1];
//             *arr[i+1] = temp;
//         }
//     }
//     for (i = 0; i < n; i++){
//         printf("%d ", arr[i]);
//     }
// }

// void main(){
//     int i,n,m;
//     scanf("%d",&n);
//     scanf("%d", &m);
//     int nval[n+m];
//     for (i = 0; i < n; i++){
//         scanf("%d", &nval[i]);
//     }               
//     for (i = n; i < n+m; i++){
//         scanf("%d", &nval[i]);
//     }
//     int m1[n+m], m2[n+m], cntr1=0,cntr2=0;
//     for (i = 0; i < n+m; i++){
//         if (nval[i]%5 == 0)
//             m1[cntr1] = nval[i];
//             cntr1++;
//     }
//     for (i = 0; i < n+m; i++){
//         if (nval[i]%5 != 0)
//             m2[cntr2] = nval[i];
//             cntr2++;
//     }
//     sort(n+m, m1[n+m]);
//     sort(n+m, m2[n+m]); 
// }


// C++ implementation to print circle pattern
#include <bits/stdc++.h>
using namespace std;
void printPattern(int radius) {
  float dist;
  for (int i = 0; i <= 2 * radius; i++) {
    for (int j = 0; j <= 2 * radius; j++) {
      dist = sqrt((i - radius) * (i - radius) +
                  (j - radius) * (j - radius));
      if (dist > radius - 0.5 && dist < radius + 0.5)
        cout << "*";
      else
        cout << " ";     
    }
    cout << "\n";
  }
}
int main() {
  int radius = 6;
  printPattern(radius);
  return 0;
  int i, j, N=5;
    for(i=1; i<=N; i++){
        for(j=1; j<=N; j++){
            printf("^");
        }
        printf("\n");
    }
    return 0;
}