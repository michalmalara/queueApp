from abc import ABC, abstractmethod


class NotificationProviderAbstract(ABC):
    @abstractmethod
    def update_queue_info(self, queue_id: str, queue_data: dict) -> None:
        raise NotImplementedError
