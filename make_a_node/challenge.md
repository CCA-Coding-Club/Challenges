---
title: Make a Node
date: 2026-07-10
description: Learn what a node is and how it's made in the context of back-end development.
---

# Make a Node

A node is an object that exists within a space that contains other nodes. In this space there exists only nodes, and connections. A node can be conected
to another node and that node can also be connected back. However, imaging the way forward and back like a one way street. If there is only a forward connection
between nodes you can only go forward and not back again. Now lets say we have three nodes A, B, and C. Node A points(is connected) to node B. Node B points to
Node C. Finally, Node C points to node A. Here we've created a triangle in which you can only walk between connections in one direction.
    You can theoretically have a space with an infinite number of nodes and connections between those nodes. A connection can be 100miles long or 2 inches
in node space it is irrelevent and either connection distance would be functionally the same. Now, what are some applications such a space containing nodes and connections?
One could be the internet, another could be a book that references another book. Here I want you to make a node that can be referenced by a list.

- A node is a simple mental construct with as many values as you wish to assign it. It can be made real, or left entirely theoretical.

## Part 1: Linear node ⭐ Easy

Make a node from a class that can point to a previous node or the next node in front of it. This would be a node that is designed to exist in a 1-D linear space.
for example

 Node1('cat') --> Node2('Dog') --> Node3('Lizard') --> Node4('Hamster')
              <--              <--  


> 💡 I recommend making a class and defining some functions that save a value or node's position to separate constructed values.

## Part 2: 2-D node ⭐ Medium

Make a node that can reference and be referenced in 2-D space. This means that the node should be able to hold an arbitrary number of connections to other nodes.

- Make that node more betterer!
- Get **Creative** wit it.
- 
- 

## Concepts Practiced

- Classes
- Object oriented programming
- Node logic
- Node space understanding