package main

func removeElement(nums []int, val int) int {

	i := 0
	for i < len(nums) {
		if nums[i] == val {
			nums[i] = -1
		}
		i++
	}

	moveToStart(nums)

	return len(nums)
}

// remove all empty elements from the array
func moveToStart(nums []int) {
	i := 0
	for i < len(nums) {
		if nums[i] == -1 {
			nums = append(nums[:i], nums[i+1:]...)
		} else {
			i++
		}
	}
}

// https://leetcode.com/problems/remove-element/submissions/1127594657/
