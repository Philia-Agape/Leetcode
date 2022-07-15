class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += self.countIsland(i, j, grid)
                
        return ans
        
    def countIsland(self, i: int, j: int, grid: List[List[str]]) -> int:
        direccion = [-1,0,1,0,-1]
        if i == -1 or i == len(grid) or j == -1 or j == len(grid[0]):
            return 0    
        elif grid[i][j] == "1":
            grid[i][j] = "0"
            for k in range (4):
                self.countIsland(i+direccion[k], j+direccion[k+1], grid)  
        else:
            return 0
        return 1
