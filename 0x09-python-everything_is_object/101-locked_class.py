#!/usr/bin/python3
"""Locked class called Lockedclass"""


class LockedClass:
"""Al locked class thatprevents the user from dynamically creating new
    intances attributes except if the attribute is called first_name
"""

    __slots__ = ["first_name"]
