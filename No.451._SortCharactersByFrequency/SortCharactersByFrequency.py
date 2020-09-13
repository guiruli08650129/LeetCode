class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic.keys():
                dic[i] = dic.get(i) + 1
            else:
                dic[i] = 1
                
        candidate=(sorted(dic.items(), key=lambda a: a[1], reverse=True))
        
        out = ""
        for item in candidate:
            c, num = item
            out = out + c*num
            
        return out   
        
        