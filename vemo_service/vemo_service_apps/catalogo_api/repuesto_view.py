from rest_framework import serializers, viewsets

from vemo_service_apps.catalogo.models.repuesto import Repuesto


class RepuestoSerializer(serializers.ModelSerializer):

    # Repuestor_nombre = serializers.ReadOnlyField(
    #     source='Repuestor.marca')

    class Meta:

    	model = Repuesto
        fields = '__all__'
        



class RepuestoViewSet(viewsets.ModelViewSet):
    queryset = Repuesto.objects.all()
    serializer_class = RepuestoSerializer

    # def get_queryset(self):
    #     query = self.request.query_params.get('query', '')
    #     queryall = (Q(id__icontains=query),
    #                 Q(nombre__icontains=query))
    #     queryset = self.queryset.filter(reduce(OR, queryall))
    #     return queryset