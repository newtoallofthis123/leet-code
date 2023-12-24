package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {

	length := 0
	current := head
	for current != nil {
		length++
		current = current.Next
	}

	if length == 1 {
		return nil
	}

	if length == n {
		return head.Next
	}

	current = head
	for current != nil {
		if length == n+1 {
			current.Next = current.Next.Next
			break
		}
		length--
		current = current.Next
	}

	return head
}
