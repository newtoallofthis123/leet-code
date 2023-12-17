package main

import "strings"

func lengthOfLongestSubstring(s string) int {
	var maxLen int

	for i := 0; i < len(s); i++ {
		var subStr string
		for j := i; j < len(s); j++ {
			if !strings.Contains(subStr, string(s[j])) {
				subStr += string(s[j])
			} else {
				break
			}
		}
		if len(subStr) > maxLen {
			maxLen = len(subStr)
		}
	}

	return maxLen
}
