# Intelligent Customer Segmentation and New User Positioning (Balanced K-Means Version)

# Use a variant of K-means clustering to divide users into k groups, ensuring that the number of people in each group differs by no more than 1
# When the number of people cannot be evenly divided, distribute the extra customers to groups with smaller cluster center IDs, assigning uniquely
# For new customer data, use the final cluster centers to assign a suitable group

# Input: N customers, each with M features
# Number of groups, (2 <= k <= min(20, N))
# Initial cluster centers: the first k customers of the input
# Clustering algorithm flow:
# 1. Process each customer in the order of input
# 2. Calculate the Euclidean distance between the customer and each cluster center, select the nearest cluster center; if distances are equal, select the one with the smallest ID
# 3. Check if the group corresponding to that cluster center has reached its capacity limit. If not, assign to that group; if yes, select the next nearest cluster center, repeat step 3
# 4. Excess customers are assigned to groups with smaller IDs
# 5. After the first round of allocation, update the cluster centers to the mean of customers in each group (rounded down)
# 6. Repeat steps 1-5 until the cluster centers no longer change

# Given data for a new customer


# Output feature values for each center point
# Output group ID for the new user (starting from 1)

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return sum((a[i] - b[i]) ** 2 for i in range(m))

# Update cluster centers
def update_centers(groups):
    new_centers = []
    for group in groups:
        new_center = [sum(customer[j] for customer in group) // len(group) for j in range(m)]
        new_centers.append(new_center)
    return new_centers

# Return the index of the closest group
def find_closest_groups(customer, centers, groups):
    distances = [(euclidean_distance(customer, centers[j]), j) for j in range(len(centers))]
    # Sort by distance accumulating, then by ID ascending
    distances.sort(key=lambda x: (x[0], x[1]))
    for _, group_idx in distances:
        if len(groups[group_idx]) < MAX_SIZE[group_idx]:
            return group_idx
    # All full
    return distances[0][1]

# First line, N, M, k
n, m, k = map(int, input().strip().split())
# Read customer data
data = [list(map(int, input().strip().split())) for _ in range(n)]
# Read new customer data
new_customer = list(map(int, input().strip().split()))

if n < k:
    k = n

# Set maximum capacity for each group
MAX_SIZE = [n // k] * k
for i in range(n % k):
    MAX_SIZE[i] += 1

groups = []
for i in range(k):
    groups.append([data[i]])  # Initialize each group, put in initial center point

# Initialize cluster centers
centers = data[:k]

# First round
for i in range(k, n):
    customer = data[i]
    group_id = find_closest_groups(customer, centers, groups)
    groups[group_id].append(customer)

# Iteratively update cluster centers and assign groups
while True:
    new_centers = update_centers(groups)
    if new_centers == centers:
        break
    centers = new_centers
    # Clear groups, reassign
    groups = [[] for _ in range(k)]
    for i in range(n):
        customer = data[i]
        group_id = find_closest_groups(customer, centers, groups)
        groups[group_id].append(customer)

# Sort final groups by cluster centers
centers.sort()
# Output final cluster centers
for center in centers:
    print(' '.join(map(str, center)))

# Assign new customer, calculate directly
_, new_group_id = min((euclidean_distance(new_customer, centers[j]), j) for j in range(k))
print(new_group_id + 1)