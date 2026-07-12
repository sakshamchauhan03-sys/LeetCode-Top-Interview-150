class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        h1=int(startTime[0:2])
        h2=int(endTime[0:2])
        m1=int(startTime[3:5])
        m2=int(endTime[3:5])
        s1=int(startTime[6:])
        s2=int(endTime[6:])
        ts1=(3600*h1)+(60*m1)+s1
        ts2=(3600*h2)+(60*m2)+s2
        return ts2-ts1
        
        
        
        