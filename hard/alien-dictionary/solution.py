from typing import List

# spador

# I do not understand the purpose of this question, hence I don't understand the question.
# I will come back to this one day to understand it better.


class Solution:

    def alienOrder(self, words: List[str]) -> str:

        adj = {c:set() for w in words for c in w}


        for i in range(len(words) - 1):

            w1, w2 = words[i], words[i+1]

            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:

                return ""

            for j in range(minLen):

                if w1[j] != w2[j]:

                    adj[w1[j]].add(w2[j])

                    break
        
        visit = {} # False = visited, True = current path

        result = []


        def dfs(c):

            if c in visit:

                return visit[c]

            visit[c] = True

            for nei in adj[c]:

                if dfs(nei):

                    return True

            visit[c] = False

            result.append(c)
        

        for c in adj:

            if dfs(c):

                return ""

        result.reverse()

        return "".join(result)
