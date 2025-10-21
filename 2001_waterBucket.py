"""
### 2. Water Bucket Problem

**Problem**: Given buckets of different sizes, determine how to fill or empty buckets to reach a target volume.

**Requirements**:
- Buckets can be filled completely or emptied completely
- Calculate minimum operations to reach target
- Handle impossible cases

**Example**:
```python
buckets = [3, 5, 8]  # Bucket sizes
target = 11
# Solution: Fill 8L and 3L buckets → Total = 11L
```
"""

'''
my idea:
1) sort original list
2) transfer the problem: select minimum number of buckets whose sum equal to target
3) use DP algo
'''

class solu(object):
    def func1(self, buckets, target):
        if not buckets:
            return 0

        nums = buckets #sorted(buckets, reverse = True) # sort
        size = len(nums)
        left = 0
        sub_sum = 0
        sub_list = []

        for right in range(size):
            sub_sum += nums[right]            
            sub_list.append(nums[right])

            while sub_sum > target:
                sub_sum -= nums[left]
                sub_list.remove(nums[left])
                left += 1                

            if sub_sum == target:
                return len(sub_list), sub_list

        if sub_sum == target:
            return len(sub_list), sub_list
        else:
            return 0, None


    def func2(self, buckets, target):
        if not buckets:
            return 0

        #buckets.sort(reverse = True)
        #nums = buckets
        nums = sorted(buckets, reverse = False)
        size = len(nums)
        
        left = 0
        right = 0
        sub_sum = 0
        sub_nums = []        
        res_len = size+1
        res_nums = []

        while right < size:
            if nums[right] > target:
                right += 1
                continue
            
            sub_nums.append(nums[right])
            sub_sum += nums[right]

            if sub_sum > target:
                left += 1
                sub_sum -= nums[left]
                sub_nums.remove(nums[left])

            if sub_sum >= target:
                res_len = min(res_len, right-left+1)
                
            right += 1            
        
        if res_len != size+1:
            return res_len, sub_nums
        else:
            return 0, None

    # DP solution, return len of sub-array and sub-array
    def func3(self, nums, target):
        # dp[s] = (最少个数, 上一个和, 当前使用的元素)
        dp = [(float('inf'), None, None)] * (target + 1)
        dp[0] = (0, None, None)  # 和为0时需要0个元素

        for num in nums:
            for s in range(target, num - 1, -1):  # 倒序保证每个元素只用一次
                if dp[s - num][0] != float('inf'):  # 可达
                    new_count = dp[s - num][0] + 1
                    if new_count < dp[s][0]:
                        dp[s] = (new_count, s - num, num)

        # 如果无解
        if dp[target][0] == float('inf'):
            return -1, []

        # 回溯找元素
        res = []
        s = target
        while s != 0:
            count, prev, num = dp[s]
            res.append(num)
            s = prev

        return dp[target][0], res[::-1]  # 翻转使顺序更自然

    # DP solution, return len of sub_len
    """
    动态规划思路
    我们要找到一个子集，使得和为 target，并且使用的元素个数最少。

    定义 DP 状态：
    dp[s] = 组成和为 s 的最少元素个数

    初始化时：
    dp[0] = 0 （和为 0 不需要任何元素）
    其他 dp[s] = inf

    状态转移：
    遍历数组中的每个数 num，更新所有可能的和 s：
    dp[s] = min(dp[s], dp[s - num] + 1)

    这里的更新顺序要从 大到小，避免一个元素被重复使用（如果允许重复用则从小到大）。

    答案：
    最终 dp[target] 如果不是 inf，就是最小元素个数，否则表示无解。
    """
    def func4(self, nums, target):
        # 初始化dp数组
        dp = [float('inf')] * (target + 1)
        dp[0] = 0  # 和为0时需要0个元素

        for num in nums:
            # 倒序遍历，防止重复使用元素
            for s in range(target, num - 1, -1):
                if dp[s - num] != float('inf'):
                    dp[s] = min(dp[s], dp[s - num] + 1)

        return dp[target] if dp[target] != float('inf') else -1

if __name__ == "__main__":
    print(solu().func3([5, 3, 8], 11), "target = ", 11)
    print(solu().func3([1, 3, 2, 4, 8, 5], 16), "target = ", 16)
    #print(solu().func3([1, 3, 2, 4, 8, 5], 16), "target = ", 16)