from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from reviews.models import Employee, Position


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ['name',]

    def validate_name(self, value):
        position = Position.objects.get(name=value)
        if not position:
            raise ValidationError("Должность не найдена.")
        return position


class ReadEmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'patronymic',
                  'position', 'is_fired', 'fire_date')


class WriteEmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'patronymic',
                  'position', 'is_fired', 'fire_date')

    def create(self, validated_data):
        position = validated_data.pop('position')
        employee = Employee.objects.create(**validated_data)
        employee.position.set(position)
        return employee
