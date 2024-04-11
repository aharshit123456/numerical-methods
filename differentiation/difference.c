#include <stdio.h>
#include <math.h>

float f(float x)
{
    return (pow(x, 2) - x - 1);
}

float forward_diff(float a, float h)
{
    return (f(a + h) - f(a)) / (h);
}

float backward_diff(float a, float h)
{
    return (f(a) - f(a - h)) / (h);
}

float central_diff(float a, float h)
{
    return (f(a + h) - f(a - h)) / (2 * h);
}

void main()
{
    printf("%f \n", (f(3.0)));
    printf("%f \n", (forward_diff(3.0, 0.001)));
    printf("%f \n", (backward_diff(3.0, 0.001)));
    printf("%f \n", (central_diff(3.0, 0.001)));
}