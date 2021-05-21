class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        intList = []
        letterList = []
        for i in logs:
            x = i.split( )
            identifier = x[0]
            if x[1].isnumeric() :
                intList.append(i)
            else:
                letterList.append(i)
                letterList.sort(key = lambda x:(x.split(' ',1)[1], x.split(' ',1)[0]))
        array = letterList + intList
        return array
            
