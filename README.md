

 📄 `README.md`

````markdown
# 📦 shortestpath_package

> 📍 A Python package for calculating the shortest paths on a directed, weighted graph using Dijkstra’s Algorithm.

---

 🔍 Purpose

This Python package was developed to **calculate the shortest paths from a source node to all other nodes** on a directed and weighted graph using **Dijkstra’s algorithm**.

The project was implemented as part of the **GMT211 - Data Structures and Algorithms** course at Hacettepe University. It includes modern software engineering components such as packaging, unit testing, documentation, and CI/CD.

---

 🧩 Features

- ✅ Accurate and efficient path calculation with Dijkstra's Algorithm  
- ✅ Customizable graph structure using Python dictionaries  
- ✅ Fully tested with `pytest`  
- ✅ Automated testing via GitHub Actions  
- ✅ HTML documentation generated using `Sphinx`  
- ✅ Publishable via TestPyPI  

---

## ⚙️ Installation

### From TestPyPI

```bash
pip install -i https://test.pypi.org/simple/ shortestpath2200674051
![image](https://github.com/user-attachments/assets/5a70a710-c560-4cf2-b95c-8b3a6ebd0aff)

````

Manual Installation

```bash
git clone https://github.com/beyzaoren/shortestpath_package.git
cd shortestpath_package
pip install .
```

---

## 💡 Usage Example

```python
from shortestpath.shortestpath import dijkstra

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

result = dijkstra(graph, 'A')
print(result)
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

---

 🧪 Testing

All tests are written using `pytest`.

```bash
pytest
```

Continuous integration is enabled via GitHub Actions. You can find the workflow file at `.github/workflows/python-test.yml`.

---

 📚 Documentation

The documentation is generated using `Sphinx`.

To view in your browser:

```bash
cd docs
make html
# Then open build/html/index.html in your browser
![image](https://github.com/user-attachments/assets/59c14461-e6d0-4c8e-8ab0-714f1fe93cb7)

```

> Author: **Beyza Ören**
> Email: [beyzaoren58@hotmail.com](mailto:beyzaoren58@hotmail.com)

---

 📁 Project Structure

```shell
shortestpath_package/
├── shortestpath/              # Core algorithm module
│   └── shortestpath.py
├── tests/                     # Unit tests
│   └── test_shortestpath.py
├── docs/                      # Sphinx documentation
│   ├── source/
│   └── build/
├── dist/                      # Compiled distribution files
├── .github/workflows/         # GitHub Actions CI workflow
│   └── python-test.yml
├── README.md
├── requirements.txt
└── setup.py
```

---

 🧠 Learning Outcomes

* Modular software development in Python
* Making algorithms testable and reusable
* Publishing to PyPI/TestPyPI
* Using GitHub Actions for CI
* Generating automatic documentation with Sphinx

---

 🪪 License

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

🏁 Contributing

Contributions are welcome!

1. Fork this repo
2. Create a new branch
3. Commit your changes
4. Open a Pull Request ✨

---

 🌐 Links

* 📦 TestPyPI: [shortestpath2200674051 on TestPyPI](https://test.pypi.org/project/shortestpath2200674051)
* 💻 GitHub: [github.com/beyzaoren/shortestpath\_package](https://github.com/beyzaoren/shortestpath_package)

---

```

---

Would you like me to generate this as a downloadable `.md` file or paste it into your project directory?
```
