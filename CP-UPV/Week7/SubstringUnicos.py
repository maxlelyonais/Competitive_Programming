from collections import deque

if __name__ == "__main__":

    letters = list(input())
    length = int(input())
    stack = deque()
    result = set()
    index = 0

    if len(letters) < length:
        print(0)
    else:
        for _ in range(length):
            stack.append(letters[index])
            index+=1

        result.add("".join(stack))

        while index < len(letters):
            stack.popleft()
            stack.append(letters[index])
            result.add("".join(stack))
            index+=1

        print(len(result))





