"""
2 big num add, numbers are stored as string
大数相加问题
今天视频面时，面试官让我手撕大数相加问题。现在就来总结一下。
两个大数相加。

两个数无限大的整数，long都装不下；
两个数都是以字符串的方式提供。
两个字符串的数字相加，核心点考的是ASCII码和相加进位的问题。
例如字符类型的’9’转换成int的9： ‘9’ - ‘0’ = 9。 还有就是相加时要注意进位的问题。

解题思路
总共分为一下四步：

从结尾开始每位相加
两个整数长度不相等(肯定有一个已经加完了，再把没有加完的加上去)
最高位有进位,要再进一位
结果字符串逆序
"""

"""
//C++大数相加
string BigNumAdd(const string& strNum1, const string& strNum2)
{
    string strSum;
    int len1 = strNum1.size()-1;
    int len2 = strNum2.size()-1;
    int bit = 0;                //保存进位

    //从结尾开始每位相加 
    while (len1>=0 && len2>=0)
    {
        //求每位的和(要把进位也加上) 
        int tmpSum = strNum1[len1]-'0' + strNum2[len2]-'0' + bit;
        //保存进结果 
        strSum += tmpSum % 10 + '0';
        //求进位 
        bit = tmpSum / 10;
        --len1;
        --len2; 
    }

    //两个整数长度不相等(肯定有一个已经加完了,不需要再额外加if来判断，因为while就可以判断)
    while (len1 >= 0)
    {
        //和上个while循环一样
        int tmpSum = strNum1[len1]-'0' + bit;
        strSum += tmpSum % 10 + '0';
        bit = tmpSum / 10;
        --len1; 
    }
    while (len2 >= 0) 
    {
        //和上个while循环一样
        int tmpSum = strNum2[len2]-'0' + bit;
        strSum += tmpSum % 10 + '0';
        bit = tmpSum / 10;
        --len2; 
    }

    //最高位有进位
    if (bit != 0)
        strSum += bit + '0'; 

    //反转
    reverse(strSum.begin(), strSum.end()); 

    return strSum;
}
"""

class Solution(object):
    def bigNumAdd(self, num1, num2):
        len1 = len(num1)
        len2 = len(num2)
        carry_bit = 0
        str_sum = []
        while len1>0 and len2>0:
            tmp_sum = ord(num1[len1-1]) - ord('0') + ord(num2[len2-1]) - ord('0') + carry_bit
            carry_bit = int(tmp_sum / 10)
            str_sum.append(tmp_sum%10)
            len1 = len1-1
            len2 = len2-1

        while len1>0:
            tmp_sum = ord(num1[len1-1]) - ord('0') + carry_bit
            carry_bit = int(tmp_sum / 10)
            str_sum.append(tmp_sum%10)
            len1 = len1-1
            
        while len2>0:
            tmp_sum = ord(num2[len2-1]) - ord('0') + carry_bit
            carry_bit = int(tmp_sum / 10)
            str_sum.append(tmp_sum%10)
            len2 = len2-1

        if carry_bit>0:
            str_sum.append(carry_bit)

        # reverse str_sum
        str_sum.reverse()
        return str_sum

    
    def bigNumSub(self, num1, num2):
        len1 = len(num1)
        len2 = len(num2)
        carry_bit = 0
        str_sum = []
        while len1>0 and len2>0:
            tmp_sum = ord(num1[len1-1]) - ord('0') + ord(num2[len2-1]) - ord('0') + carry_bit
            carry_bit = int(tmp_sum / 10)
            str_sum.append(tmp_sum%10)
            len1 = len1-1
            len2 = len2-1

        while len1>0:
            tmp_sum = ord(num1[len1-1]) - ord('0') + carry_bit
            carry_bit = int(tmp_sum / 10)
            str_sum.append(tmp_sum%10)
            len1 = len1-1
            
        while len2>0:
            tmp_sum = ord(num2[len2-1]) - ord('0') + carry_bit
            carry_bit = int(tmp_sum / 10)
            str_sum.append(tmp_sum%10)
            len2 = len2-1

        if carry_bit>0:
            str_sum.append(carry_bit)

        # reverse str_sum
        str_sum.reverse()
        return str_sum

if __name__ == "__main__":
    print(Solution().bigNumAdd('9876', '6789'))
    print(Solution().bigNumAdd('9876654', '6789'))


