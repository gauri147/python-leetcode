class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        for a in boxTypes:
            a[0],a[1]=a[1],a[0]
        boxTypes=sorted(boxTypes,reverse=True)
        res=0
        units=0
        for a in boxTypes:
            while a[1]>0 and truckSize>res:
                res+=1
                a[1]-=1
                units+=a[0]
                #print(units)
        return(units)
