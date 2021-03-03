from datetime import date
from domains.model import Day, Task


def test_abc():
    day = Day("20210303", date.today(), 20)
    task = Task("story-001", "task-001", "task-001-desc", 10)

    day.allocate(task)

    assert day.available_points == 10
