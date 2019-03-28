def climbing_leader_board(scores, alice):
    alice_count = len(alice)
    scores = list(set(scores))
    scores.sort(reverse=True)
    scores_count = len(scores)
    result = []
    for i in range(0, alice_count):
        for j in range(0, scores_count):
            if alice[i] == scores[j]:
                result.append(j + 1)
                break
            elif alice[i] > scores[0]:
                result.append(1)
                break
            elif alice[i] < scores[scores_count - 1]:
                result.append(len(scores) + 1)
                break
            elif scores[j] > alice[i] > scores[j + 1]:
                result.append(j + 2)
                break

    print(result)


climbing_leader_board([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
