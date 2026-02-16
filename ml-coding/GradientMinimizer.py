# manually implement gradient descent optimizer

def gradient_descent(f, x0, lr=0.01, max_steps=1000, eps=1e-8):
    x = x0
    for _ in range(max_steps):
        # approximate gradient using finite difference
        grad = (f(x + eps) - f(x - eps)) / (2 * eps)

        x_new = x - lr * grad

        if abs(f(x_new) - f(x)) < eps: # converge
            break

        x = x_new
    
    return x, f(x)
