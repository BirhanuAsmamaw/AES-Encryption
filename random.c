#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define KEYSIZE 16
void main() {
int i;
char key[KEYSIZE];

for (int j =1524020929-7200; j <= 1524020929; j++) {
    srand(j);   
    for (i = 0; i< KEYSIZE; i++){
    key[i] = rand()%256;
    // printf("%d", key[i]);
    printf("%.2x", (unsigned char)key[i]);
} 
    printf(",%d", j);
    printf("\n");

}


}