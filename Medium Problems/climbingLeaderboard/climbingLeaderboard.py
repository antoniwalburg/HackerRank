#bisect solution
import bisect
def climbingLeaderboard(ranked, player):
    result = []
    ranked = sorted(set(ranked))
    for i in player:
        result.append(len(ranked) + (1 - bisect.bisect(ranked, i)))
    return result

#O(n^2) solution Time limit exceeded on 4 out of 12 test cases
def climbingLeaderboard(ranked, player):

    leader = []
    ans = []
    ranked = list(set(ranked))
    ranked.sort()

    for i in range(len(player)):
        for j in range(len(ranked)):
            if (player[i] < ranked[j]):
                leader.append(i)
    for i in range(len(player)):
        if (i not in leader):
            ans.append(player.count(player[i]))
        else:
            count = leader.count(i)
            ans.append(count + 1)
    if (1 not in ans):
        return ans
    else:
        for i in range(len(ans)):
            if (ans[i] == 1):
                index = i
                break
        for i in ans[index:-1]:
            if (i != 1):
                ans.remove(i)
                ans.insert(-1, 1)
        ans[-1] = 1
        return ans