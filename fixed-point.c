#include <stdio.h>

double function(double x){
	return x / 2.0 + 1 / x;
}

void fixed_point(double(*function)(double), double x, int n){
	for (int i = 0; i < n; i++){
		double xn = function(x);
		printf("%.16f\n", xn);
		x = xn;
	}
}

int main(){
	fixed_point(function, 1.678, 10);

	return 0;
}