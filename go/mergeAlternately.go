package main

func mergeAlternately(word1 string, word2 string) string {
	i := 0
	j := 0
	k := 0
	res := make([]byte, len(word1)+len(word2))

	for j < len(word1) && k < len(word2) {
		if i%2 == 0 {
			res[i] = word1[j]
			j++
		} else {
			res[i] = word2[k]
			k++
		}
		i++
	}

	for j < len(word1) {
		res[i] = word1[j]
		j++
		i++
	}
	for k < len(word2) {
		res[i] = word2[k]
		k++
		i++
	}

	return string(res)
}
