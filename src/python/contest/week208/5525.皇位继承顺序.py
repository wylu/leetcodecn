#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5525.皇位继承顺序.py
@Time    :   2020/09/27 11:18:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.children = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []

        def dfs(name: str) -> None:
            if name not in self.dead:
                ans.append(name)
            for child in self.children[name]:
                dfs(child)

        dfs(self.king)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

if __name__ == "__main__":
    t = ThroneInheritance("king")
    t.birth("king", "andy")
    # 继承顺序：king > andy
    t.birth("king", "bob")
    # 继承顺序：king > andy > bob
    t.birth("king", "catherine")
    # 继承顺序：king > andy > bob > catherine
    t.birth("andy", "matthew")
    # 继承顺序：king > andy > matthew > bob > catherine
    t.birth("bob", "alex")
    # 继承顺序：king > andy > matthew > bob > alex > catherine
    t.birth("bob", "asha")
    # 继承顺序：king > andy > matthew > bob > alex > asha > catherine
    print(t.getInheritanceOrder())
    # 返回 ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
    t.death("bob")
    # 继承顺序：king > andy > matthew > bob（已经去世）> alex > asha > catherine
    print(t.getInheritanceOrder())
    # 返回 ["king", "andy", "matthew", "alex", "asha", "catherine"]
