package main

// https://leetcode.com/problems/container-with-most-water/

// height = [1,8,6,2,5,4,8,3,7]

func maxArea(height []int) int {
	left := 0
	right := len(height) - 1
	area := 0

	if len(height) == 2 {
		return min(height[0], height[1])
	}

	for left < right {
		tempArea := min(height[left], height[right]) * (right - left)
		if tempArea > area {
			area = tempArea
		}
		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}

	return area
}

// https://leetcode.com/problems/container-with-most-water/submissions/1139213677/
