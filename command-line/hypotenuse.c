/**
 * Created by Nate, 2025-4-24
 */

#include <math.h>

double hypotenuse(int a, int b)
{
	double c;

	c = sqrt(pow((double)a, 2) + pow((double)b, 2));
	return c;
}
