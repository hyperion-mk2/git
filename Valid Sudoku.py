class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        numlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for index in range(len(board)):
            for index2 in range(len(numlist)):
                if board[index].count(numlist[index2]) > 1:

                    return False
        for index in range(9):
            datalist = []
            for index2 in range(9):
                datalist.append(board[index2][index])
            for index3 in range(9):
                if datalist.count(numlist[index3]) > 1:

                    return False
        for index1 in range(3):
            for index2 in range(3):
                datalist = []
                for index3 in range(3):
                    for index4 in range(3):
                        datalist.append(board[3*index1+index3][3*index2+index4])
                for index5 in range(9):
                    if datalist.count(numlist[index5]) > 1:
                        return False
        return True

if __name__ == '__main__':
    print(Solution.isValidSudoku(Solution,[["5","2",".",".","7",".",".",".","."],["3","8",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
