

````markdown
# Shortestpath Package

Welcome to the **Shortestpath Package**!  
This Python package implements Dijkstra's algorithm to calculate the shortest path in a weighted graph. It is developed as part of a GMT211 assignment and extended with documentation, testing, and packaging features.

---

## 🚀 Develop a New Feature

### ✨ Feature: `dijkstra()` Function

This project introduces a `dijkstra()` function to compute the shortest distances from a given start node to all other nodes in a graph.

```python
def dijkstra(graph, start):
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        unvisited_nodes = {node: shortest_distances[node] for node in graph if node not in visited}
        current_node = min(unvisited_nodes, key=unvisited_nodes.get)
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            new_distance = shortest_distances[current_node] + weight
            if new_distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = new_distance

    return shortest_distances
````

**Purpose:** This function finds the shortest path from the start node to all others. It's useful in routing systems, logistics, and optimization problems.

---

## 🧪 Testing with GitHub Actions

All test cases are written using `pytest`.
A GitHub Actions workflow (`python-test.yml`) runs the tests on every push to ensure stability.

```bash
pytest
```

Sample test:

```python
def test_dijkstra_simple_graph():
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    expected = {'A': 0, 'B': 1, 'C': 3, 'D': 4}
    result = dijkstra(graph, 'A')
    assert result == expected
```

GitHub Actions status: ✅ Success

> [See GitHub Actions tab](https://github.com/beyzoren/shortestpath_package/actions)

---

## 📚 Documentation with Sphinx

Documentation has been generated with **Sphinx**.

📷 Sample screenshot:

![Documentation Screenshot](docs/sphinx_screenshot.png)

🔗 **HTML Documentation Index:**
[Click to open index.html](docs/build/html/index.html)

---

## 🔍 Bonus: Logging Feature

Although optional, a basic logging mechanism is added to track algorithm steps:

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info(f"Visiting {current_node} with current shortest distance {shortest_distances[current_node]}")
```

**Benefits:**
Helps understand the internal steps of Dijkstra's execution — great for debugging or educational purposes.

---

## 🤖 AI Usage Disclosure

This project received limited support from **ChatGPT** to:

* Write boilerplate code
* Generate documentation sections
* Fix syntax issues
* Translate instructions

All logic, design, testing, and content were created, reviewed, and validated by the developer manually.

---

## 📦 Installation (TestPyPI)

```bash
pip install --index-url https://test.pypi.org/simple/ shortestpath2200674051
```

---

## 👩‍💻 Author

* **Name:** Beyza Ören
* **School ID:** 2200674051
* **Email:** [beyzaren58@hotmail.com](mailto:beyzaren58@hotmail.com)

---

> Project for GMT211 – Data Structures and Algorithms

