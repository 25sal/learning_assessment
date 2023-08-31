from enum import Enum


class ErrorTopics(Enum):
    declarations = 0
    conflict = 1
    incompatibility = 2
    assignment = 3
    initialization = 4
    parameters = 5
    syntax = 6
    array = 7


class WarningTopics(Enum):
    conflict = 0
    pointers = 1
    cast = 2
    scope = 3
    conversion = 4
    format = 5
    syntax = 6
    array = 7
