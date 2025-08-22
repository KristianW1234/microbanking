from rest_framework.decorators import api_view
from ..services.impl.customer_service_impl import Customer_Service_Impl
from rest_framework.response import Response
from ..serializers.customer_serializer import Customer_Serializer

@api_view(["POST"])
def add_customer(request):
    data = request.data
    service = Customer_Service_Impl()
    customer = service.add_customer(data)
    return Response({
        "status": 200,
        "message": "Customer added.",
        "data": Customer_Serializer(customer).data
    })


@api_view(["GET"])
def get_customer_by_id(_, customer_id): #request parameter can be replaced with '_' if you don't want to do anything about it.

    service = Customer_Service_Impl()
    customer = service.get_customer_by_id(customer_id)

    if customer is None:
        return Response({
            "status": 404,
            "message": "Customer not found",
            "data": None
        }, status=404)

    return Response({
        "status": 200,
        "message": "Customer retrieved",
        "data": Customer_Serializer(customer).data
    }, status=200)

@api_view(["PATCH"])
def update_customer(request):
    data = request.data
    service = Customer_Service_Impl()
    customer = service.update_customer(data)

    if customer is None:
        return Response({
            "status": 404,
            "message": "Customer not found",
            "data": None
        }, status=404)

    return Response({
        "status": 200,
        "message": "Customer updated",
        "data": Customer_Serializer(customer).data
    }, status=200)

@api_view(["DELETE"])
def delete_customer(_, customer_id):

    service = Customer_Service_Impl()
    customer = service.delete_customer(customer_id)

    if customer is None:
        return Response({
            "status": 404,
            "message": "Customer not found",
            "data": None
        }, status=404)

    return Response({
        "status": 200,
        "message": "Customer deleted",
        "data": Customer_Serializer(customer).data
    }, status=200)

@api_view(["GET"])
def search_customer(request):
    query_params = request.GET
    service = Customer_Service_Impl()
    customers = service.search_customer(query_params)
    customers_found = len(customers)
    res_status = 200
    res_message = str(customers_found) + " Customers found."
    if customers_found == 1:
        res_message = "1 Customer found"
    elif customers_found == 0:
        res_status = 404
        res_message = "Customer not found"
    return Response({
        "status": res_status,
        "message": res_message,
        "data": Customer_Serializer(customers, many=True).data
    })