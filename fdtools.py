import numpy

def cosspace(a, b, n=50):
    return (a + b)/2 + (b - a)/2 * (numpy.cos(numpy.linspace(-numpy.pi, 0, n)))

def vander_chebyshev(x, n=None):
    if n is None:
        n = len(x)
    T = numpy.ones((len(x), n))
    if n > 1:
        T[:,1] = x
    for k in range(2,n):
        T[:,k] = 2 * x * T[:,k-1] - T[:,k-2]
    return T

def chebeval(z, n=None):
    """Build matrices to evaluate the n-term Chebyshev expansion and its derivatives at point(s) z"""
    z = numpy.array(z, ndmin=1)
    if n is None:
        n = len(z)
    Tz = vander_chebyshev(z, n)
    dTz = numpy.zeros_like(Tz)
    dTz[:,1] = 1
    dTz[:,2] = 4*z
    ddTz = numpy.zeros_like(Tz)
    ddTz[:,2] = 4
    for n in range(3,n):
        dTz[:,n]  = n * (2*Tz[:,n-1] + dTz[:,n-2]/(n-2))
        ddTz[:,n] = n * (2*dTz[:,n-1] + ddTz[:,n-2]/(n-2))
    return [Tz, dTz, ddTz]

def fdstencilV(z, x):
    """Compute finite difference weights using a Vandermonde matrix"""
    x = numpy.array(x)
    V = numpy.vander(x - z, increasing=True)
    scaling = numpy.array([numpy.math.factorial(i) for i in range(len(x))])
    return (numpy.linalg.inv(V).T * scaling).T

def fdstencil(z, x, nderiv=None):
    """Compute finite difference weights using recurrences for Lagrange polynomials (see Fornberg 1998)"""
    if nderiv is None:
        nderiv = len(x)
    x = numpy.array(x) - z
    k = numpy.arange(nderiv+1)
    c = numpy.outer(0.*k, x)
    c[0,0] = 1
    prod = 1
    for j in range(1,len(x)):
        dx = x[j] - x[:j]
        c[1:,j] = x[j-1]*c[1:,j-1] - k[1:]*c[:-1,j-1]
        c[0,j] = x[j-1]*c[0,j-1]
        c[:,j] *= -prod
        prod = numpy.prod(dx)
        c[:,j] /= prod
        c[1:,:j] = (x[j]*c[1:,:j] - k[1:,None]*c[:-1,:j]) / dx
        c[0,:j]  =  x[j]*c[0,:j] / dx
    return c

def fdcompact(z, x, k):
    """Compute a compact (implicit) differencing scheme

         b @ u^(k)(z) = c @ u(x)

       that maximizes the accuracy of u^(k)(z[0])."""
    z = numpy.array(z)
    x = numpy.array(x)
    n = len(x)
    x = x - z[0]
    z = z - z[0]
    xmin, xmax = min(x), max(x)
    dx = (xmax - xmin) / (n - 1)
    y = numpy.zeros(n + len(z) - 1)
    y[:n] = x
    for i in range(1, len(z)):
        if (z[i] < 0):
            xmin -= dx
            y[n + i - 1] = xmin
        else:
            xmax += dx
            y[n + i - 1] = xmax
    S = numpy.array([fdstencil(t, y, k)[k] for t in z])
    b = numpy.ones(len(z))
    T = S[1:,n:].T
    b[1:] = numpy.linalg.lstsq(T, -S[0,n:])[0]
    c = b.dot(S[:,:n])
    return b, c

def dispersion(z, x, b, c):
    from matplotlib import pyplot
    theta = numpy.linspace(0, numpy.pi, 100)[1:]
    phiz = numpy.exp(1j*numpy.outer(z, theta))
    phix = numpy.exp(1j*numpy.outer(x, theta))
    pyplot.plot(theta, (c.dot(phix) / b.dot(phiz)).imag, '.')
    pyplot.plot(theta, theta)
    pyplot.plot(theta, numpy.sin(theta))
    pyplot.show()

def rk_butcher_4():
    A = numpy.array([[0,0,0,0],[.5,0,0,0],[0,.5,0,0],[0,0,1,0]])
    b = numpy.array([1/6, 1/3, 1/3, 1/6])
    return A, b

def rk_butcher_ssp32():
    A = numpy.array([[0, 0, 0],
                     [1/2, 0, 0],
                     [1/2, 1/2, 0]])
    b = numpy.array([1/3, 1/3, 1/3])
    return A, b

def ode_rkexplicit(f, u0, butcher=None, tfinal=1, h=.1):
    if butcher is None:
        A, b = rk_butcher_4()
    else:
        A, b = butcher
    c = numpy.sum(A, axis=1)
    s = len(c)
    u = u0.copy()
    t = 0
    hist = [(t,u0)]
    while t < tfinal:
        if tfinal - t < 1.01*h:
            h = tfinal - t
            tnext = tfinal
        else:
            tnext = t + h
        h = min(h, tfinal - t)
        fY = numpy.zeros((len(u0), s))
        for i in range(s):
            Yi = u.copy()
            for j in range(i):
                Yi += h * A[i,j] * fY[:,j]
            fY[:,i] = f(t + h*c[i], Yi)
        u += h * fY.dot(b)
        t = tnext
        hist.append((t, u.copy()))
    return hist
