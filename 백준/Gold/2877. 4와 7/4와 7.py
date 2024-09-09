K = int(input())
binary = format(K + 1, 'b')
binary = binary[1:]
print(binary.replace('0', '4').replace('1', '7'))