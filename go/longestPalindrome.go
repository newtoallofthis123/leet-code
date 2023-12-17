package main

func isPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-i-1] {
			return false
		}
	}

	return true
}

func longestPalindrome(s string) string {
	var pal string

	for i := 0; i < len(s); i++ {
		for j := i; j < len(s); j++ {
			if isPalindrome(s[i:j+1]) && len(s[i:j+1]) > len(pal) {
				pal = s[i : j+1]
			}
		}
	}

	return pal
}
