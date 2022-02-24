#include <stdio.h>
#include <math.h>

#define N 209448815
#define L (pow(10, -10) * 1.41)

double function(double x){
	return ((N + 1) / (1 + (N * exp(-L*(N+1)*x)))) - (N * 0.25);
}

void bisection(double(*function)(double), double a, double b, int max_rounds){
	if(max_rounds > 0){
		if(function(a) * function(b) >= 0){
			printf("Error!\n");
			return;

		}else {
			double c = (a + b) / 2;
			printf("%.16f\n", c);

			if(function(c) == 0){
				return;
			}else {

				if(function(a) * function(c) < 0){
					bisection(function, a, c, --max_rounds);
			
				}else if(function(c) * function(b) < 0){
					bisection(function, c, b, --max_rounds);
			
				}

			}
		}
	}
}

int main(){

	bisection(function, 0, 1298, 12);

	return 0;
}