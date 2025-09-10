import unittest
from chord import Node, hash_key

nodes = [Node(hash_key(f"node{i}")) for i in range(4)]
nodes[0].join(None)  
for i in range(1, 4):
    nodes[i].join(nodes[0])

print("Danh sách Node trong vòng:")
for n in nodes:
    print(f"Node ID: {n.id}, Successor: {n.successor.id}")

keys = ["John", "Alex", "Linda", "Dyan"]

print("\nKết quả lookup các key:")
for k in keys:
    kid = hash_key(k)
    succ = nodes[0].find_successor(kid)
    print(f"Key '{k}' (id={kid}) được lưu tại Node {succ.id}")
