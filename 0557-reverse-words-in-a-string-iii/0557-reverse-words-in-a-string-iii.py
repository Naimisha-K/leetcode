class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.split()
        for i in range(len(w)):
            w[i]=w[i][::-1]
        return " ".join(w)