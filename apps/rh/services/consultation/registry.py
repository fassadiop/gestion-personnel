from typing import Dict, Type


class ConsultationRegistry:
    """
    Registre des providers de consultation.
    """

    _providers: Dict[str, Type] = {}

    @classmethod
    def register(cls, name: str, provider: Type) -> None:
        cls._providers[name] = provider

    @classmethod
    def get(cls, name: str) -> Type:
        try:
            return cls._providers[name]
        except KeyError:
            raise ValueError(
                f"Aucun provider de consultation enregistré pour '{name}'."
            )