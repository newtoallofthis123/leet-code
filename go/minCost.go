package main

func minCost(colors string, neededTime []int) int {
	cost := 0
	i, j := 0, 0

	for i < len(neededTime) && j < len(colors) {
		currTotal := 0
		currMax := 0

		for j < len(colors) && colors[j] == colors[i] {
			currTotal += neededTime[j]
			currMax = max(currMax, neededTime[j])
			j++
		}

		cost += currTotal - currMax
		i = j
	}

	return cost
}
