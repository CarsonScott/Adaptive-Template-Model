# A Framework for Template-Matching in Topological Space

In the past, template-matching has traditionally been useful in machine-learning problems where digital images are being processed in order to detect visual patterns. The most basic example of which deals with a (typically small) two-dimensional filter being slid across an image surface in order to detect low-level patterns of black and white pixels. 

Pattern recognition through template-matching is currently restricted in that it is only useful when dealing with vector spaces. Unfortunately, problems of higher complexity are associated with patterns beyond spacetime, and tend toward more conceptually abstract relations. 

In the following framework I propose a way to extend the template-matching process beyond vector space, and rather to operate on topological spaces like networks and graphs. The main goal is to propose a possible system for future algorithms to comprehend more complex patterns using template-matching processes, in an attempt to minimize there computational expense of high-level pattern recognition.  

## 1. Templates

**_1.1 Graph Templates_**

A graph template (GT) is a subgraph that compares its topology with another graph. The output of a GT is a decimal value measuring the similarity between the input graph and the GT. Similarity is calculated by finding the number of nodes in the input graph that share a topology with a given node in the template graph, then dividing by the total number of nodes in the input graph.

Both the input and template graphs are equipped with origin nodes. An origin is simply a node in a graph that is viewed as its position or center. The origin of the template graph is aligned with that of the input graph, which allows a comparison to be made in order to calculate the similarity value.

**_1.2 Sliding Graph Templates_**

A sliding graph template (SGT) is a GT that traverses a larger graph and compares its topology with the local subgraph of each node in the walk. The output of a SGT is a graph where each node has an assigned decimal value measuring the similarity between the local subgraph of the input a given node and the GT. 

The position of an SGT with respect to the input graph is measured by its origin node. The SGT traverses from node-to-node each step by moving its origin from the current or center node to one of its neighbors. This means that at each step along the walk, the SGT chooses one node from the local subgraph to become the center node of the next step (and consequently, the local subgraph at every step includes the center node of the previous step).
