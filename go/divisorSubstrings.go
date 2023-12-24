package main

import "fmt"

func divisorSubstrings(num int, k int) int {
	var res int

	var new_num string = fmt.Sprintf("%d", num)
	i := 0

	for i < len(new_num) {
		if i > len(new_num)-k {
			break
		}

		var sub_num string = new_num[i : i+k]
		var sub_num_int int
		fmt.Sscanf(sub_num, "%d", &sub_num_int)

		if sub_num_int == 0 {
			i++
			continue
		}

		if num%sub_num_int == 0 {
			res++
		}

		i++
	}

	return res
}

// https://leetcode.com/problems/find-the-k-beauty-of-a-number/submissions/1127345293/
// Runtime: 0 ms, faster than 100.00% of Go online submissions
// Memory Usage: 2.1 MB, Beats 5.66% of Go online submissions
