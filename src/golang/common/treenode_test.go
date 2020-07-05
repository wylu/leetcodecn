package common

import (
	"reflect"
	"testing"
)

func want1() *TreeNode {
	return &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val:   4,
				Right: &TreeNode{Val: 7},
			},
		},
		Right: &TreeNode{
			Val:  3,
			Left: &TreeNode{Val: 5},
			Right: &TreeNode{
				Val:  6,
				Left: &TreeNode{Val: 8},
			},
		},
	}
}

func want2() *TreeNode {
	return &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val:   3,
				Right: &TreeNode{Val: 4},
			},
		},
		Right: &TreeNode{
			Val:  3,
			Left: &TreeNode{Val: 4},
			Right: &TreeNode{
				Val:  5,
				Left: &TreeNode{Val: 6},
			},
		},
	}
}

func TestMkTreeFromPreAndIn(t *testing.T) {
	type args struct {
		pre []int
		in  []int
	}
	tests := []struct {
		name string
		args args
		want *TreeNode
	}{
		// Case 1
		// 		    /----- 6
		// 	 	    |       \----- 8
		//  /----- 3
		//  |       \----- 5
		// 1
		//  \----- 2
		// 		    |       /----- 7
		// 		    \----- 4
		{
			name: "Case 1",
			args: args{
				pre: []int{1, 2, 4, 7, 3, 5, 6, 8},
				in:  []int{4, 7, 2, 1, 5, 3, 8, 6},
			},
			want: want1(),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := MkTreeFromPreAndIn(tt.args.pre, tt.args.in); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("MkTreeFromPreAndIn() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestBuildTreeFromPreAndIn(t *testing.T) {
	type args struct {
		pre []int
		in  []int
	}
	tests := []struct {
		name string
		args args
		want *TreeNode
	}{
		// Case 1
		// 		    /----- 5
		// 	 	    |       \----- 6
		//  /----- 3
		//  |       \----- 4
		// 1
		//  \----- 2
		// 		    |       /----- 4
		// 		    \----- 3
		{
			name: "Case 1",
			args: args{
				pre: []int{1, 2, 3, 4, 3, 4, 5, 6},
				in:  []int{3, 4, 2, 1, 4, 3, 6, 5},
			},
			want: want2(),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := BuildTreeFromPreAndIn(tt.args.pre, tt.args.in); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("BuildTreeFromPreAndIn() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestMkTreeFromInAndPost(t *testing.T) {
	type args struct {
		in   []int
		post []int
	}
	tests := []struct {
		name string
		args args
		want *TreeNode
	}{
		// Case 1
		// 		    /----- 6
		// 	 	    |       \----- 8
		//  /----- 3
		//  |       \----- 5
		// 1
		//  \----- 2
		// 		    |       /----- 7
		// 		    \----- 4
		{
			name: "Case 1",
			args: args{
				in:   []int{4, 7, 2, 1, 5, 3, 8, 6},
				post: []int{7, 4, 2, 5, 8, 6, 3, 1},
			},
			want: want1(),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := MkTreeFromInAndPost(tt.args.in, tt.args.post); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("MkTreeFromInAndPost() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestBuildTreeFromInAndPost(t *testing.T) {
	type args struct {
		in   []int
		post []int
	}
	tests := []struct {
		name string
		args args
		want *TreeNode
	}{
		// Case 1
		// 		    /----- 5
		// 	 	    |       \----- 6
		//  /----- 3
		//  |       \----- 4
		// 1
		//  \----- 2
		// 		    |       /----- 4
		// 		    \----- 3
		{
			name: "Case 1",
			args: args{
				in:   []int{3, 4, 2, 1, 4, 3, 6, 5},
				post: []int{4, 3, 2, 4, 6, 5, 3, 1},
			},
			want: want2(),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := BuildTreeFromInAndPost(tt.args.in, tt.args.post); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("BuildTreeFromInAndPost() = %v, want %v", got, tt.want)
			}
		})
	}
}
