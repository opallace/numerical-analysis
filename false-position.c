#include <stdio.h>
#include <math.h>

#define PI 3.14159265359

#define N 209448815
#define L (pow(10, -10) * 1.41)

double function(double x){
	return ((N + 1) / (1 + (N * exp(-L*(N+1)*x)))) - (N * 0.25);
}

double false_position(double(*function)(double), double a, double b, int n){
	double fa = function(a);
	double fb = function(b);

	if(fa * fb < 0){
		for (int i = 0; i < n; i++){
			double x = ((a * fb) - (b * fa)) / (fb - fa);
			printf("x_%i = %.16f\n", i+1, x);

			double fx = function(x);

			if(fx == 0){
				printf("FIND!\n");
				break;
			
			}else if(fa * fx < 0){
				b  = x;
				fb = fx;
			
			}else {
				a  = x;
				fa = fx;
			}
		}
	}
}

int main(){
	false_position(function, 0.0, 1298, 7);

	return 0;
}