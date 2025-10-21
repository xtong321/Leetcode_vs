"""
给你一个无重复元素的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的所有不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的同一个数字可以无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
对于给定的输入，保证和为 target 的不同组合数少于 150 个。

示例 1：
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。

示例 2：
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

示例 3：
输入: candidates = [2], target = 1
输出: []

Idea:
解题思路
采用回溯法。由于组合中的数字要按序排列，我们先将集合中的数排序。依次把数
字放入组合中，因为所有数都是正数，如果当前和已经超出目标值，则放弃；如果
和为目标值，则加入结果集；如果和小于目标值，则继续增加元素。由于结果集中
不允许出现重复的组合，所以增加元素时只增加当前元素及之后的元素。
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        result_list = []
        self.combination(candidates, target, [], result_list)
        return result_list

    def combination(self, candidates, target, current_list, result_list):
        s = sum(current_list) if current_list else 0
        if s > target:
            return
        elif s == target:
            result_list.append(current_list)
            return
        else:
            for i, v in enumerate(candidates):
                self.combination(candidates[i:], target, current_list + [v], result_list)


if __name__ == "__main__":
    print(Solution().combinationSum([2, 3, 6, 7], 7))