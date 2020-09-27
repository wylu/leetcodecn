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
from typing import List


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.people = {}
        self.parent = {}
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.people:
            self.people[parentName] = []
        self.people[parentName].append(childName)
        self.parent[childName] = parentName

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        indices = {k: 0 for k, _ in self.people.items()}
        seen = {self.king}
        x, curOrder = self.king, []
        if self.king not in self.dead:
            curOrder.append(self.king)
        while True:
            if not self.people.get(x) or set(self.people[x]).issubset(seen):
                if x == self.king:
                    break
                else:
                    x = self.parent[x]
            else:
                y = self.people[x][indices[x]]
                if y not in self.dead:
                    curOrder.append(y)
                seen.add(y)
                indices[x] += 1
                x = y
        return curOrder


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
