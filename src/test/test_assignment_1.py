def approximate_sqrt_two():
    x0 = 1.5
    tol = 0.000001
    iter = 0 
    diff = x0
    x = x0

    print(f"{iter} : {x}")

    while diff >= tol:
        iter += 1
        y = x

        x = (x/2)+(1/x)
        print(f"{iter} : {x}")

        diff = abs(x-y)
    
    print(f"\nConvergence after {iter} iterations.")
    return x

def bisection_method(f,left,right,tol=1e-6, max_iter=100):
    iter_count = 0

    while(right - left)/2 > tol and iter_count < max_iter:
        iter_count += 1
        midpoint = (left+right)/2

        if f(midpoint) == 2:
            return midpoint
        elif f(left) * f(midpoint) < 0:
            right = midpoint
        else:
            left = midpoint
    return (left+right)/2.0

def fixed_point_iteration(g, p0, tol=1e-6, max_iter = 100):
    i = 1
    while i <= max_iter:
        p = g(p0)
        if abs(p - p0) < tol:
            print(f"SUCCESS: p = {p}")
            return p
        i += 1
        p0=p
    print("FAIL")
    return None

def Newton_method(f, f_prime, p0, tol=1e-6, max_iter = 100):
    i = 1
    while i <= max_iter:
        if f_prime(p0) != 0:
            p_next = p0 - f(p0) / f_prime(p0)
            if abs(p_next - p0) < tol:
                print(f"SUCCESS: p_next = {p_next}")
                return p_next
            i += 1
            p0 = p_next
        else:
            print("UNSUCCESSFUL: Derivative is 0")
            return None
    
    print("UNSUCCESSFUL: max iter reached")
    return None

def main():
    # Square Root approx
    print("Running Square Root Approximation algorithm:")
    sqrt_root = approximate_sqrt_two()
    print(f"Approximated square root of 2: {sqrt_root}\n")

    # Bisection method
    print("Running Bisection algorithm:")
    def f(x):
        return x**2 - 2
    
    left = 1
    right = 2

    root = bisection_method(f, left, right)
    print(f"Approximate root of f(x) = x^2 - 2: {root}")

    # Fixed-Point
    print("Running Fixed-Point algorithm:")
    def g(x):
        return (x+2/x)/2
    
    # Initial approx
    p0 = 1.5

    fixed_point = fixed_point_iteration(g, p0)
    if fixed_point is not None:
        print(f"Fixed point: {fixed_point}")
    
    # Newton Method
    print("Running Newton's Method Algorithm:")
    def f_newton(x):
        return x**2 - 2

    def f_prime(x):
        return 2 * x

    p0_newton = 1.5

    newton_root = Newton_method(f_newton, f_prime, p0_newton)
    if newton_root is not None:
        print(f"Root found using Newton's Method: {newton_root}")

if __name__ == "__main__":
    main()