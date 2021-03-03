
'''
    Allocating Tasks

    + Objectives:
      1. Build a DDD model to handle business logic (constraint) + Unit tests
      2. Build an adapter repository to abstract away persistence + Unit tests
      3. Build a simple service on Flask + Unit tests
      4. Build an Unit of Work

    + Noun:
      - [1|Week]
      - [2|Story]
      - [3|Task]
      - [4|Date]

    + Notes:
      - A [1] is identified by a reference, and a name comprises 7 of [4]
      - A [2] is identified by a reference, a name, a description. Assignees will have to break down a [2] into at least one [3]
      - A [3] is identified by a [2]'s reference, a name, a description, and a required points
      - A [4] is identified by a reference, a timestamp, and an available points

    + Constraints:
      - When users allocate a Story to a Date, the date's available points will be reduced by each Task's required points
      - Cannot allocate to a Date when the available points is less than the sum of tasks' required point
'''

from dataclasses import dataclass
from typing import List, Optional
from datetime import date, datetime

class Week:

    def __init__(self, ref: str, name: str):
        self.ref: str = ref
        self.name: str = name


@dataclass(unsafe_hash=True)
class Task:
    story_ref: str
    name: str
    desc: str
    required_point: int


class Story:

    def __init__(self, ref: str, name: str, desc: str, tasks: List[Task]):
        self.ref: str = ref
        self.name: str = name
        self.desc: str = desc
        self.tasks: List[Task] = tasks


class Day:

    def __init__(self, ref: str, ts: date, allocated_points: int):
        self.ref: str = ref
        self.ts: date = ts
        self.allocated_points: int = allocated_points
        self._allocations = set()

    @property
    def available_points(self):
        return self.allocated_points - self.allocation_points

    @property
    def allocation_points(self):
        return sum([task.required_point for task in self._allocations])

    def allocate(self, task: Task):
        if task.required_point > self.allocated_points:
            raise Exception("Can't allocate task")
        if task not in self._allocations:
            self._allocations.add(task)
