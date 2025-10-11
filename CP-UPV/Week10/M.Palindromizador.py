if __name__ == "__main__":

    n = int(input())

    for _ in range(n):

        seq = input()
        normalized = []
        mapping = []


        for idx, char in enumerate(seq):

            if char != " ":
                normalized.append(char.lower())
                mapping.append(idx)
        
        normalizedSeq = "".join(normalized)
        lengthSeq = len(normalizedSeq)

        if lengthSeq == 0:
            print(seq.strip())
            continue

        dp = [[False] * lengthSeq for _ in range(lengthSeq)]
        max_length = 0
        best_sub = seq[mapping[0]:mapping[0] + 1]

        for i in range(lengthSeq):
            dp[i][i] = True

            if max_length < 1:
                max_length = 1
                best_sub = seq[mapping[i]:mapping[i]+1]

        for length in range(2, lengthSeq+1):

            for i in range(lengthSeq-length+1):
                j = i + length - 1
                toCompare = normalizedSeq[j]
                originalChar = normalizedSeq[i]

                if originalChar == toCompare:

                    if length == 2 or dp[i+1][j-1]:

                        dp[i][j] = True
                        orig_i, orig_j = mapping[i], mapping[j]
                        candidate = seq[orig_i:orig_j + 1]

                        if length > max_length:
                            max_length = length
                            best_sub = candidate
                        elif length == max_length and candidate < best_sub:
                            best_sub = candidate
                            
        print(best_sub.strip())