class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = ['{','(','[']
        closers = ['}',')',']']
        for i in s :
            if i in openers :
                stack.append(i)
            if i in closers :
                if len(stack)>0:
                    if openers.index(stack[-1]) == closers.index(i) :
                        stack.pop()
                    else :
                        return False
                else :
                    return False
        if len(stack) == 0 :
            return True
        else :
            return False