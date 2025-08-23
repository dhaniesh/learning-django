from rest_framework import serializers
from flightApp.models import Flight, Passenger, Reservation

# Method 3: using custom method validators def validate_<fieldname>
def validate_email(request):
    if '@' not in request['email']:
        raise serializers.ValidationError(
            "Invalid email pattern, email must contain @")


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

        # Method 3: using custom method validators def validate_<fieldname>
        # validators = [validate_email]

    # Method 1: using specific field validators def validate_<fieldname>
    def validate_email(self, email):
        if '@' not in email:
            raise serializers.ValidationError(
                "Invalid email pattern, email must contain @")

    # Method 2: Built in validators
    def validate(self, request):
        if '@' not in request['email']:
            raise serializers.ValidationError(
                "Invalid email pattern, email must contain @")


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
