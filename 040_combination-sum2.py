"""
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次 。
注意：解集不能包含重复的组合。 

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]

在一个数组（存在重复值）中寻找和为特定值的组合。
注意点：
所有数字都是正数
组合中的数字要按照从小到大的顺序
原数组中的数字只可以出现一次
结果集中不能够有重复的组合
例子：
输入: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8 输出: [[1, 1, 6], [1, 2, 5], [1, 7],
[2, 6]]
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        res_combs = []
        self.combination(candidates, target, [], res_combs)
        return res_combs

    def combination(self, candidates, target, cur_comb, res_combs):
        s = sum(cur_comb) if cur_comb else 0
        if s > target:
            return
        elif s == target:
            res_combs.append(cur_comb)
            return
        else:
            i = 0
            while i < len(candidates):
                self.combination(candidates[i + 1:], target, cur_comb + [candidates[i]], res_combs)
                # ignore repeating elements
                while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1
                i += 1


if __name__ == "__main__":
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]