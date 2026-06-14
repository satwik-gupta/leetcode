/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func pairSum(head *ListNode) int {
    var prev *ListNode

    slow := head
    fast := head

    for fast != nil && fast.Next != nil {
        fast = fast.Next.Next

        next := slow.Next
        slow.Next = prev
        prev = slow
        slow = next
    }

    ans := 0

    for prev != nil {
        sum := prev.Val + slow.Val
        if sum > ans {
            ans = sum
        }

        prev = prev.Next
        slow = slow.Next
    }

    return ans
}