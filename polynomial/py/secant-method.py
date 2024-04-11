from bisection import bisection

def y(x):
    y = pow(x,2) - x - 1
    return y


def secant(y,a,b,N):
    l = 0
    x = a
    while l < N:
        if (y(a) * y(b) < 0):
            x = a-(y(a)*(b-a)/(y(b)-y(a)))
            print(x)
            if(y(a)*y(x) < 0):
                b = x
                x = a-(y(a)*(b-a)/(y(b)-y(a)))
                print(x)
            else:
                a = x
                x = a-(y(a)*(b-a)/(y(b)-y(a)))
                print(x)
        else:
            print("Wrong Range.")
            return
        l = l + 1
    return x


print("Solving by Secant Method")
secant(y,0,5,25)
print("Solving by Bisection Method")
bisection(y,0,5,25)