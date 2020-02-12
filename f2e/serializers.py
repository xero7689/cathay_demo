from django.core.serializers.python import Serializer

class OrdersPythonSerializer(Serializer):
    def end_object(self, obj):
        self._current['deal_type'] = obj.deal_type
        self._current['date'] = obj.date.strftime('%Y-%m-%d %H:%M:%S')
        self.objects.append(self._current)

