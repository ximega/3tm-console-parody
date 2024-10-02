class Depot:
    def __init__(self, number: int) -> None:
        self.number = number
        self.routes: list[int] = []
        self.bus_depot_nums: list[int] = []
        
    def add_routes(self, *routes: int) -> None:
        self.routes.extend(routes)
    
    def remove_routes(self, *routes: int) -> None:
        for route in routes:
            try:
                self.routes.remove(route)
            except ValueError:
                pass
        
    def add_buses(self, *buses: int) -> None:
        self.bus_depot_nums.extend(buses)
        
    def remove_buses(self, *buses: int) -> None:
        for bus in buses:
            try:
                self.bus_depot_nums.remove(bus)
            except ValueError:
                pass
            
    def rename(self, new_number: int) -> None:
        self.number = new_number