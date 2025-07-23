from abc import ABC, abstractmethod

class Customer_Service(ABC):
    @abstractmethod
    def add_customer(self, data): pass

    @abstractmethod
    def get_customer_by_id(self, customer_id): pass

    @abstractmethod
    def update_customer(self, customer_id, data): pass

    @abstractmethod
    def delete_customer(self, customer_id): pass