class Fungus(object):

    CAP_CHOICES = [
        'campanulate',
        'conical',
        'convex',
        'depressed',
        'flat',
        'infundibuliform',
        'offset',
        'ovate',
        'umbilicate',
        'umbonate',
    ]

    HYMENIUM_CHOICES = [
        'gills',
        'pores',
        'smooth',
        'ridges',
        'teeth',
        'gleba',
    ]

    GILL_CHOICES = [
        'adnate',
        'adnexed',
        'decurrent',
        'emarginate',
        'free',
        'seceding',
        'sinuate',
        'subdecurrent',
        'none',
        'N/A'
    ]
    
    STIPE_CHARACTER_CHOICES = [
        'bare',
        'ring',
        'volva',
        'ring and volva',
        'cortina',
        'N/A'
    ]

    SPOREPRINT_CHOICES = [
        'black',
        'blackish-brown',
        'brown',
        'buff',
        'cream',
        'ochre',
        'olive',
        'olive-brown',
        'pink',
        'pinkish-brown',
        'purple',
        'purple-black',
        'purple-brown',
        'reddish-brown',
        'salmon',
        'tan',
        'white',
        'yellow',
        'yellow-orange',
        'yellow-brown',
    ]

    ECOLOGICAL_CHOICES = [
        'mycorrhizal',
        'parasitic',
        'saprotrophic',
    ]

    EDIBLE_CHOICES = [
        'choice',
        'edible',
        'inedible',
        'unpalatable',
        'caution',
        'psychoactive',
        'poisonous',
        'allergenic',
        'deadly',
        'unknown'
    ]
    
    def __init__(self, 
                 name, 
                 image_url, 
                 wiki_link, 
                 kingdom, 
                 division,
                 cclass, 
                 order, 
                 family, 
                 genus, 
                 species, 
                 cap_shapes,
                 hymenium_types, 
                 gill_types, 
                 stipe_characters, 
                 sporeprint_colors,
                 ecology_types, 
                 how_edible):
        self.name = name
        self.image_url = image_url
        self.wiki_link = wiki_link
        self.kingdom = kingdom
        self.division = division
        self.cclass = cclass
        self.order = order
        self.family = family
        self.genus = genus
        self.species = species
        self.ecologies = ecology_types        
        self.cap_shapes = []
        for i in range(len(cap_shapes)):
            if cap_shapes[i] in cap_shapes:
                self.cap_shapes.append(cap_shapes[i])
        
        self.hymenium_types = []
        for hymenium_type in hymenium_types:
            if hymenium_type in self.HYMENIUM_CHOICES:
                self.hymenium_types.append(hymenium_type)
        
        self.gill_types = []
        for gill_type in gill_types:
            if gill_type in self.GILL_CHOICES:
                self.gill_types.append(gill_type)
                    
        self.stipe_characters = []
        for stipe_character in stipe_characters:
            if stipe_character in self.STIPE_CHARACTER_CHOICES:
                self.stipe_characters.append(stipe_character)
        
        self.sporeprint_colors = []
        for sporeprint_color in sporeprint_colors:
            if sporeprint_color in self.SPOREPRINT_CHOICES:
                self.sporeprint_colors.append(sporeprint_color)
                    
        self.ecology_types = []
        for ecology_type in ecology_types:
            if ecology_type in self.ECOLOGICAL_CHOICES:
                self.ecology_types.append(ecology_type)
                    
        self.how_edible = []
        for choice in how_edible:
            if choice in self.EDIBLE_CHOICES:
                self.how_edible.append(choice)

    def __str__(self):
        out = self.name + "\n" \
            + "Kingdom: " + self.kingdom
        return self.name


    # def details(self):
    #     out = "Name: " + self.name + \
    #
    #
