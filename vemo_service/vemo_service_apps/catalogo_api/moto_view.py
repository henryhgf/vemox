from rest_framework import serializers, viewsets

from vemo_service_apps.catalogo.models.moto import Moto


class MotoSerializer(serializers.ModelSerializer):

    # motor_nombre = serializers.ReadOnlyField(
    #     source='motor.marca')

    class Meta:
    	model = Moto
        fields = '__all__'
        

class MotoViewSet(viewsets.ModelViewSet):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer

    # def get_queryset(self):
    #     query = self.request.query_params.get('query', '')
    #     queryall = (Q(id__icontains=query),
    #                 Q(nombre__icontains=query))
    #     queryset = self.queryset.filter(reduce(OR, queryall))
    #     return queryset