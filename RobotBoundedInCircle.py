class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        start_point=[0,0]
        direction='N'
        for a in instructions:
            if direction=='N':
                if a=='G':
                    start_point[1]=start_point[1]+1
                    direction='N'
                elif a=='L':
                    direction='W'
                else:
                    direction='E'
            elif direction=='S':
                if a=='G':
                    start_point[1]=start_point[1]-1
                    direction='S'
                elif a=='L':
                    direction='E'
                else:
                    direction='W'
            elif direction=='E':
                if a=='G':
                    start_point[0]=start_point[0]+1
                    direction='E'
                elif a=='L':
                    direction='N'
                else:
                    direction='S'
            else:
                if a=='G':
                    start_point[0]=start_point[0]-1
                    direction='W'
                elif a=='L':
                    direction='S'
                else:
                    direction='N'
        if ((start_point[0]==0) and (start_point[1]==0)):
            return (bool(1))
        elif direction!='N':
            return(bool(1))
        else:
            return(bool(0))
