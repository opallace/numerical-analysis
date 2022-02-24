#include <stdio.h>
#include <math.h>

#define PI 3.14159265359

double function(double x){
	return ((2 * 49 * pow(x, 5/2))/5) + ((45600 * pow(x, 2))/2) - (81 * 9.81 * x) - (81 * 9.81 * 0.81);
}

void secante(double(*function)(double), double x, double xx, int max_rounds){
	for (int i = 0; i < max_rounds; i++){

		double fxx = function(xx);
		double fx  = function(x);

		if(fxx == fx){
			return;
		}

		double new_x = ((x * fxx) - (xx * fx)) / (fxx - fx);
		
		printf("%.12lf\n", new_x);

		x = xx;
		xx = new_x;
	}
}

int main(){
	secante(function, 0.84, 1.89, 8);

	return 0;
}

