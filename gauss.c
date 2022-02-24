#include <stdio.h>

#define L 4
#define C 5

void print_matrix(double array[L][C]){
	for (int i = 0; i < L; ++i){
		for (int j = 0; j < C; ++j){
			printf("%.16lf\t ", array[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void gauss(double E[L][C]){
	for (int j = 0; j < C - 2; ++j){
		for (int i = j; j < L; ++i){
			if(E[i][j] != 0){
				if(i != j){
					//aqui é preciso trocar as linhas Li por Lj
					double temp;
					for (int k = 0; k < C; ++k){
						temp = E[i][k];
						E[i][k] = E[j][k];
						E[j][k] = temp;
					}
				}
				// o pivo (elemento ij de E) é não nulo
				// aqui vamos executar as operações em linha

				for (int m = j + 1; m < L; ++m){
					double a = -E[m][j] / E[j][j];
					for (int n = j; n < C; ++n){
						E[m][n] += a * E[j][n];
						printf("ESSEEEE %.16f\n", a);
					}
				}

				print_matrix(E);

				break;

			}else {
				if(i == L - 1){
					printf("Esse sistema não possui solução\n");
				}
			}
		}
		
	}
}

void reverse_substitution(double E[L][C]){
	double answer[L];
	for (int i = 0; i < L; ++i){
		int d = L - 1 - i;
		double b = E[d][C - 1];

		for (int j = d + 1; j < C - 1; ++j){
			b -= E[d][j] * answer[j];
		}

		double xd = b / E[d][d];

		answer[d] = xd;

		printf("x_%d = %.16f\n", d + 1, xd);
	}

}

int main(){
	
	double E[L][C] = {{-2, 5, -2, -1,0}, {5, 2, -1, -5,0}, {2, -5, -1, 4,0}, {2, -5, 1, -3,0}};


	print_matrix(E);
	gauss(E);
	print_matrix(E);

	return 0;
}