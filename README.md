# k_means

## Description

This is a simple implementation of the k-means algorithm in Python.

## Usage

Directly from terminal:

```bash
python k_means.py
```

From Python:

```python
from k_means import KMeans

k = 3
iterations = 20
points = []
for _ in range(300):
    points.append(Point(random.random(), random.random()))

k_means = KMeans(points, k)
k_means.run(iterations)
k_means.plot()
```

## Requirements

```bash
pip install -r requirements.txt
```
