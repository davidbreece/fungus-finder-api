from rest_framework.serializers import HyperlinkedModelSerializer
from api.models import Mushroom

class FungusSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Mushroom
        fields = ('id', 'name', 'image_link','wiki_link','kingdom','division','cclass',
            'order', 'family', 'genus', 'species', 'cap_shapes', 'hymenium_types',
            'gill_types', 'stipe_characters', 'sporeprint_colors', 'ecologies',
            'edibility')
        extra_kwargs = {
            'id': {'read_only': True}
        }