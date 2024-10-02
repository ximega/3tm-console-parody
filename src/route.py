from src.bus import BusStop, Bus


class Route:
    def __init__(self, number: int, depot: int) -> None:
        self.number = number
        self.depot = depot
        self.buses: list[Bus] = []
        self.stops: list[BusStop] = []
        
    def add_buses(self, *buses: Bus) -> None:
        self.buses.extend(buses)
    
    def remove_buses(self, *bus_ids: int) -> None:
        for bus_id in bus_ids:
            try:
                self.buses.pop([bus.id for bus in self.buses].index(bus_id))
            except ValueError:
                pass
    
    def add_stops(self, *stops: BusStop) -> None:
        self.stops.extend([stop for stop in stops])
        
    def remove_stops(self, *stop_ids: int) -> None:
        for stop_id in stop_ids:
            try:
                self.stops.pop([stop.id for stop in self.stops].index(stop_id))
            except ValueError:
                pass
            
    def rename(self, new_number: int) -> None:
        self.number = new_number
        
    def transfer(self, new_depot: int) -> None:
        self.depot = new_depot