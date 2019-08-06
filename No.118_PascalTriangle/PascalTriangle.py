class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows is 0:
            return []        
        elif numRows is 1:
            return [[1]]
        elif numRows is 2:
            return [[1], [1,1]]
        else:
            output = []
            output.append([1])
            output.append([1,1])
            for i in range(numRows-2):
                current = output[-1]
                sublist = [1]
                for j in range(len(current)-1):
                    sublist.append(current[j]+current[j+1])
                sublist.append(1)
                output.append(sublist)
            return output