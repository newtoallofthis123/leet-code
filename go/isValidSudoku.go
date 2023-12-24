package main

func isValidSudoku(board [][]byte) bool {
	i := 0
	j := 0

	for i < len(board) {
		for j < len(board[i]) {
			if board[i][j] != '.' {
				if !isValid(board, i, j) {
					return false
				}
			}
			j++
		}
		i++
		j = 0
	}

	return true
}

func isValid(board [][]byte, i int, j int) bool {
	for k := 0; k < len(board[0]) && k != j; k++ {
		if board[i][k] == board[i][j] {
			return false
		}
	}

	for k := 0; k < len(board) && k != i; k++ {
		if board[k][j] == board[i][j] {
			return false
		}
	}

	for k := i / 3 * 3; k < i/3*3+3; k++ {
		for l := j / 3 * 3; l < j/3*3+3; l++ {
			if k != i && l != j && board[k][l] == board[i][j] {
				return false
			}
		}
	}

	return true
}
