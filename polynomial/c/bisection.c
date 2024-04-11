#include <stdio.h>
#include <math.h>

float y(float x)
{
    return (pow(x, 2) - x - 1);
}

float bisection(float a, float b, int N)
{
    float x = a;
    for (int i = 0; i < N; i++)
    {
        if (y(a) * y(b) < 0)
        {
            x = (a + b) / 2;
            // printf("%f \n", x);
            if (y(a) * y(x) < 0)
            {
                b = x;
                x = (a + x) / 2;
                // printf("%f \n", x);
            }
            else
            {
                a = x;
                x = (b + x) / 2;
                // printf("%f \n", x);
            }
        }
        else
        {
            printf("Wrong range");
        }
    }
    return x;
}

float secant(float a, float b, int N)
{
    float x = a;
    for (int i = 0; i < N; i++)
    {
        if (y(a) * y(b) < 0)
        {
            x = a - (y(a) * (b - a) / (y(b) - y(a)));
            // printf("%f \n", x);
            if (y(a) * y(x) < 0)
            {
                b = x;
                x = a - (y(a) * (b - a) / (y(b) - y(a)));
                // printf("%f \n", x);
            }
            else
            {
                a = x;
                x = a - (y(a) * (b - a) / (y(b) - y(a)));
                // printf("%f \n", x);
            }
        }
        else
        {
            printf("Wrong range");
        }
    }
    return x;
}

void main()
{

    printf("The root of the equation is %f \n", bisection(0.0, 5.0, 50));
    printf("The root of the equation is %f \n", secant(0.0, 5.0, 50));
}