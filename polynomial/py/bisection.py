def y(x):
    y = pow(x,2) - x - 1
    return y


def bisection(y,a,b,N):
    l = 0
    x = a
    while l < N:
        if (y(a) * y(b) < 0):
            x = (a+b)/2
            print(x)
            if(y(a)*y(x) < 0):
                b = x
                x = (a+x)/2
                print(x)
            else:
                a = x
                x = (b+x)/2
                print(x)
        else:
            print("Wrong Range.")
            return
        l = l + 1
    return x

bisection(y,0,5,25)