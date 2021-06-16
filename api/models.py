from __future__ import unicode_literals
from django.db import models
from multiselectfield import MultiSelectField
import requests
import random

CAP_SHAPES = (('campanulate', 'campanulate'),
                  ('conical', 'conical'),
                  ('convex', 'convex'),
                  ('depressed', 'depressed'),
                  ('flat', 'flat'),
                  ('infundibuliform', 'infundibuliform'),
                  ('offset', 'offset'),
                  ('ovate', 'ovate'),
                  ('umbilicate', 'umbilicate'),
                  ('umbonate', 'umbonate'),
                  ('no', 'no'),
                  ('na', 'NA'))

HYMENIUM_TYPES = (('gills', 'gills'),
                    ('pores', 'pores'),
                    ('smooth', 'smooth'),
                    ('ridges', 'ridges'),
                    ('teeth', 'teeth'),
                    ('gleba', 'gleba'))

GILL_TYPES = (('adnate', 'adnate'),
                ('adnexed', 'adnexed'),
                ('decurrent', 'decurrent'),
                ('emarginate', 'emarginate'),
                ('free', 'free'),
                ('seceding', 'seceding'),
                ('sinuate', 'sinuate'),
                ('subdecurrent', 'subdecurrent'),
                ('no', 'no'),
                ('na', 'NA'))

STIPE_CHARACTERS = (
                    ('bare', 'bare'),
                    ('ring', 'ring'),
                    ('volva', 'volva'),
                    ('ring-and-volva', 'ring and volva'),
                    ('cortina', 'cortina'),
                    ('na', 'NA'))

SPOREPRINT_COLORS = (('black', 'black'),
                    ('blackish-brown', 'blackish-brown'),
                    ('brown', 'brown'),
                    ('buff', 'buff'),
                    ('cream', 'cream'),
                    ('ochre', 'ochre'),
                    ('olive', 'olive'),
                    ('olive-brown', 'olive-brown'),
                    ('pink', 'pink'),
                    ('pinkish-brown', 'pinkish-brown'),
                    ('purple', 'purple'),
                    ('purple-black', 'purple-black'),
                    ('purple-brown', 'purple-brown'),
                    ('reddish-brown', 'reddish-brown'),
                    ('salmon', 'salmon'),
                    ('tan', 'tan'),
                    ('white', 'white'),
                    ('yellow', 'yellow'),
                    ('yellow-orange', 'yellow-orange'),
                    ('yellow-brown', 'yellow-brown'))

ECOLOGIES = (('mycorrhizal', 'mycorrhizal'),
            ('parasitic', 'parasitic'),
            ('saprotrophic', 'saprotrophic'))

EDIBILITY_TYPES = (('choice', 'choice'),
                    ('edible', 'edible'),
                    ('inedible', 'inedible'),    
                    ('unpalatable', 'unpalatable'),
                    ('caution', 'caution'),
                    ('psychoactive', 'psychoactive'),
                    ('poisonous', 'poisonous'),
                    ('allergenic', 'allergenic'),
                    ('deadly', 'deadly'),
                    ('unknown', 'unknown'))
        

class Mushroom(models.Model):

    class Meta:
        verbose_name_plural = "mushrooms"
        ordering = ['name']

    slug = models.SlugField
    name = models.CharField(max_length=255)
    image_link = models.URLField(max_length=512, blank=True, null=True)
    wiki_link = models.URLField(max_length=512, null=True, blank=True)
    kingdom = models.CharField(max_length=50, null=True, blank=True)
    division = models.CharField(max_length=50, null=True, blank=True)
    cclass = models.CharField(max_length=50, null=True, blank=True)
    order = models.CharField(max_length=50, null=True, blank=True)
    family = models.CharField(max_length=50, null=True, blank=True)
    genus = models.CharField(max_length=50, null=True, blank=True)
    species = models.CharField(max_length=50, null=True, blank=True)
    cap_shapes = MultiSelectField(choices=CAP_SHAPES, null=True, blank=True)
    hymenium_types = MultiSelectField(choices=HYMENIUM_TYPES, null=True, blank=True)
    gill_types = MultiSelectField(choices=GILL_TYPES, null=True, blank=True)
    stipe_characters = MultiSelectField(choices=STIPE_CHARACTERS, null=True, blank=True)
    sporeprint_colors = MultiSelectField(choices=SPOREPRINT_COLORS, null=True, blank=True)
    ecologies = MultiSelectField(choices=ECOLOGIES, null=True, blank=True)
    edibility = MultiSelectField(choices=EDIBILITY_TYPES, null=True, blank=True)
   
    def __str__(self):
        return self.name


class WikiUrl(models.Model):

    class Meta:
        verbose_name_plural = "wikiurls"
    
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.url
