# TROPHIC COHERENCE
# Alessio Pagani

## The following functions compute the trophic level of each node in a direct network.
## The trophic difference and the the trophic coherence (q) of the network are then computed.

## A detailed explanation on how to compute trophic levels ad trophic coherence can be found 
## on the paper "Resilience or robustness: identifying topological vulnerabilities in rail networks"
## https://royalsocietypublishing.org/doi/10.1098/rsos.181301

import numpy as np
import networkx as nx
import math


# compute the trophic level of each node
def compute_trophic_levels(DG):
    adj_mtrx = nx.to_numpy_matrix(DG)
    Kv = np.array([max(DG.in_degree(node), 1) for node in DG.nodes()])
    A = np.diag(Kv) - np.transpose(adj_mtrx)
    S = None
    if np.linalg.det(A) == 0:
        print('Error: Singular matrix')
        return None, None
    else:
        S = np.linalg.solve(A, Kv)
        trophic_levels = []
        idx = 0
        for node in DG.nodes():
            trophic_levels.append([node, S[idx]])
            DG.nodes()[node]['tr_lvl'] = float(S[idx])
            idx += 1
    return S, DG


# compute the trophic difference of each edge
def trophic_diff(DG):
    nodes = DG.nodes(data=True)
    trophic_diff = []
    for edge in DG.edges():
        t_diff = abs(nodes[edge[0]]['tr_lvl'] - nodes[edge[1]]['tr_lvl'])
        trophic_diff.append([edge, t_diff])
    return trophic_diff


# compute the trophic coherence (q)
def coherence_parameter(DG, tr_diff):
    q = 0
    for x in tr_diff:
        q += x[1] * x[1]
    q /= float(DG.number_of_edges())
    q = math.sqrt(q - 1)
    return q


# Comparison with null model
## The basal ensemble expectation (q') is used as a null model to compare the 
## results of different networks.
## The trophic incoherence measure q/q' has a value close to 1 when a network
## has a trophic coherence similar to a random expectation, it has a value 
## lower than 1 when the network is coherent while it has a value greater than
## 1 when the network is incoherent.


def basal_ensemble_expectation(DG):
    # number of edges connected to basal nodes
    L_b = 0
    basal_nodes, _ = get_basal_and_top_nodes(DG)
    for node in basal_nodes:
        L_b += len(DG.out_edges(node))
    q_b = math.sqrt(DG.number_of_edges() / float(L_b) - 1)
    return q_b


def get_basal_and_top_nodes(G):
    basal_nodes = []
    for node in G.nodes():
        if G.in_degree(node) == 0:
            basal_nodes.append(node)

    top_nodes = []
    for node in G.nodes():
        if G.out_degree(node) == 0:
            top_nodes.append(node)
    return basal_nodes, top_nodes
