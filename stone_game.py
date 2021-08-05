class Solution:
    def stoneGame(self, piles) -> bool:
        Alex = 0
        Lee = 0
        player = 'Alex'
        while len(piles) > 0:
            if player == 'Alex':
                if piles[0] > piles[-1]:
                    Alex += piles.pop(0)
                else:
                    Alex += piles.pop(-1)
            else:
                if piles[0] > piles[-1]:
                    Lee += piles.pop(0)
                else:
                    Lee += piles.pop(-1)
            player == 'Lee' if player == 'Alex' else player== 'Alex'
        if Alex > Lee:
            return True
    

x = Solution()
x.stoneGame([1,3,6,4,7,3,5,4])