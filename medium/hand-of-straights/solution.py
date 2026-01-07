# spador

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        cardmap = {}
        for i in range(len(hand)):
            if hand[i] not in cardmap:
                cardmap[hand[i]] = 1
            else:
                cardmap[hand[i]] += 1
        
        minHeap = list(cardmap.keys())
        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]

            for i in range(start, start + groupSize):
                if i not in cardmap:
                    return False
                cardmap[i] -= 1
                if cardmap[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True

