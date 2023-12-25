package main

import "fmt"

func uniqueOccurrences(arr []int) bool {
	occurences := make(map[int]int, len(arr))

	for _, v := range arr {
		occurences[v] += 1
	}

	fmt.Println(occurences)

	vals := make([]int, len(occurences))

	for _, v := range occurences {
		if containsIntInArr(vals, v) {
			return false
		} else {
			vals = append(vals, v)
		}
	}

	return true
}
