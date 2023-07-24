"""Program that calculates the k-means clustering of a set of points in a 2D plane."""

import math
import random
import sys

import matplotlib.pyplot as plt
import numpy as np


class Point:
    """Class representing a point in a 2D plane."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        """Returns the distance between this point and another point."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Cluster:
    """Class representing a cluster of points in a 2D plane."""

    def __init__(self, center):
        self.center = center
        self.points = []

    def add_point(self, point):
        """Adds a point to the cluster."""
        self.points.append(point)

    def clear_points(self):
        """Removes all points from the cluster."""
        self.points = []

    def update_center(self):
        """Updates the center of the cluster to the average of the points in the cluster."""
        if len(self.points) == 0:
            return
        x_sum = 0
        y_sum = 0
        for point in self.points:
            x_sum += point.x
            y_sum += point.y
        self.center = Point(x_sum / len(self.points), y_sum / len(self.points))


class KMeans:
    """Class representing a k-means clustering of a set of points in a 2D plane."""

    def __init__(self, points, k):
        self.points = points
        self.k = k
        self.clusters = []
        for _ in range(k):
            self.clusters.append(Cluster(self.random_point()))

    def random_point(self):
        """Returns a random point from the set of points."""
        return self.points[random.randint(0, len(self.points) - 1)]

    def assign_points(self):
        """Assigns each point to the cluster with the closest center."""
        for cluster in self.clusters:
            cluster.clear_points()
        for point in self.points:
            closest_cluster = self.clusters[0]
            closest_distance = point.distance(closest_cluster.center)
            for cluster in self.clusters[1:]:
                distance = point.distance(cluster.center)
                if distance < closest_distance:
                    closest_cluster = cluster
                    closest_distance = distance
            closest_cluster.add_point(point)

    def update_centers(self):
        """Updates the centers of each cluster to the average of the points in the cluster."""
        for cluster in self.clusters:
            cluster.update_center()

    def run(self, iterations):
        """Runs the k-means algorithm for the specified number of iterations."""
        for _ in range(iterations):
            self.assign_points()
            self.update_centers()

    def plot(self):
        """Plots the points and clusters."""
        plt.figure()
        for cluster in self.clusters:
            x = [point.x for point in cluster.points]
            y = [point.y for point in cluster.points]
            plt.scatter(x, y)
        plt.show()


def main():
    """Main function."""
    k = 3
    iterations = 20
    points = []
    for _ in range(300):
        points.append(Point(random.random(), random.random()))

    k_means = KMeans(points, k)
    k_means.run(iterations)
    k_means.plot()


if __name__ == "__main__":
    main()
