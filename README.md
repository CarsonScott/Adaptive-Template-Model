# A Framework for Template-Matching in Topological Space

Template-matching algorithms have traditionally been used in machine-learning for things like digital image processing, in which usually small, two-dimensional filters are slid across images to detect low-level patterns of visual stimuli. 

These pattern-recognition methods are restricted in that they are limited to only work on vector spaces. Here I propose a framework for extending this template-matching mechanism to topological spaces such as networks and graphs, and potentially allowing the comprehension of more complex patterns that exist independently from their spatiotemporal properties.  

## 1. Templates

**_1.1 Graph Templates_**

A graph template (GT) is a subgraph that compares its topology with another graph. The output of a GT is a decimal value measuring the similarity between the input graph and the GT. Similarity is calculated by finding the number of nodes in the input graph that share a topology with a given node in the template graph, then dividing by the total number of nodes in the input graph.

Both the input and template graphs are equipped with origin nodes. An origin is simply a node in a graph that is viewed as its position or center. The origin of the template graph is aligned with that of the input graph, which allows a comparison to be made in order to calculate the similarity value.

**_1.2 Sliding Graph Templates_**

A sliding graph template (SGT) is a GT that traverses a larger graph and compares its topology with the local subgraph of each node in the walk. The output of a SGT is a graph where each node has an assigned decimal value measuring the similarity between the local subgraph of the input a given node and the GT. 

The position of an SGT with respect to the input graph is measured by its origin node. The SGT traverses from node-to-node each step by moving its origin from the current or center node to one of its neighbors. This means that at each step along the walk, the SGT chooses one node from the local subgraph to become the center node of the next step (and consequently, the local subgraph at every step includes the center node of the previous step).
