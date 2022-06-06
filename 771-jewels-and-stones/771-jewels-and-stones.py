class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = list(stones.strip())
        original = len(stones)
        for i in jewels:
            stones  = list(filter(lambda a: a!=i ,stones))
        
        return original - len(stones)