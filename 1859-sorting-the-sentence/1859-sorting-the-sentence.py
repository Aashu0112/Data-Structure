class Solution:
    def sortSentence(self, s: str) -> str:
        lst1 = s.split()
        lst = [None]*(len(lst1))
        for i in range(len(lst1)):
            lst[int(lst1[i][-1]) - 1] = lst1[i][:-1]

        return ' '.join([str(elem) for elem in lst])
        