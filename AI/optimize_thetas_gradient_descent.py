import sys
import math
from decimal import Decimal, ROUND_HALF_UP


# Calculate U sequence for given thetas
# thetas: angle array
# r: radius
# space dimension k
# Can be halved for 1/4 circle

def build_U_from_thetas(thetas, r, k):
    sorted_thetas = sorted(thetas) # Ensure angles are ordered
    # Generate U sequence on [0, pi/4]
    U = [r * math.sin(t) for t in thetas]
    if k % 2 == 1:  # Odd dimension, add r / sqrt(2)
        U.append(r / math.sqrt(2.0))
    # Symmetric part, is reverse of U sequence, cos part
    U += [r * math.cos(t) for t in reversed(thetas)]
    return [0.0] + U + [r] # Add boundary


def objective(thetas, r, k):
    # Generate strips
    U_full = build_U_from_thetas(thetas, r, k)
    s = 0.0 # 1/4 area
    # i in [1, K+1] # Rectangle upper boundary
    for i in range(1, k + 2):
        # x is x coordinate corresponding to angle[i-1]
        # i - 1 + x = k + 1 -> x = k - i + 2
        dy = U_full[i] - U_full[i - 1]
        x_cap = U_full[k - i + 2]
        s += dy * x_cap
    return 4.0 * s # Multiply by 4 to get full area

# Gradient descent optimization
from scipy.optimize import minimize

def optimize_thetas(M):

    if M == 1:
        return  1 # Corver entire pixel area
    r = 0.5
    k = (M - 1) // 2
    p = k // 2

    # Initialize thetas
    thetas = [ (i + 1) * (math.pi / 4.0) / (p + 1) for i in range(p) ]

    # Gradient descent
    # Increase Scipy precision in optimize_thetas
    res = minimize(lambda th: objective(th, r, k), thetas, method='L-BFGS-B',
                bounds=[(0.0, math.pi / 4.0)] * p,
                options={'ftol': 1e-16, 'gtol': 1e-16, 'maxiter': 20000})
    # Parameter meaning
    # minimize is minimization function, objective itself is to minimize area
    # thetas is initial point
    # method is optimization method
    # bounds is value range for each parameter
    # options is optimization options: ftol is function value convergence threshold, gtol is gradient convergence threshold, maxiter is max iterations
    # Returned res contains optimization result
    return objective(res.x, r, k)

# If implementing gradient descent manually, can refer to following code
def gradient_descent(thetas, r, k, learning_rate=0.01, max_iter=10000, tol=1e-8):
    p = len(thetas)
    for iteration in range(max_iter):
        grad = [0.0] * p
        # Calculate gradient: Central difference method
        for i in range(p):
            delta = 1e-8 # Tiny change
            thetas_plus = thetas[:] # Copy
            thetas_minus = thetas[:] # Copy
            thetas_plus[i] += delta # Tiny increase 
            thetas_minus[i] -= delta # Tiny decrease
            f_plus = objective(thetas_plus, r, k) # Calculate objective function value
            f_minus = objective(thetas_minus, r, k) # Calculate objective function value
            grad[i] = (f_plus - f_minus) / (2 * delta) # Central difference method to calculate gradient
        # Update parameters
        max_change = 0.0 # Record max change among all parameters
        for i in range(p):
            change = learning_rate * grad[i]
            thetas[i] -= change # Gradient descent update
            max_change = max(max_change, abs(change)) # Record max change
        # Check convergence
        if max_change < tol:
            break
    return objective(thetas, r, k)
    


def main():
    M = int(sys.stdin.readline().strip())
    # ans = optimize_thetas(M)
    # Manual gradient descent
    if M == 1:
        ans = 1.0
    else:
        r = 0.5
        k = (M - 1) // 2
        p = k // 2
        thetas = [ (i + 1) * (math.pi / 4.0) / (p + 1) for i in range(p) ]
        ans = gradient_descent(thetas, r, k, learning_rate=0.01, max_iter=20000, tol=1e-16)
    out = Decimal(str(ans)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
    print(out)

if __name__ == "__main__":
    main()
