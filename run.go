package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
)

func main() {
	fileName := os.Args[1]

	if _, err := os.Stat(fileName); os.IsNotExist(err) {
		fmt.Println("File does not exist")
		return
	}

	var prog string

	if fileName[len(fileName)-3:] == ".ts" {
		prog = "ts"
	}

	if prog == "ts" {
		err := exec.Command("tsc", "--outDir", "dist", fileName).Run()
		if err != nil {
			log.Fatal(err)
			return
		}

		err = os.Chdir("dist")
		if err != nil {
			fmt.Println("Error changing directory")
			return
		}

		out, err := exec.Command("node", fileName[:len(fileName)-3]+".js").Output()
		if err != nil {
			log.Fatal(err)
			return
		}

		fmt.Println(string(out))
	}
}
