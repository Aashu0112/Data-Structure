class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []
        for i in range(numRows):
            lst.append([])
            for j in range(i+1):

                lst[i].append(factorial(i)//(factorial(j)*factorial(i-j)))

        return lst