from src.bus import *
from src.depot import *
from src.route import *
from src.utils import *

class City:
    def __init__(self, name: str) -> None:
        self.name = name
        self.depots: list[Depot] = []
        self.routes: list[Route] = []
        self.buses: list[Bus] = []
        
    def add_depots(self, *depots: Depot) -> None:
        self.depots.extend(depots)
    
    def add_routes(self, *routes: Route) -> None:
        self.routes.extend(routes)
        
    def add_buses(self, *buses: Bus) -> None:
        self.buses.extend(buses)
        
    def demolish_depot(self, depot_num: int) -> None:
        depot = self.depots[[depot.number for depot in self.depots].index(depot_num)]
        
        if len(depot.bus_depot_nums) > 0:
            raise MonitoringError("You can't delete a depot as long as it's not free of buses")
        
        del self.depots[[depot.number for depot in self.depots].index(depot_num)]
        del depot
        
    def close_route(self, route_num: int) -> None:
        pass