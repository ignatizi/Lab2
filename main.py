def Prostoe(a):

    if a>100000:

        return print("Eror")
    if a<0:

        return print("Eror")

    if a < 2:
         return False
    if a == 2:
        return True
    limit = a**(1/2)
    i=2
    while i<=limit:
        if a%i == 0:
            return False
        i +=1
    return True

print(Prostoe(int(input("a= "))))

def funNew(fn, dfn, x, tol, maxiter):
    for i in range(maxiter):
        xnew = x - fn(x)/dfn(x)
        if abs(xnew - x) < tol: break
        x = xnew
    print(xnew, i)

y = lambda x: 2*x**3 - 9.5*x +7.5
dy = lambda x: 6*x**2 - 9.5

funNew(y, dy, 5, 0.0001, 100)