"""
Bracket Validation and Nested String Parser

**Problem**: Parse and validate nested string structures with brackets.

**Part A**: Validate Well-Formed Brackets
Determine if a tokenized string has properly matched brackets.

**Part B**: Convert Nested Strings to Nested Lists
Transform bracket-delimited strings into nested list structures.

**Test Cases**:
```python
assert is_well_formed(tokenize("(a,b,c)"))        # True
assert is_well_formed(tokenize("(a,b,c))"))       # False
assert read_rich_text(tokenize("(a,(b),c)")) == [['a', ['b'], 'c']]
assert read_rich_text(tokenize("(((a)b)c)")) == [[[['a'], 'b'], 'c']]
```

"""

class Solution(object):
    def is_well_formed(self, str):
        """
        :type str: a string
        :rtype bool: Ture if it is well formed, otherwise False if not
        """
        if not str or len(str) % 2 != 0:
            return False            

        N = len(str)

        # clean all other ch if it is not '()[]{}'
        for i, ch in enumerate(str):
            if ch not in '()[]{}':
                str = str.replace(ch, '')            

        while '()' in str or '[]' in str or '{}' in str:
            str = str.replace('()', '')
            str = str.replace('[]', '')
            str = str.replace('{}', '')
        
        if len(str) == 0:
            return True
        else:
            return False

        pass
    def is_well_formed2(self, str):
        """
        :type str: a string
        :rtype bool: Ture if it is well formed, otherwise False if not
        """
        if not str:
            return False

        N = len(str)
        stack = []
        for i, ch in enumerate(str):
            if ch in '([{':
                stack.append(ch)
            elif ch in ')]}':
                if len(stack)==0:
                    return False
                if (ch == ')' and stack[-1]!='(') or (ch == ']' and stack[-1]!='[')\
                    or (ch == '}' and stack[-1]!='{'):
                    return False
                stack.pop()
            else:
                continue

        return True if len(stack)==0 else False


    def read_rich_text(self, str):
        """
        :type str: input string
        :rtype: parsed layered string
        """    
        def parse(idx):
            result = []
            while idx < len(str):
                tok = str[idx]
                if tok == '(':
                    sublist, idx = parse(idx + 1)
                    result.append(sublist)
                elif tok == ')':
                    return result, idx + 1
                elif tok == ',':
                    idx += 1  # skip comma
                else:
                    result.append(tok)
                    idx += 1
            return result, idx

        parsed, _ = parse(0)
        return parsed


if __name__ == "__main__":
    print(Solution().is_well_formed("(a,b,c)")) # True
    print(Solution().is_well_formed("(a,b,c))")) # False

    print(Solution().read_rich_text("(a,(b),c)")) # [['a', ['b'], 'c']]
    print(Solution().read_rich_text("(((a)b)c)")) # [[[['a'], 'b'], 'c']]