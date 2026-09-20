class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {"+", "-", "*", "/"}
        stack = []
        for val in tokens:
            if val in operations:
                val_1 = stack.pop()
                val_2 = stack.pop()
                if val == "+" :
                    stack.append(val_1+val_2)
                elif val == "-" :
                    stack.append(val_2-val_1)
                elif val == "*": 
                    stack.append(val_1*val_2)
                else: # val == "/"
                    stack.append(int(val_2 / val_1))
            else:
                stack.append(int(val))
        return stack[-1]
