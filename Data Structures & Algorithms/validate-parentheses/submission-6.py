class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in s:
            if i in bracket_map:
                top_element = stack.pop() if len(stack) > 0 else'#'

                if bracket_map[i] != top_element:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0