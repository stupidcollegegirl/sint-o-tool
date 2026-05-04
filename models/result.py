from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class ScanResult:
    target: str
    type: str
    data: Dict[str, Any]
    errors: list
