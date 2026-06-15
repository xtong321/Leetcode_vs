"""
1318. Minimum Flips to Make a OR b Equal to c
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
核心逻辑:
比较 a, b, c 在同一二进制位（bit）上的值：
当 c 的该位为 0 时：a 和 b 的该位必须都为 0。
如果 a 的该位是 1，翻转 1 次；如果 b 的该位是 1，翻转 1 次。总翻转次数为 a 与 b 该位数值之和。
当 \(c\) 的该位为 1 时：\(a\) 或 \(b\) 的该位至少要有一个为 1。如果 \(a\) 和 \(b\) 的该位均为 0，则必须翻转其中一个使之变为 1，总翻转次数加 1。
"""

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1
            
            if bit_c == 0:
                # c 为 0 时，a 和 b 的对应位必须都是 0
                flips += (bit_a + bit_b)
            else:
                # c 为 1 时，a 和 b 的对应位至少有一个为 1
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            
            a >>= 1
            b >>= 1
            c >>= 1
        
        return flips
    
    def minFlips2(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a>0 or b>0 or c>0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & c
            if bit_c == 0:
                ans += (bit_a + bit_b)
            else:
                if bit_a==0 and bit_b==0:
                    ans += 1
                
            a >>=1
            b >>=1
            c >>=1
        
        return ans
        
        