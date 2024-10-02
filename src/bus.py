from enum import Enum, auto


class BusStop:
    last_id = 0
    
    def __init__(self, name: str) -> None:
        BusStop.last_id += 1
        self.id = BusStop.last_id
        self.name = name
        # self.routes is stored 
        # in form of `type list[Route, RouteDirection]`, 
        # but Route will be int (number of route), RouteDirection is a string.
        # can't add it right here 
        # as it would cause errors with circular import
        self.routes: list[tuple[int, str]] = []
        # `type tuple[int, int]`
        # first int is a number of route
        # second int is a time in seconds of bus coming
        self.coming: list[tuple[int, int]]
        
    def set_route(self, *routes: tuple[int, str]) -> None:
        """
        `type direction: str`, 
        but it represents last bus stop of a route 
        in a form of string (w.m. BusStop.name) 
        
        `route` from `routes` is a composite of (route_num, direction)
        """
        
        for route in routes:
            self.routes.append(route)
            
    def demolish(self) -> None:
        while True:
            inp = input('Do you really want to demolish this bus stop? {}, {} [y / N]'.format(self.id, self.name))
            
            match inp:
                case 'y':
                    del self
                    break
                case 'N':
                    print('You canceled bus stop deconstruction')
                    break
                case _:
                    continue
                
    def __str__(self) -> str:
        return self.name
    
    def get_formatted_routes(self) -> str:
        return ", ".join([str(route[0]) for route in self.routes])


class BusTypes(Enum):
    YUT_ELEC = auto()
    YUT_CNG = auto()
    KK_CNG = auto()
    KK_ELEC = auto()
    MAN_CNG = auto()
    MER_LF = auto()

class Bus:
    last_id = 0
    
    def __init__(self, bus_type: BusTypes, gov_num: str, depot: int, depot_num: int) -> None:
        Bus.last_id += 1
        self.id = Bus.last_id
        self.bus_type = bus_type
        self.gov_num = gov_num
        self.depot = depot
        self.depot_num = depot_num
        # int represents time of arrival
        # None if bus won't come
        self.next_stop: None | tuple[BusStop, int | None] = None
        
    def set_next_stop(self, bus_stop: BusStop, time: int) -> None:
        self.next_stop = (bus_stop, time)
        
    def transfer(self, new_depot: int, new_depot_number: int):
        self.depot = new_depot
        self.depot_num = new_depot_number