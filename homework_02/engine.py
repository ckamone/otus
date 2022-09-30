"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Vehicle:
    volume: int
    pistons: int  # цилиндры
