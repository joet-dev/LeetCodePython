
class DecimalToBinary: 

    def findBin(self, num, res):
        if num == 0:
            return res 
        
        res = str(num % 2) + res
        return self.findBin(num // 2, res)
    
    

dtb = DecimalToBinary()
print(dtb.findBin(20,""))