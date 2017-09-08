# A Framework for Template-Matching in Topological Space

Traditionally, template-matching algorithms have been used for things like digital image processing and visual pattern recognition. One simple example of this deals with taking a (typically very small) two-dimensional filter and sliding it across an image in order to detect low-level patterns of black-and-white pixels. 

Pattern recognition through template-matching is currently restricted in that it is only useful when dealing with vector spaces. However, problems of high complexity tend to deal with conceptually abstract relations and not with patterns dependent on spacetime. 

In the following framework, I propose a feasible solution for extending template-matching methods to topological space, like graphs and networks. The main objective is to ultimately uncover a mechanism for complex pattern recognition that uses template-matching methods, as this may substantially reduce the computational resources required for high-level pattern recognition.  

## 1) Templates

**_1.1 Graph Templates_**

A graph template (GT) is a graph that compares its topology with another graph. The output of a GT is a decimal value measuring the similarity between the input graph and the GT. Similarity is calculated by finding the number of nodes in the input graph that share a topology with a given node in the template graph, then dividing by the total number of nodes in the input graph.

Both the input and template graphs are equipped with origin nodes. An origin is simply a node in the graph which is viewed as its center or position. The origin of the template graph is aligned with that of the input graph, which allows a comparison to be made in order to calculate the similarity value.

![](https://github.com/CarsonScott/Topological-Template-Matching/blob/master/img/template.png)

**_1.2 Sliding Graph Templates_**

A sliding graph template (SGT) is a GT that traverses a larger graph and compares its topology with the local subgraph of each node in the walk. The output of a SGT is a graph where each node has an assigned decimal value measuring the similarity between the local subgraph of the input of a given node and the GT. 

The position of an SGT with respect to the input graph is measured by its origin node. The SGT traverses from node-to-node each step by moving its origin from the current or center node to one of its neighbors. This means that at each step along the walk, the SGT chooses one node from the local subgraph to become the center node of the next step (and consequently, the local subgraph at every step includes the center node of the previous step).
