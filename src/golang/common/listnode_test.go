package common

import (
	"reflect"
	"testing"
)

func list1() *ListNode {
	return &ListNode{
		Val: 1,
		Next: &ListNode{
			Val:  2,
			Next: &ListNode{Val: 3},
		},
	}
}

func TestListNode_ToString(t *testing.T) {
	tests := []struct {
		name string
		node *ListNode
		want string
	}{
		// Case 1
		{
			name: "Case 1",
			node: list1(),
			want: "1 -> 2 -> 3",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.node.ToString(); got != tt.want {
				t.Errorf("ListNode.ToString() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestMkLinkedList(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want *ListNode
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{nums: []int{1, 2, 3}},
			want: list1(),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := MkLinkedList(tt.args.nums...); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("MkLinkedList() = %v, want %v", got, tt.want)
			}
		})
	}
}
