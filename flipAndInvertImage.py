class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for index in range(len(A)):
            datalen = len(A[index])
            for index2 in range(len(A[index])//2):
                A[index][index2],A[index][datalen-1-index2] = A[index][datalen-index2-1],A[index][index2]
            for index2 in range(len(A[index])):
                A[index][index2] = 1 - A[index][index2]
        return A
if __name__ == "__main__":
    print(Solution.flipAndInvertImage(Solution,[[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
