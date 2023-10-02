// https://leetcode.com/problems/lemonade-change/description/

package main

import "fmt"

func lemonadeChange(bills []int) bool {
	money := make(map[int]int)

	for _, bill := range bills {
		if bill == 5 {
			money[5]++
		} else if bill == 10 {
			if money[5] == 0 {
				return false
			}
			money[5]--
			money[10]++
		} else if bill == 20 {
			if money[10] > 0 && money[5] > 0 {
				money[10]--
				money[5]--
			} else if money[5] >= 3 {
				money[5] -= 3
			} else {
				return false
			}
		}
	}
	return true
}

func main() {
	bills := []int{5, 5, 5, 10, 20}
	fmt.Println(lemonadeChange(bills))
}
