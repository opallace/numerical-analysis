#include <stdio.h>

#define ROWS 4
#define COLS 4

void jacobi(double a[ROWS][COLS], double b[COLS], double chute[COLS], int n){
	for (int it = 0; it < n; it++){
		
		double temp[COLS] = {}; 

		for (int i = 0; i < ROWS; i++){
			double xi = b[i];

			for (int j = 0; j < COLS; ++j){
				if(i != j){
					xi -= a[i][j] * chute[j];
				}
			}

			xi /= a[i][i];
			temp[i] = xi;
			
		}

		printf("X^(%i)", it + 1);
		for(int k = 0; k < COLS; k++){
			chute[k] = temp[k];
			printf("%.10f\t", chute[k]);
		}

		printf("\n");
		
	}
}



int main(){

	double a[ROWS][COLS] = {{-10.79, 1.35, 3.81, -4.47}, {0.52, -5.83, 1.23, 2.92}, {-4.56, -1.37, 12.02, -4.94}, {-3.32, 2.86, -1.87, 9.2}};
	double b[ROWS] = {-4.79, -1.29, 3.6, -3.22};

	double chute[COLS] = {4.36, -0.08, 2.18, 0.19};
	int n = 16;

	jacobi(a, b, chute, n);

	return 0;
}