import json
import random
import argparse

def generate_random_name(label):
    if label == "PERSON":
        title = random.choice(["Mr.", "Mrs."])
        name = chr(random.randint(65, 90))
        return f"{title} {name}"
    elif label == "COMPANY":
        return f"Company {chr(random.randint(65, 90))}"

def main(nodes_count, edges_count):
    nodes = []
    edges = []
    max_node_id = nodes_count

    # Generate nodes
    for i in range(1, nodes_count + 1):
        label = random.choice(["PERSON", "COMPANY"])
        name = generate_random_name(label)
        nodes.append({"data": {"id": i, "label": label, "name": name}})

    # Generate edges
    for j in range(max_node_id + 1, max_node_id + edges_count + 1):
        source_id = random.randint(1, nodes_count)
        target_id = random.randint(1, nodes_count)
        label = random.choice(["FOUNDER", "CEO", "EMPLOYEE", "PARTNER"])
        edges.append({"data": {"id": j, "label": label, "source": source_id, "target": target_id}})

    # Combine into a single dictionary
    graph_data = {
        "nodes": nodes,
        "edges": edges
    }

    # Write data to JSON file
    with open('./data/pseudo-1000.json', 'w') as file:
        json.dump(graph_data, file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate random network data")
    parser.add_argument('--nodes', type=int, default=200, help='Number of nodes')
    parser.add_argument('--edges', type=int, default=200, help='Number of edges')
    args = parser.parse_args()

    main(args.nodes, args.edges)

# python src/generate-data.py --nodes 300 --edges 300