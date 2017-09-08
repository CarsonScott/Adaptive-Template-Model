# A Framework for Template-Matching in Topological Space

Traditionally, template-matching algorithms have been used for things like digital image processing and visual pattern recognition. One simple example of this deals with taking a (typically very small) two-dimensional filter and sliding it across an image in order to detect low-level patterns of black-and-white pixels. 

Pattern recognition through template-matching is currently restricted in that it is only useful when dealing with vector spaces. However, problems of high complexity tend to deal with conceptually abstract relations and not with patterns dependent on space-time.

In the following framework, I propose a feasible solution for extending template-matching methods to topological space, like graphs and networks. The main objective is to ultimately uncover a mechanism for complex pattern recognition that uses template-matching methods, as this may substantially reduce the computational resources required for high-level pattern recognition.

## 1. Graphs

**_1.1) Graph Components_**

A graph is a collection of nodes connected by links, each with a certain set of properties than can take one of a finite amount of values at any given time. Every node in a graph has the same set of properties as every other node, and the same goes for links as well. Each graph is equipped with two property sets: one for nodes and one for links. While every component of one type shares an identical set of properties with the rest, its values can vary from node-to-node or link-to-link.

**_1.2) Graph Attributes_**

Any two graphs that have identical property sets are said to be compatible. That is, they are similar enough to compare with one another. A comparison between graphs is a measurement of similarity between them. Similarity refers to number of attributes shared between two graphs, with respect to the number of attributes held by only one graph or the other.

Attributes not only references the properties of a graph’s nodes and links, but also the topology of the graph. This means that the connectivity of nodes and links can be regarded as a property itself, not specific to any one component but rather an attribute of the graph as a unified object.

***

### 2. Templates

**_2.1) Template Graphs_**

A template graph is a graph that compares itself to another graph, called the input graph, by calculating a measurement call the similarity value. The input and template graphs are each equipped with an origin node, which is simply a node that acts as a universal reference point to the rest of the graph. The origin nodes are aligned and a comparison is made between them, resulting in said similarity value. This value measures the correspondence between a given input graph with the template graph, and thus presents information about a graph through a comparative process, rather than simply conveying information about the graph in isolation. 

**_2.2) Sliding Templates_**

A sliding template is a template graph that traverses a larger graph and compares itself to the local subgraph around each node along the walk. The output of a sliding template is a graph where each node has an assigned similarity value in reference to the local subgraph around a specific input node. 

Sliding templates at any point along their walk can be located using their origin nodes. They traverse a graph by moving their origin from the current or center node on the input graph to align with one of its connected neighbors. This means that each step along its walk, a sliding template selects a single node from the local subgraph, which then becomes the new center node (resulting in the previous center node becoming part of the new local subgraph).
