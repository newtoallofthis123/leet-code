package main

import "fmt"

func minOperationsBox(boxes string) []int {
	res := make([]int, len(boxes))
	newBoxes := make([]int, len(boxes))
	onePositions := []int{}

	for i, v := range boxes {
		if v == '1' {
			onePositions = append(onePositions, i)
		}
		switch v {
		case '1':
			newBoxes[i] = 1
		case '0':
			newBoxes[i] = 0
		}
	}

	fmt.Println(onePositions)

	i := 0

	for i < len(boxes) {
		for _, v := range onePositions {
			res[i] += abs(i - v)
		}
		i++
	}

	return res
}
