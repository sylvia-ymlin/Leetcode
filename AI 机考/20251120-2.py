# Vision Transformer中的Patch Embdding层实现

# 1. 将输入的图像分割为不重叠的patches
# 2. 将每个patch展开为一个向量
# 3. 使用线性变换对矩阵进行映射 Z = XE + b
# 4. 添加可学习的位置编码

def patch_embedding(imp_size, patch_size, channel, embedding_dim):
    # 默认长宽相等
    num_patches_per_side = imp_size // patch_size
    # X 的 shape
    num_patches = num_patches_per_side * num_patches_per_side
    # 添加一维 CLS_token
    x_shape = (num_patches + 1, patch_size * patch_size * channel)
    # E 的 shape
    e_shape = (patch_size * patch_size * channel, embedding_dim)
    # Z 的 shape
    z_shape = (num_patches + 1, embedding_dim)

    return z_shape



# 读入数据
imp_size, patch_size, channel, embedding_dim = map(int, input().strip().split())

# 输出 embedding shape
z_shape = patch_embedding(imp_size, patch_size, channel, embedding_dim)
print(f"{z_shape[0]} {z_shape[1]}")
