'''
Docstring for Group-C.78-约瑟夫问题

一个随机数组成的数组，初始长度 m
从数列首位开始计数，计数到 m 后，令 m = 数值处的数值，并将该位置的数删除
从下一个位置重新开始计数，直到所有数值都被替换出 -> 数组为空
计数达到末尾，从头开始继续计数

输出数组被删除数值的顺序

'''

def array_iterate(n: int, input_array: list, m: int) -> list:
    result = []
    index = 0

    while input_array:
        # 从当前位置开始，数 m 个位置（计数从1开始，所以是 m-1 步）
        index = (index + m - 1) % len(input_array)
        # 获取该位置的值，更新 m，并删除该元素
        m = input_array.pop(index)
        result.append(m)
        # 删除后，如果 index 超出数组长度，需要调整到开头
        # 注意：pop 后如果 index == len(input_array)，说明删除的是最后一个元素
        # 下一次应该从头开始，所以 index 保持不变会在下次取模时自动处理
        if index >= len(input_array) and input_array:
            index = 0

    return result

if __name__ == "__main__":
    input_array = [3, 1, 2, 4]
    len_input_array = len(input_array)
    m = 7 # 是一个输入值

    output_array = array_iterate(len_input_array, input_array, m)
    print(output_array)