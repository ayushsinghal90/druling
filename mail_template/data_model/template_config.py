from dataclasses import dataclass

from typing import Any


@dataclass
class TemplateConfig:
    template_name: str
    subject: str
    html: Any
    text: Any
    source: str
