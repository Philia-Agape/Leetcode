class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort();
        print(amount[0]);
        if amount[0] + amount[1] <= amount[2]:
            return amount[2];
        else:
            #amount[0]+amount[1]+amount[2] ==amount[2]-(amount[1]-amount[0])
            if (amount[2]-amount[1]+amount[0]) % 2 == 0:
                return (amount[0]+amount[1]+amount[2]) >> 1;
            else:
                return (amount[0]+amount[1]+amount[2]+1) >> 1;
