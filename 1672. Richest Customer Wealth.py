class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        if accounts is None or len(accounts) == 0:
            return accounts

        summW = sum(accounts[0])
        for i in range(1,len(accounts)):
            if sum(accounts[i]) > summW:
                summW = sum(accounts[i])
        return summW

            
