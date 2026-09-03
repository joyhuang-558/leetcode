class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a,b):
            return int(a)+int(b)
        def minus(a,b):
            return int(a)-int(b)
        def multiplate(a,b):
            return int(a)*int(b)
        def divide(a,b):
            return int(a)/int(b)
        stack = []
        for i in tokens:
            print(f"current i: {i}")
            if i not in "+-*/":
                stack.append(int(i))
                print(f"stack:{stack}")
            else:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    res = add(a,b)
                if i == "-":  
                    res = minus(a,b)          
                if i == "*": 
                    res = multiplate(a,b)
                if i == "/":
                    res = divide(a,b)

                print(f"res:{res}")
                stack.append(res)
        return int(stack.pop())
        
        