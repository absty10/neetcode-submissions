class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 !=0:
            return False
        
        stack=list()
        print(stack)
        for i in s:
            print('i= ', i)
            if i=="[" or i=="(" or i=="{":
                stack.append(i)
                print(stack)
            else:
                if len(stack)==0:
                    return False
                    break
                if stack[-1] == '[' and i==']':
                    stack.pop()
                    print(stack)
                elif stack[-1] == '(' and i==')':
                    stack.pop()
                    print(stack)
                elif stack[-1] == '{' and i=='}':
                    stack.pop()
                    print(stack)
                else:
                    return False

        if stack: 
            return False
        else:
            return True


