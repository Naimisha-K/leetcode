class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=sentence.lower()
        c=0
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if i in s:
                c+=1
        if c==26:
            return True
        else:
            return False