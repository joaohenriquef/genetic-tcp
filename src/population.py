from tour import Tour
from graph import Graph

# Represents a population of Tours, from which the optimal one will spawn and be chosen
class Population:
    # Initializes population
    # 'initialise' flag may be 'False' when individual generation is not neededt 
    def __init__(self, population_size: int, graph: 'Graph', initialise: bool = True):
        self.tours = []

        for _ in range(0, population_size):
            newTour = Tour(graph.number_of_cities())
            self.tours.append(newTour)
        if initialise:
            for tour in self.tours:
                tour.generate_individual(graph)
    
    # Returns tour od corresponding index
    def get_tour(self, tour_index: int) -> 'Tour':
        return self.tours[tour_index]
    
    # Returns the fittest tour in the population
    def get_fittest(self) -> 'Tour':
        fittest = self.tours[0]
        for tour in self.tours:
            if tour.get_fitness() > fittest.get_fitness():
                fittest = tour
        return fittest
    
    # Returns the number of tours in population
    def get_population_size(self) -> int:
        return len(self.tours)

    # Adds tour to desired index in population
    def save_tour(self, index: int, tour: 'Tour'):
        self.tours[index] = tour