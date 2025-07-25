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
        customer = Customer.objects.get(id=customer_id)
        return customer

    def update_customer(self, data):
        try:
            customer = Customer.objects.get(id=data['id'])
        except:
            return None

        allowed_fields = ['name', 'email', 'phone_number', 'address', 'national_id', 'date_of_birth']
        for field in allowed_fields:
            if field in data and data[field] is not None:
                setattr(customer, field, data[field])

        customer.updated_at = timezone.now()
        customer.save()
        return customer

    def delete_customer(self, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
        except:
            return None
        customer.delete()
        return customer

    def search_customer(self,data):
        pass


