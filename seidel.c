#include <stdio.h>

#define ROWS 4
#define COLS 4

void seidel(double a[ROWS][COLS], double b[COLS], double chute[COLS], int n){
	for (int it = 0; it < n; it++){
		for (int i = 0; i < ROWS; i++){
			double xi = b[i];

			for (int j = 0; j < COLS; ++j){
				if(i != j){
					xi -= a[i][j] * chute[j];
				}
			}

			xi /= a[i][i];
			chute[i] = xi;
			
		}

		printf("X^(%i)", it + 1);
		for(int k = 0; k < COLS; k++){
			printf("%.10f\t", chute[k]);
		}

		printf("\n");
		
	}
}



int main(){

	double a[ROWS][COLS] = {{-9.04088, -4.33547, 0.12958, -2.85899}, {-0.83174, -4.32457, 1.23839, -0.53759}, {2.99565, 1.61637, 11.29034, 4.96148}, {2.7656, 4.40308, -0.93959, -9.82511}};
	double b[ROWS] = {-3.07706, 2.18921, -4.86819, 3.60354};

	double chute[COLS] = {-2.56707, -1.26515, 2.78851, 4.93766};
	int n = 16;

	seidel(a, b, chute, n);

	return 0;
}