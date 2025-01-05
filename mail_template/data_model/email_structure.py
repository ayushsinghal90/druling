from dataclasses import dataclass
from typing import Any


@dataclass
class EmailStructure:
    html_part: Any
    text_part: Any
