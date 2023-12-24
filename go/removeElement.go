package main

import "fmt"

func removeElement(nums []int, val int) int {

	i := 0
	for i < len(nums) {
		if nums[i] == val {
			nums[i] = -1
		}
		i++
	}

	nums = moveToStart(nums)
	fmt.Println(nums)

	return len(nums)
}

// remove all empty elements from the array
func moveToStart(nums []int) []int {
	i := 0
	for i < len(nums) {
		if nums[i] == -1 {
			nums = append(nums[:i], nums[i+1:]...)
		} else {
			i++
		}
	}

	return nums
}

// https://leetcode.com/problems/remove-element/submissions/1127594657/
