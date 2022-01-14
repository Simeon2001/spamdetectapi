from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from data.predict import predict

# Create your views here.
@api_view(['post'])
def predict_it(request):
    if request.method == "POST":
        message = str(request.data.get("msg"))
        value = predict(message)
    return Response (
                {
                    "message": value,
                    "status":True
                }
            )