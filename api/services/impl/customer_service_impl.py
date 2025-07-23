from ..customer_service import Customer_Service
from ...models.customer import Customer
from django.utils import timezone

class Customer_Service_Impl(Customer_Service):
    def add_customer(self, data):
        customer = Customer(
            name=data['name'],
            email=data.get('email'),
            phone_number=data.get('phone_number'),
            address=data.get('address'),
            national_id=data.get('national_id'),
            date_of_birth=data['date_of_birth'],
            created_at=timezone.now()
        )
        customer.save()
        return customer

    def get_customer_by_id(self, customer_id):
        customer = Customer.objects.filter(id=customer_id).first()
        return customer

    def update_customer(self, customer_id, data):
        pass

    def delete_customer(self, customer_id):
        pass


