from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from flightApp.models import Flight, Passenger, Reservation
from flightApp.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.views import Response
# Create your views here.


@api_view(['POST'])
def findFlights(request):
    flights = Flight.objects.filter(
        departureCity=request.data['departureCity'],
        arrivalCity=request.data['arrivalCity'],
        dateOfDeparture=request.data['dateOfDeparture']
    ).all()
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
