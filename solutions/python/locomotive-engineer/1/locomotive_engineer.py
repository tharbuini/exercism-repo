"""Functions which helps the locomotive engineer to keep track of the train."""

def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    
    wagons = []
    for value in args:
        wagons.append(value)

    return wagons    

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    wagon_1, wagon_2 = each_wagons_id.pop(0), each_wagons_id.pop(0)

    each_wagons_id.append(wagon_1)
    each_wagons_id.append(wagon_2)
    
    index = each_wagons_id.index(1) 
    for wagon in missing_wagons[::-1]:
        each_wagons_id.insert(index + 1, wagon)
    
    return each_wagons_id

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    stops = list(kwargs.values())
    route.update({"stops": stops})
    
    return route
    
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """

    complete_route = []
    for key, value in route.items():
        complete_route.append([key, value])
    for key, value in more_route_information.items():
        complete_route.append([key, value])

    complete_route.sort()
    return dict(complete_route)

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    fixed_wagons = []
    for row in range(0, len(wagons_rows)):
        temporary_list = []
        for column in range(0, 3):
            temporary_list.append(wagons_rows[column][row])
        fixed_wagons.append(temporary_list)

    return fixed_wagons