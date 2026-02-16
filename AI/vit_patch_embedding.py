# Vision Transformer Patch Embedding Layer Implementation

# 1. Split input image into non-overlapping patches
# 2. Flatten each patch into a vector
# 3. Map the matrix using linear transformation Z = XE + b
# 4. Add learnable position encoding

def patch_embedding(imp_size, patch_size, channel, embedding_dim):
    # Default length and width are equal
    num_patches_per_side = imp_size // patch_size
    # Shape of X
    num_patches = num_patches_per_side * num_patches_per_side
    # Add 1D CLS_token
    x_shape = (num_patches + 1, patch_size * patch_size * channel)
    # Shape of E
    e_shape = (patch_size * patch_size * channel, embedding_dim)
    # Shape of Z
    z_shape = (num_patches + 1, embedding_dim)

    return z_shape



# Read data
imp_size, patch_size, channel, embedding_dim = map(int, input().strip().split())

# Output embedding shape
z_shape = patch_embedding(imp_size, patch_size, channel, embedding_dim)
print(f"{z_shape[0]} {z_shape[1]}")
