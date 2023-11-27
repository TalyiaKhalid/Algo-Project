# Python3 program for the above approach
import numpy as np 
from typing import DefaultDict
import converting

INT_MAX = 2147483647

# Function to find the minimum
# cost path for all the paths
def findMinRoute(tsp):
	sum = 0
	counter = 0
	j = 0
	i = 0
	min = INT_MAX
	visitedRouteList = DefaultDict(int)

	# Starting from the 0th indexed
	# city i.e., the first city
	visitedRouteList[0] = 1
	route = [0] * len(tsp)

	# Traverse the adjacency
	# matrix tsp[][]
	while i < len(tsp) and j < len(tsp[i]):

		# Corner of the Matrix
		if counter >= len(tsp[i]) - 1:
			break

		# If this path is unvisited then
		# and if the cost is less then
		# update the cost
		if j != i and (visitedRouteList[j] == 0):
			if tsp[i][j] < min:
				min = tsp[i][j]
				route[counter] = j + 1

		j += 1

		# Check all paths from the
		# ith indexed city
		if j == len(tsp[i]):
			sum += min
			min = INT_MAX
			visitedRouteList[route[counter] - 1] = 1
			j = 0
			i = route[counter] - 1
			counter += 1

	# Update the ending city in array
	# from city which was last visited
	i = route[counter - 1] - 1

	for j in range(len(tsp)):

		if (i != j) and tsp[i][j] < min:
			min = tsp[i][j]
			route[counter] = j + 1

	sum += min

	# Started from the node where
	# we finished as well.
	print("Minimum distance with a different n :", sum)



tsp = converting.distance_matrix
# number of nodes/cities
# Select a different number of cities (e.g. 10)
n = 248
tsp_subset = converting.distance_matrix[:n, :n]

# Function Call
findMinRoute(tsp_subset)


