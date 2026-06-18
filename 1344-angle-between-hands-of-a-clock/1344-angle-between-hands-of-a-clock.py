class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutesDegree=minutes*6
        hoursDegree=(hour*30)+(minutes*6)/12
        ans=abs(minutesDegree-hoursDegree)
        return min(ans,360-ans)