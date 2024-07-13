s = input()
bomb = input()
result = ""
stack = []

for v in s:
    stack.append(v)
    if "".join(stack[- len(bomb):]) == bomb:
        for i in range(len(bomb)):
            stack.pop()

result = "".join(stack)
print(result if result else "FRULA")