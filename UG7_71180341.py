class PrefixConverter:
    id = {'*':2,'/':2,'+':1,'-':1}
    def __init__(self):
        self.stackList = []
        

    
    def push(self,data):
        self.stackList.append(data)

   
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"
    
    
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"

    def isempty(self):
        if(self.size==-1):
            return True
        else:
            return False
    
    def seek(self):
        if self.isempty():
            return False;
        else:
            return self.stackList[self.size];
    
    def cekValidExpression(self,expression):
        for isi in self.stackList:
            if isi == '(' or isi == ')':
                return False;
            else:
                if isi == "*" or isi == "+" or isi == "-" or isi == "/":
                    return True;
                
    def infixToPrefix(self,expression):
        
        prefix=""
        status = self.cekValidExpression(expression)
        if status == False:
            print("Expresi Infix yang anda masukkan tidak valid !!")
        else:
            for isi in expression:
                if(isi in '+-/*'):
                    while(len(self.stackList)and self.nilai[isi] < self.nilai[self.seek()]):
                        prefix += self.pop()
                    self.push(isi)

# Test Case
if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))