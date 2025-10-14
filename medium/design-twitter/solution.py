"""
355. Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, 
and is able to see the 10 most recent tweets in the user's news feed.

Time Complexity:
- postTweet: O(1)
- getNewsFeed: O(k log n) where k is number of tweets retrieved (up to 10) and n is number of users being followed
- follow: O(1)
- unfollow: O(1)

Space Complexity: O(n + m) where n is total number of tweets and m is total number of follow relationships
"""

import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.timeStamp = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [timestamp, tweetId]
        self.followMap = defaultdict(set)  # userId -> set of followeeIds
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Composes a new tweet with ID tweetId by the user userId.
        Each call to this function will be made with a unique tweetId.
        """
        self.tweetMap[userId].append([self.timeStamp, tweetId])
        self.timeStamp -= 1  # incrementing in negative so we can use minHeap to get most recent tweets

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieves the 10 most recent tweet IDs in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user themself.
        Tweets must be ordered from most recent to least recent.
        """
        result = []   # returns top 10 most recent tweets for a user
        minHeap = []

        self.followMap[userId].add(userId)  # because we need to return tweets made by user as well
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1  # most recent tweet will be in last
                timeStamp, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([timeStamp, tweetId, followeeId, index - 1])
        
        heapq.heapify(minHeap)
        while minHeap and len(result) < 10:
            timeStamp, tweetId, followeeId, index = heapq.heappop(minHeap)
            result.append(tweetId)
            if index >= 0:
                timeStamp, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [timeStamp, tweetId, followeeId, index - 1])
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        The user with ID followerId started following the user with ID followeeId.
        """
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        The user with ID followerId started unfollowing the user with ID followeeId.
        """
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


# Example usage:
if __name__ == "__main__":
    twitter = Twitter()
    
    # Test case from the problem
    twitter.postTweet(1, 5)        # User 1 posts tweet 5
    print(twitter.getNewsFeed(1))  # Should return [5]
    
    twitter.follow(1, 2)           # User 1 follows user 2
    twitter.postTweet(2, 6)        # User 2 posts tweet 6
    print(twitter.getNewsFeed(1))  # Should return [6, 5]
    
    twitter.unfollow(1, 2)         # User 1 unfollows user 2
    print(twitter.getNewsFeed(1))  # Should return [5]
