class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        count={}
        maxf=0
        ans=0
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                count[s[i]] += 1
            maxf= max(maxf, count[s[i]])
            while (i-l+1)-maxf>k:
                count[s[l]]-=1
                l+=1
            ans=max(ans,i-l+1)
        return ans