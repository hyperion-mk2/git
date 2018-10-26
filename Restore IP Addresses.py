class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num = 0
        xmax = [0]*len(grid[0])
        ymax = [0]*len(grid)
        for index in range(len(grid)):
            for index2 in range(len(grid[index])):
                if grid[index][index2] > 0:
                    num += 1
                    if(grid[index][index2]>xmax[index2]):
                        xmax[index2] = grid[index][index2]
                    if (grid[index][index2] > ymax[index]):
                        ymax[index] = grid[index][index2]
        return num+sum(xmax)+sum(ymax)
if __name__ == '__main__':
    Solution.projectionArea(Solution,[[1,1,1],[1,0,1],[1,1,1]])