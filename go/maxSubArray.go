package main

import (
	"math"
)

func maxSubArray(nums []int) int {
	maxSum := int(math.Inf(-1))
	currSum := 0

	for _, num := range nums {
		currSum += num

		if currSum > maxSum {
			maxSum = currSum
		}

		if currSum < 0 {
			currSum = 0
		}
	}

	return maxSum
}
