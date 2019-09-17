#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int i, j, n, soma[3], vet1[3], vet2[3];
	for(i=0; i<3; i++){
		scanf("%d", &vet1[i]);
	}
	for(i=0; i<3; i++){
		scanf("%d", &vet2[i]);
	}	
	for(i=0; i<3; i++){
		soma[i]=vet1[i]+vet2[i];
	}
	for (j=2; j>0; j--){
		for(i=0; i<3; i++){
			if(soma[i]>soma[i+1]){
				j=soma[i];
				soma[i]=soma[i+1];
				soma[i+1]=j;
			}
		}
	}
	for(i=0; i<3; i++){
		printf("%d", soma[i]);
	}
}
