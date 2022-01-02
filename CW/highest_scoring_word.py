def high(x):
    mapping = {chr(i + 96): i for i in range(1, 27)}  # generate the dictionary mapping.
    x = x.lower().split(" ")  # Making the sentence lower case
    score = 0
    # location = 0
    results = {}
    for i in range(len(x)):
        for j in x[i]:
            score += mapping[j]
            results[i] = score
        score = 0
    print(results)
    # winner = max(zip(results.values(), results.keys()))[1]
    new_winner = 0
    new_score = 0
    for i in range(len(results)):
        if results[i] > new_score:
            new_score = results[i]
            new_winner = i
        else:
            pass


    return x[new_winner]


print(high('what time are we climbing up the volcano'))