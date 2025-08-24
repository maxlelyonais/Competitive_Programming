from collections import deque

if __name__ == "__main__":
    n = int(input())
    stack = deque()

    for _ in range(n):
        line = input().split()
        action = line[0]

        if action == "Depositan":
            libro = " ".join(line[1:])  
            stack.append(libro)
        elif action == "Retiran":
            if stack:
                stack.pop()

    # Output final
    if not stack:
        print("No quedan libros")
    else:
        while stack:
            print(stack.pop())
