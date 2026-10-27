class Solution:
    def isValid(self, s: str) -> bool:

        stack =[]
        a=True
        for i in s:
            if i in "([{":
                stack.append(i)
            elif i in ")}]":
                if stack==[]:
                    a=False
                elif i==")" and stack[-1] =="(" :
                    stack.pop(-1)
                elif i=="}" and stack[-1]=="{" :
                    stack.pop(-1)
                elif i=="]" and stack[-1]=="[" :
                    stack.pop(-1)
                else:
                    a=False
            else:
                a=False
        if stack !=[]:
            a= False
        return a 

  








        


