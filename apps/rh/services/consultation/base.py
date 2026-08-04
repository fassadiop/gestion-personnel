from abc import ABC, abstractmethod
from typing import Any

from .registry import ConsultationRegistry


class BaseConsultationProvider(ABC):
    """
    Classe de base des providers de consultation.
    """

    provider = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.provider:
            ConsultationRegistry.register(
                cls.provider,
                cls,
            )

    @classmethod
    def execute(cls, **kwargs) -> Any:
        cls.validate(**kwargs)
        return cls.process(**kwargs)

    @classmethod
    def validate(cls, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def process(cls, **kwargs) -> Any:
        raise NotImplementedError