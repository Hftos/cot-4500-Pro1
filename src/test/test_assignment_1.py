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



def main():
    print("Running Square Root Approximation Algorithm:")
    sqrt_root = approximate_sqrt_two()
    print(f"Approximated square root of 2: {sqrt_root}\n")

    print("Running Bisection Method Algorithm:")
    def f(x):
        return x**2 - 2

    
    left = 1
    right = 2

    root = bisection_method(f, left, right)
    print(f"Approximate root of f(x) = x^2 - 2: {root}")

if __name__ == "__main__":
    main()