# Multi-Objective Recommendation Ranking Model Optimization
# Use linear regression to complete optimization of multi-objective recommendation ranking model
# Shared feature weights, retain task-specific bias terms
# Use joint loss function: loss = MSE_ctr + alpha * MSE_cvr
# Weights and biases start from 0

# Return final loss value, magnified 1e10 times and rounded to nearest integer output

# The sample for this question is problematic!

def parse_matrix(line: str):
    # parse "1,2; 3,4" to [[1,2],[3,4]]
    rows = line.strip().split(';')
    matrix = []
    for row in rows:
        matrix.append([float(x) for x in row.split(',')])
    return matrix

def train_and_loss(X, y, iters, lr, alpha):
    # For feature matrix X
    # n = sample count
    # d = feature dimension
    n = len(X)
    d = len(X[0])

    # Initialize: weight size consistent with feature dimension
    weights = [0.0] * d
    # Bias terms for ctr and cvr
    b_ctr = 0.0 
    b_cvr = 0.0

    for _ in range(iters): # Iteration
        # 1. Calculate current prediction and error
        e_ctr = []
        e_cvr = []
        for i in range(n): # For each sample
            # Sum, feature weight x feature value
            shared_sum = sum(weights[j] * X[i][j] for j in range(d))
            e_ctr.append(shared_sum + b_ctr - y[i][0]) # Predicted value - True value
            e_cvr.append(shared_sum + b_cvr - y[i][1])

        # 2. Calculate gradient
        # Gradient shape consistent with variable
        # e = sum((y_pred - y_true)^2)/n
        # de/dw = 2/n * sum((y_pred - y_true) * x_i)
        # de/dw = 2/n * sum(e_i * x_i)
        grad_w = [0.0] * d
        for j in range(d):
            sum_w = 0.0
            for i in range(n):
                sum_w += (e_ctr[i] * X[i][j] + alpha * e_cvr[i] * X[i][j])
            # Multiply by 2/n after sum
            grad_w[j] = (2.0 / n) * sum_w
        
        # Gradient for bias term, 2/n * sum(e_i) * 1
        grad_b_ctr = (2.0 / n) * sum(e_ctr)
        # --- Add alpha ---
        grad_b_cvr = alpha * (2.0 / n) * sum(e_cvr) 

        # 3. Update parameters
        for j in range(d): # Update weights
            weights[j] -= lr * grad_w[j]
        b_ctr -= lr * grad_b_ctr
        b_cvr -= lr * grad_b_cvr
    
    # Final Loss calculation
    final_mse_ctr = 0.0
    final_mse_cvr = 0.0
    for i in range(n):
        shared_sum = sum(weights[j] * X[i][j] for j in range(d))
        final_mse_ctr += (shared_sum + b_ctr - y[i][0]) ** 2
        final_mse_cvr += (shared_sum + b_cvr - y[i][1]) ** 2
    
    total_loss = (final_mse_ctr / n) + alpha * (final_mse_cvr / n)
    return total_loss


def main():
    # Read X
    X_line = input()
    X = parse_matrix(X_line)
    # Read y
    y_line = input()
    y = parse_matrix(y_line)
    # Read iteration count, learning rate, alpha
    iters = int(input())
    lr = float(input())
    alpha = float(input())

    loss = train_and_loss(X, y, iters, lr, alpha)
    print(round(loss * 1e10))

if __name__ == "__main__":
    main()