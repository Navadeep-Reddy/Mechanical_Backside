import networkx as nx
import matplotlib.pyplot as plt

class RepairGraph:
    def __init__(self):
        # Initialize an empty directed graph
        self.graph = nx.DiGraph()
    
    def add_repair(self, repair, related_repairs):
        # Add edges from repair to each related repair
        for related_repair in related_repairs:
            self.graph.add_edge(repair, related_repair)
    
    def next_related_repair(self, repair):
        # Return the next related repairs if they exist
        return list(self.graph.successors(repair))
    
    def display_graph(self):
        # Draw the graph using matplotlib
        pos = nx.spring_layout(self.graph)  # positions for all nodes
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=3000, edge_color='gray', font_size=10, font_weight='bold')
        plt.title("Vehicle Repair Graph")
        plt.show()


def bike_graph():
    repair_graph = RepairGraph()

    # Add repairs and their related repairs as edges to the graph 
    repair_graph.add_repair("Tire Repair", ["Frame", "Suspension"])
    repair_graph.add_repair("Gear Adjustment", ["Lubrication"])
    repair_graph.add_repair("Brake Checkup", ["Tire Repair"])
    repair_graph.add_repair("Chain Maintenance", ["Drivetrain", "Lubrication"])
    repair_graph.add_repair("Suspension", ["Frame", "Tire Repair", "Wheel Truing"])
    repair_graph.add_repair("Drivetrain", ["Gear Adjustment", "Lubrication"])
    repair_graph.add_repair("Engine Checkup", ["Gear Adjustment", "Drivetrain"])

    return repair_graph

def car_graph():
    repair_graph = RepairGraph()

    # Add repairs and their related repairs as edges to the graph 
    repair_graph.add_repair("Brake Checkup", ["Suspension", "Tire Checkup"])
    repair_graph.add_repair("Suspension", ["Frame", "Tire Checkup"])
    repair_graph.add_repair("Tire Checkup", ["Brake Checkup", "Fuel Injector"])
    repair_graph.add_repair("Fuel Injector", ["Engine Maintenance"])
    repair_graph.add_repair("Transmission", ["Engine Maintenance", "Fuel Injector", "Drivetrain"])
    repair_graph.add_repair("Drivetrain", ["Engine Maintenance", "Transmission"])

    return repair_graph

def cycle_graph():
    # Initialize the repair graph
    repair_graph = RepairGraph()

    # Add repairs and their related repairs to the graph 
    repair_graph.add_repair("Tire Puncture", ["Wheel Checkup", "Tube Replacement"])
    repair_graph.add_repair("Brake Adjustment", ["Wheel Checkup", "Brake Pad"])
    repair_graph.add_repair("Frame", ["Headset Adjustment", "Wheel Checkup", "Lubrication", "Suspension"])
    repair_graph.add_repair("Suspension", ["Brake Adjustment", "Frame"])

    return repair_graph


if __name__ == "__main__":
    a = cycle_graph().display_graph()
    b = bike_graph().display_graph()
    c = car_graph().display_graph()

