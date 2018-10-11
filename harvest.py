############
# Part 1   #
############

from pprint import pprint 

class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest=first_harvest
        self.color=color
        self.is_seedless=is_seedless
        self.is_bestseller = is_bestseller
        self.name=name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        return None

   
    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        return None 

    def __repr__(self):
        return "Code: {}, First harvest: {}, Color: {}, Seedless: {}, bestseller: {}, name: {}".format(self.code, 
        self.first_harvest, self.color, self.is_seedless, self.is_bestseller,self.name)


def make_melon_types():
    """Returns a list of current melon types."""
    muskemelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    muskemelon.add_pairing("mint")

    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")

    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    crenshaw.add_pairing("proscuitto")

    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True,
                                                    "Yellow Watermellon")
    yellow_watermelon.add_pairing("ice cream")



    all_melon_types = [muskemelon, casaba, crenshaw, yellow_watermelon]

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(melon.name, "pairs with:")
        for pairing in melon.pairings:
            print("-", pairing)
    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_reporting_codes = {}
    for melon in melon_types:
        melon_reporting_codes[melon.code] = melon

    return melon_reporting_codes

############
# Part 2   #
############

class Melon:
    """A melon in a melon harvest."""
    def __init__(self, MelonType_object, shape_rating, color_rating, harvest_field, harvested_by):

        self.melon_type   = MelonType_object
        self.shape_rating  = shape_rating
        self.color_rating  = color_rating
        self.harvest_field = harvest_field
        self.harvested_by  = harvested_by

    def is_sellable(self):
        return self.shape_rating > 5 and self.color_rating > 5 and self.harvest_field !=3

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    #melon_type_list = MelonType.make_melon_types()
    melons_by_id = make_melon_type_lookup(melon_types)

   
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    return [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:   
        if melon.is_sellable():
            sellable = "(CAN BE SOLD)"
        else:
            sellable = "(NOT SELLABLE)"
        print("Harvested by {} from Field {}.{}".format(melon.harvested_by, melon.harvest_field, sellable))


