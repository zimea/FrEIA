
from .base import Split

import torch


class EvenSplit(Split):
    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        return torch.split(x, 2, dim=1)

    def inverse(self, x1: torch.Tensor, x2: torch.Tensor) -> torch.Tensor:
        return torch.cat((x1, x2), dim=1)
