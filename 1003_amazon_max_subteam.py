"""
#Can you write a function to be able to calculate the sub team with the max average experience/

#Manager A 5 ManagerB ManagerC
#Manager B 5 employee1 4 employee2 2
#Manager C 5 employee3 3 employee4 6


#manager b = > 11/3 = 3.66
#manager c -> 14/3 = 4.66
#manager a 30/7 = 4.2

Here is a Python function to calculate the subteam with maximum average experience based on your hierarchical structure:

Problem Recap
Input tree:

scss
复制
编辑
Manager A (5)
├── Manager B (5)
│   ├── employee1 (4)
│   └── employee2 (2)
└── Manager C (5)
    ├── employee3 (3)
    └── employee4 (6)

Expected output
Manager B average = (5+4+2)/3 = 3.66

Manager C average = (5+3+6)/3 = 4.66

Manager A average = (5+5+4+2+5+3+6)/7 = 4.2

Hence Manager C has max average experience.
"""

class Node:
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp
        self.subordinates = []

def max_average_subteam(root):
    max_avg = float('-inf')
    max_manager = None

    def dfs(node):
        nonlocal max_avg, max_manager

        total, count = node.exp, 1
        for child in node.subordinates:
            child_total, child_count = dfs(child)
            total += child_total
            count += child_count

        avg = total / count
        if count > 1 and avg > max_avg:  # Only consider non-leaf managers
            max_avg = avg
            max_manager = node.name

        return total, count

    dfs(root)
    return max_manager, max_avg

# -----------------------------
# Build your input tree

# Define employees
employee1 = Node("employee1", 4)
employee2 = Node("employee2", 2)
employee3 = Node("employee3", 3)
employee4 = Node("employee4", 6)

# Define managers B and C
managerB = Node("ManagerB", 5)
managerB.subordinates = [employee1, employee2]

managerC = Node("ManagerC", 5)
managerC.subordinates = [employee3, employee4]

# Define top manager A
managerA = Node("ManagerA", 5)
managerA.subordinates = [managerB, managerC]

# -----------------------------
# Run the function

result = max_average_subteam(managerA)
print("Subteam with max average experience:", result)
