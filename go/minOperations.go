package main

func minOperations(s string) int {
	counts := make([]int, 2)

	for i := 0; i < len(s); i += 1 {
		if i%2 == 0 && s[i] == '1' {
			counts[0]++
		}
		if i%2 == 1 && s[i] == '0' {
			counts[0]++
		}
	}

	for i := 0; i < len(s); i += 1 {
		if i%2 == 0 && s[i] == '0' {
			counts[1]++
		}
		if i%2 == 1 && s[i] == '1' {
			counts[1]++
		}
	}

	return min(counts[0], counts[1])
}

// well wasn't that a pleasant surprise
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/submissions/1127303835?envType=daily-question&envId=2023-12-24
// Runtime: 0 ms, faster than 100.00% solutions for Go
// Memory Usage: 2.48 MB, beats 98.41% of solutions for Go
