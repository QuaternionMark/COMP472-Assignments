import heapq
from typing import Tuple, List

from structures.PuzzleNode import PuzzleNode


class PriorityQueue:
    def __init__(self):
        self.elements: List[Tuple[int, PuzzleNode]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: PuzzleNode, priority: int):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> PuzzleNode:
        return heapq.heappop(self.elements)[1]