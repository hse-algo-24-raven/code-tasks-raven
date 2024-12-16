"""Классы пакета Расписание.

Task: Представляет задачу для составления расписания.

ScheduleItem: Представляет собой элемент расписания, включает в себя
задачу, выполняющуюся в течение некоторого времени.

StagedTask: Представляет задачу для составления расписания. Задача состоит из
нескольких этапов, каждый из которых имеет некоторую продолжительность.

ConveyorSchedule: Класс представляет оптимальное расписание для списка задач,
состоящих из двух этапов и двух исполнителей. Для построения расписания
используется алгоритм Джонсона.
"""

from schedule_pack.task import Task
from schedule_pack.schedule_item import ScheduleItem
from schedule_pack.staged_task import StagedTask
from schedule_pack.conveyor_schedule import ConveyorSchedule


__all__ = ["Task", "ScheduleItem", "StagedTask", "ConveyorSchedule"]
__version__ = "1.0.0"
__author__ = "Alexander Mikhailov"
__license__ = "MIT"
