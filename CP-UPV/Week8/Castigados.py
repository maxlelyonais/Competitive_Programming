

if __name__ == "__main__":

    nQueries = int(input())
    accusations = input().split(" ")
    result = []

    for index in range(nQueries):

        visited = set()
        number = index

        while number not in visited:

            visited.add(number)
            number = int(accusations[number]) - 1

        result.append(str(number+1))

    print(" ".join(result))
        
        

