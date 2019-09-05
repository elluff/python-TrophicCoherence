import networkx as nx
import TrophicCoherence


# Example 1
## Hierarchical network. 4 basal nodes (1, 2, 3, 4) are connected 
## to 2 intermediate nodes (10, 20). The intermediate nodes are connected to a top node (100).

# Define the direct graph
G = nx.DiGraph()
G.add_edges_from([(1, 10), (2, 10), (3, 20), (4, 20), (10, 100), (20, 100)])
nx.draw_planar(G, with_labels=True, node_color="r", alpha = 0.7, arrowsize=20,
               node_size=500, font_weight="bold")

# Compute trophic coherence
_, G = TrophicCoherence.compute_trophic_levels(G)
labels = {}
for node in G.nodes(data=True):
    labels[node[0]] = node[1]['tr_lvl']
nx.draw_planar(G, labels = labels, with_labels=True, node_color="r", alpha = 0.7, arrowsize=20,
               node_size=500, font_weight="bold")

print("Example 1")
coherence = TrophicCoherence.coherence_parameter(G, TrophicCoherence.trophic_diff(G))
print("Coherence of the network: ", coherence)
basal_ensemble = TrophicCoherence.basal_ensemble_expectation(G)
print("Basal ensemble: ", basal_ensemble)
print("Normalized coherence", coherence / basal_ensemble)


# Example 2
## If a new edge is added between a basal node (4) and a top node (100), the trophic level of the nodes changes.

# Define the direct graph
G = nx.DiGraph()
G.add_edges_from([(1, 10), (3, 20), (4, 20), (4, 100), (10, 100), (20, 100)])
nx.draw_planar(G, with_labels=True, node_color="r", alpha = 0.7, arrowsize=20,
               node_size=500, font_weight="bold")

# Compute trophic coherence
_, G = TrophicCoherence.compute_trophic_levels(G)
labels = {}
for node in G.nodes(data=True):
    labels[node[0]] = node[1]['tr_lvl']
nx.draw_planar(G, labels = labels, with_labels=True, node_color="r", alpha = 0.7, arrowsize=20,
               node_size=500, font_weight="bold")

print("Example 2")
coherence = TrophicCoherence.coherence_parameter(G, TrophicCoherence.trophic_diff(G))
print("Coherence of the network: ", coherence)
basal_ensemble = TrophicCoherence.basal_ensemble_expectation(G)
print("Basal ensemble: ", basal_ensemble)
print("Normalized coherence", coherence / basal_ensemble)


# Example 3
## In this example a loop is added (between node 20 and node 100).
## Loops are one of the major causes of incoherence.

# Define the direct graph
G = nx.DiGraph()
G.add_edges_from([(1, 10), (2, 10), (3, 20), (4, 20), (10, 100), (20, 100), (100,20)])
nx.draw_planar(G, with_labels=True, node_color="r", alpha = 0.7, arrowsize=20,
               node_size=500, font_weight="bold")

# Compute trophic coherence
_, G = TrophicCoherence.compute_trophic_levels(G)
labels = {}
for node in G.nodes(data=True):
    labels[node[0]] = node[1]['tr_lvl']
nx.draw_planar(G, labels = labels, with_labels=True, node_color="r", alpha = 0.7, arrowsize=20,
               node_size=500, font_weight="bold")


print("Example 3")
coherence = TrophicCoherence.coherence_parameter(G, TrophicCoherence.trophic_diff(G))
print("Coherence of the network: ", coherence)
basal_ensemble = TrophicCoherence.basal_ensemble_expectation(G)
print("Basal ensemble: ", basal_ensemble)
print("Normalized coherence", coherence / basal_ensemble)


# Example 4
## In this example, a network with several loops is created.

# Define the direct graph
G = nx.DiGraph()
G.add_edges_from([(1, 100), (20, 10), (3, 20), (4, 10), (4, 20), (10, 100), (4, 100), (100,20), (100,1), (1,20)])
nx.draw_planar(G, with_labels=True, node_color="r", alpha = 0.7, arrowsize=20,
               node_size=500, font_weight="bold")

# Compute trophic coherence
_, G = TrophicCoherence.compute_trophic_levels(G)
labels = {}
for node in G.nodes(data=True):
    labels[node[0]] = node[1]['tr_lvl']
nx.draw_planar(G, labels = labels, with_labels=True, node_color="r", alpha = 0.7, arrowsize=20,
               node_size=500, font_weight="bold")

print("Example 4")
coherence = TrophicCoherence.coherence_parameter(G, TrophicCoherence.trophic_diff(G))
print("Coherence of the network: ", coherence)
basal_ensemble = TrophicCoherence.basal_ensemble_expectation(G)
print("Basal ensemble: ", basal_ensemble)
print("Normalized coherence", coherence / basal_ensemble)

