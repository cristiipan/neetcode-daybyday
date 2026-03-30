from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)  # 如果key不存在，会自动创建这个key，对应的value设置为空list
        self.follows = defaultdict(set)  # 默认是空set而不是空list
        # 为什么用set？1. 性能，set的添加和删除和查找都是O1，list也可以用可以实现功能但是性能差一些
                    # 2. set自动去重，如果一个人关注又取关又关注，只会存储一次这个关注关系而不是两次
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1  # +1的逻辑放在前面，第一条tweet从0开始
        self.tweets[userId].append((self.timestamp, tweetId))  # append tuple 记录发贴时间和贴子id

        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result = []
        people = self.follows[userId] | {userId}  # 用set的并集

        for person in people:
            for tweet in self.tweets[person]:  # set没有.values() 直接遍历就可以了 这里已经通过userId定位到它的value了就是一个关注者set
                heapq.heappush(heap, (-tweet[0], tweet[1]))
        while heap and len(result) < 10:
            result.append(heapq.heappop(heap)[1])

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)  # the key->value should be follower->followee, cause we need the follower's info to decide who are their followees, and then pull out their tweets
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
"""
时空复杂度
    postTweet：O(1)
    follow/unfollow：O(1)
    getNewsFeed：O(n log n)
    n = 所有相关用户的推文总数
    把所有推文push进堆：O(n log n)
    pop出10条：O(10 log n) = O(log n)
    总体：O(n log n)
空间复杂度：O(n)
    n = 所有推文总数
"""
