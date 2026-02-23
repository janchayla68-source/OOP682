from abc import ABC, abstractclassmethod
from typing import List

class ILogSource(ABC):

    @abstractclassmethod
    def get_logs(self) -> List[str]:
        pass