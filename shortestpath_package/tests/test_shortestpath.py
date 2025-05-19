import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shortestpath.shortestpath import dijkstra

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
