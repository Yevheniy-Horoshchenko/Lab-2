import math
def f(x):
    return 6*x**4-4*x**3-x**2+x-7
def df(x):
    return 24*x**3-12*x**2-2*x+1
def ddf(x):
    return 72*x**2-24*x-2
def new(a,b,e):
    if f(b)*ddf(b)>0:
        x=b
    else:
        x=a
    h=f(x)/df(x)
    x=x-h
    while abs(h)>=e:
         h=f(x)/df(x)
         x=x-h
    print(x)
    return x
print (new(-2,-0.3,0.0001))
def comb(a,b,eps):
    if df(a)*ddf(a)<0:
        a0=a
        b0=b
    else:
        a0=b
        b0=a
    a_n=a-f(a)*(b-a)/(f(b)-f(a))
    b_n=b-f(b)/df(b)
    while b_n-a_n>eps:
        a_n=a-f(a)*(b-a)/(f(b)-f(a))
        b_n=b-f(b)/df(b)
    x=(b+a)/2
    print(x)
    return x
comb(-2,-0.3,0.0001)