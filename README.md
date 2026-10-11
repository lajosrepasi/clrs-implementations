# CLRS 4th Edition - Python Algorithms Implementations

This project contains Python implementations of algorithms from the textbook **"Introduction to Algorithms" (4th Edition)** by Cormen, Leiserson, Rivest, and Stein (CLRS).

---

## 🚀 Getting Started

This project uses [`uv`](https://github.com/astral-sh/uv) as its project and package manager.

### Prerequisites

Ensure you have `uv` installed on your system. If it is not installed, you can install it using `pip`:

```bash
pip install uv
```

### Installation

Clone the repository and sync the dependencies:

```bash
uv sync
```

---

## 🛠️ Usage

### Running an Algorithm

You can execute any algorithm implementation directly with `uv run`:

```bash
uv run python ./src/clrs/chapter02/bubble_sort.py
```

### Running Tests

To run the complete test suite across the project, execute:

```bash
uv run pytest
```

---

## ⚠️ Disclaimer

- **Implementation Code:** All algorithm implementation code is old-fashioned, hand-written, and typed manually.
- **AI Assistance:** Generative AI tools (Gemini and ChatGPT) were used **exclusively** to help write unit tests, generate docstrings, and validate algorithm implementations.
