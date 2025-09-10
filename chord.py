import hashlib

M = 5  
RING_SIZE = 2 ** M

def hash_key(key: str) -> int:
    return int(hashlib.sha1(key.encode()).hexdigest(), 16) % RING_SIZE


class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.successor = self
        self.predecessor = None
        self.finger = [self] * M

    def __repr__(self):
        return f"Node({self.id})"

    def find_successor(self, key_id):
        if self.id < key_id <= self.successor.id:
            return self.successor
        else:
            n0 = self.closest_preceding_finger(key_id)
            if n0 == self:
                return self.successor
            return n0.find_successor(key_id)

    def closest_preceding_finger(self, key_id):
        for i in reversed(range(M)):
            if self.id < self.finger[i].id < key_id:
                return self.finger[i]
        return self

    def join(self, other):
        if other:
            self.init_finger_table(other)
        else:
            for i in range(M):
                self.finger[i] = self
            self.predecessor = self
            self.successor = self

    def init_finger_table(self, other):
        self.finger[0] = other.find_successor((self.id + 1) % RING_SIZE)
        self.successor = self.finger[0]
        self.predecessor = self.successor.predecessor
        self.successor.predecessor = self
        for i in range(M - 1):
            start = (self.id + 2 ** (i + 1)) % RING_SIZE
            if start <= self.finger[i].id:
                self.finger[i + 1] = self.finger[i]
            else:
                self.finger[i + 1] = other.find_successor(start)
