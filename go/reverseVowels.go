package main

func reverseVowels(s string) string {
	vowels := []byte{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

	sVowels := []byte{}

	for _, v := range s {
		if containsByteInArr(vowels, byte(v)) {
			sVowels = append(sVowels, byte(v))
		}
	}

	k := len(sVowels) - 1
	temp := []byte(s)

	for i, v := range s {
		if containsByteInArr(vowels, byte(v)) {
			temp[i] = sVowels[k]
			k--
		}
	}

	return string(temp)
}

func containsByteInArr(arr []byte, b byte) bool {
	for _, v := range arr {
		if v == b {
			return true
		}
	}

	return false
}
