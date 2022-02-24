#include <stdio.h>
#include <math.h>

#define PI 3.14159265359

double function(double x){
	return ((2 * 49 * pow(x, 5/2))/5) + ((45600 * pow(x, 2))/2) - (81 * 9.81 * x) - (81 * 9.81 * 0.81);
}

double dfunction(double x){
	return (45600 * x) + (49 * pow(x, 3/2)) - 794.61;
}

void newton(double(*function)(double), double(*dfunction)(double), double x, int max_rounds){
	for (int i = 0; i < max_rounds; i++){
		double new_x = x - function(x) / dfunction(x);
		printf("x_%i = %.16f\n",i+1, new_x);
		x = new_x;
	}
}

int main(){
	newton(function, dfunction, 1.12, 6);

	return 0;
}