
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


@dataclass
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


class Date:

    def __init__(self, ref: str, ts: date, available_points: int):
        self.ref: str = ref
        self.ts: date = ts
        self.available_points: int = available_points

    def allocate(self):
        pass