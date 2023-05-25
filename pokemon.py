from dataclasses import dataclass
from typing import List


@dataclass
class Statistics:
    base_stat: str
    name: str


@dataclass
class Pokemon:
    name: str
    stats: List[Statistics]

    def get_statistic_base_stat(self, stat_name: str):
        for stat in self.stats:
            if stat.name == stat_name:
                return stat.base_stat
        return 0
