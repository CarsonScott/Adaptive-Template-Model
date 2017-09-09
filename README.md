# Adaptive Template Model of Intelligence

## 1. Introduction

**_1.1) Problem Overview_**

Traditionally, template-matching algorithms have been used for things like digital image processing and visual pattern recognition. One simple example of this deals with taking a (typically very small) two-dimensional filter and sliding it across an image in order to detect low-level patterns of black-and-white pixels. 

Pattern recognition through template-matching is currently restricted in that it is only useful when dealing with vector spaces. However, problems of high complexity tend to deal with conceptually abstract relations and not with patterns dependent on space-time.

**_1.2) System Objectives_**

In the following framework, I propose a feasible solution for extending template-matching methods to topological space, like graphs and networks. The two main objectives are: 1. to uncover a mechanism for complex pattern recognition that uses template-matching methods, as this may substantially reduce the computational resources required for high-level pattern recognition, and 2. to provide a universal method of analogical processing that can be applied across all types of information.

***

## 2. Graphs

**_2.1) Graph Components_**

A graph is a collection of nodes connected by links, each with a certain set of properties than can take one of a finite amount of values at any given time. Every node in a graph has the same set of properties as every other node, and the same goes for links as well. Each graph is equipped with two property sets: one for nodes and one for links. While every component of one type shares an identical set of properties with the rest, its values can vary from node-to-node or link-to-link.


**_2.2) Component Properties_**

Any two graphs that have identical property sets are said to be compatible. That is, they are similar enough to compare with one another. A comparison between graphs is a measurement of similarity between them. Similarity refers to number of attributes shared between two graphs, with respect to the number of attributes held by only one graph or the other.

Attributes not only references the properties of a graph’s nodes and links, but also the topology of the graph. This means that the connectivity of nodes and links can be regarded as a property itself, not specific to any one component but rather an attribute of the graph as a unified object.

***

## 3. Templates

**_3.1) Template Graphs_**

A template graph is a graph that compares itself to another graph, called the input graph, by calculating a measurement call the similarity value. The input and template graphs are each equipped with an origin node, which is simply a node that acts as a universal reference point to the rest of the graph. The origin nodes are aligned and a comparison is made between them, resulting in said similarity value. This value measures the correspondence between a given input graph with the template graph, and thus presents information about a graph through a comparative process, rather than simply conveying information about the graph in isolation. 

![](https://github.com/CarsonScott/Topological-Template-Matching/blob/master/img/template.png)

**_3.2) Sliding Templates_**

A sliding template is a template graph that traverses a larger graph and compares itself to the local subgraph around each node along the walk. The output of a sliding template is a graph where each node has an assigned similarity value in reference to the local subgraph around a specific input node. 

Sliding templates at any point along their walk can be located using their origin nodes. They traverse a graph by moving their origin from the current or center node on the input graph to align with one of its connected neighbors. This means that each step along its walk, a sliding template selects a single node from the local subgraph, which then becomes the new center node (resulting in the previous center node becoming part of the new local subgraph).

***

## 4. Comparisons

**_4.1) Comparison Operators_**

To better explain the abstract notion of taking two graphs and making some comparison between them, we’ll go through some simple examples (It might also be comforting to know that we’re barely stepping outside the realm of basic set theory). The process of “comparison” as we’ve discussed requires little more than elementary binary operations that you are probably familiar with. The following shows three examples of how binary operations are used to compare graphs whose nodes have exhibit a property of color.

![](https://github.com/CarsonScott/Topological-Template-Matching/blob/master/img/operations.png)

**_4.2) Applied Comparisons_**

Now, we’ll take this idea a step further and use a sliding template on a large graph to show how topological properties are detected during a traversal. We will use a simple graph template that consists of an origin node along with three neighbors.

![](https://github.com/CarsonScott/Topological-Template-Matching/blob/master/img/example.png)

The left image shows the input graph, and the right a color-coded version of the output graph. Each node is shaded according to the calculation of similarity at that point on the input graph. In the right upperhand corner is a key that relates each color with the associated level of similarity. As you can see, nodes with exactly three neighbors received strong similarity values with those with greater or less than three received weaker values.

***

## 5. Agents
**_5.1) Agent Fitness_**

Agents are used to control the movement of sliding templates. During a walk, an agent observes the local environment, or subgraph, as well as a performance rating, or similarity measurement, and selects an action, or neighbor, which becomes the position at the next step. When the total value of similarity measurements along a walk is high, then the agent is said to have performed well. When the total is low, its said to have performed poorly.

Each agent has a finite memory space that it uses to store/retrieve information about the environment throughout a walk. Agents “earn” memory space by performing well, which means it can keep track of more information that it uses to make decisions about its movement during a walk. This means the agents that perform consistently well are rewarded with computational resources that help sustain those successful behaviors, while the lower-ranking agents are deprived of said resources which decreases their chance of survival.

**_5.2) Agent Evolution_**

Once an agent’s resources fall below a certain amount, it “goes extinct” and is removed from the population. On the other hand if the amount of resources exceeds a certain amount, the agent “reproduces” and creates a duplicate agent, where a small chance of mutation can lead to differences in the properties of its associated graph template. 

Since all computational systems have constraints on resources, an evolving population operates like a Darwinian zero-sums game, where the winners are the agents who can locate the greatest number of matching subgraphs during a walk.


## 6. Adaptations

**_6.1) Reproductive Adaptations_**

An elementary agent, the simplest type of agent, selects actions by measuring the similarity for each neighbor and simply moves in the toward the highest value. No additional memory space is required, however an elementary agent will still die if its memory space decreases below a certain point. 

The run-time of an elementary agent is brief unless it accumulates enough space to duplicate itself. This triggers the evolutionary process which potentially leads to brand new agents being formed, via mutations that occur in each new generation.

**_6.2) Generative Adaptations_**

When an elementary agent dies, its graph is replaced with the local subgraph around its last position. Agents rapidly pop in-and-out of existence, trying out new graphs until one takes hold. These graphs are called stable because they have the ability to sustain themselves for a relatively longer period of time.
