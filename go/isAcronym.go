package main

func isAcronym(words []string, s string) bool {
	if len(words) != len(s) {
		return false
	}

	i := 0

	for i < len(words) {
		if words[i][0] != s[i] {
			return false
		}
		i++
	}
	return true
}
