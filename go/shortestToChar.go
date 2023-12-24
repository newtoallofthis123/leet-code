package main

func shortestToChar(s string, c byte) []int {
	distances := make([]int, len(s))
	indexes := []int{}

	i := 0
	for i < len(s) {
		if s[i] == c {
			indexes = append(indexes, i)
		}
		i++
	}

	i = 0
	for i < len(s) {
		min := len(s)
		for _, index := range indexes {
			if abs(index-i) < min {
				min = abs(index - i)
			}
		}
		distances[i] = min
		i++
	}

	return distances
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
