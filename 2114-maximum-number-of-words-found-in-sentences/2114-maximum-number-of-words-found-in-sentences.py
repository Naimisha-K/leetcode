class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=len(sentences[0].split())
        for i in range(len(sentences)):
            if len(sentences[i].split())>m:
                m=len(sentences[i].split())
        return m