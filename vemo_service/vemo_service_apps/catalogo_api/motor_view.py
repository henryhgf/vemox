from rest_framework import serializers, viewsets

from vemo_service_apps.catalogo.models.motor import Motor


class MotorSerializer(serializers.ModelSerializer):

    # motor_nombre = serializers.ReadOnlyField(
    #     source='motor.marca')

    class Meta:
        
        model = Motor
        fields = '__all__'

class MotorViewSet(viewsets.ModelViewSet):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer

    # def get_queryset(self):
    #     query = self.request.query_params.get('query', '')
    #     queryall = (Q(id__icontains=query),
    #                 Q(nombre__icontains=query))
    #     queryset = self.queryset.filter(reduce(OR, queryall))
    #     return queryset