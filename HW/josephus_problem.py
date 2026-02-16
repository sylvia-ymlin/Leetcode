'''
Docstring for Group-C.78-Josephus Problem

An array of random numbers, initial length m
Start counting from the first position of the sequence. When counting reaching m, let m = value at current position, and remove the number at this position.
Restart counting from the next position until all numbers are replaced/removed -> array is empty.
If counting reaches the end, continue counting from the beginning.

Output the order of removed numbers from the array.

'''

def array_iterate(n: int, input_array: list, m: int) -> list:
    result = []
    index = 0

    while input_array:
        # Count m positions starting from current position (counting starts from 1, so move m-1 steps)
        index = (index + m - 1) % len(input_array)
        # Get value at position, update m, and remove element
        m = input_array.pop(index)
        result.append(m)
        # After removal, if index exceeds array length, need to adjust to beginning
        # Note: If pop removes the last element, index == len(input_array)
        # Next time should start from beginning, so keeping index as is will be handled by modulo next time
        if index >= len(input_array) and input_array:
            index = 0

    return result

if __name__ == "__main__":
    input_array = [3, 1, 2, 4]
    len_input_array = len(input_array)
    m = 7 # Input value

    output_array = array_iterate(len_input_array, input_array, m)
    print(output_array)