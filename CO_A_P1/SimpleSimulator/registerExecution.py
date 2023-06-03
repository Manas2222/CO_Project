# def binary8bitConverter(number):
    


def overflowChecker(data):
    if data > 2**16 - 1:
        return True
    return False


def convert7bitStringToBin(data):
    answer = (int(data,2))
    # print(answer)
    return answer


def convertIntTo16BitBin(data):
    ans = bin(data)[2:].zfill(16)
    return ans



class Registers:


    registers = {
        "000" : '0000000000000000',
        "001" : '0000000000000000',
        "010" : '0000000000000000',
        "011" : '0000000000000000',
        "100" : '0000000000000000',
        "101" : '0000000000000000',
        "110" : '0000000000000000',
        '111' : '0000000000000000'
    }


    def getRegister(self,regNum):
        return int(self.registers[regNum],2)
    

    def setRegister(self,regNum,val):
        if overflowChecker(val) == False:
            self.registers[regNum] = bin(val)[2:].zfill(16)
        else:
            temp = bin(val)[2:]
            self.registers[regNum] = temp[len(temp) - 16 : ]


    def setOverflow(self):
        self.registers['111'] = '0000000000001000'

    
    def defaultFlag(self):
        self.registers['111'] = '0000000000000000'
            
    
    def dump(self):
        for k,v in self.registers.items():
            print(v,sep = ' ')
        print()
        return
    

RF = Registers()


# RF.dump()
# a = 26
# print(convertIntTo16BitBin(a))

# RF.setRegister('000',2**15 + 3 << 2)
# RF.dump()