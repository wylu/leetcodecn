package common

import "testing"

// 		    /----- 6
// 	        |       \----- 8
//  /----- 3
//  |       \----- 5
// 1
//  \----- 2
// 		    |       /----- 7
// 		    \----- 4
func tree1() *TreeNode {
	return MkTreeFromPreAndIn(
		[]int{1, 2, 4, 7, 3, 5, 6, 8},
		[]int{4, 7, 2, 1, 5, 3, 8, 6},
	)
}

//                  /----- 20
//                  |       \----- 15
//          /----- 14
//          |       \----- 13
//  /----- 12
//  |       |       /----- 11
//  |       \----- 10
//  |               \----- 9
// 8
//  |               /----- 7
//  |       /----- 6
//  |       |       \----- 5
//  \----- 4
//          |       /----- 3
//          \----- 2
//                  \----- 1
func tree2() *TreeNode {
	return MkTreeFromPreAndIn(
		[]int{8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 20, 15},
		[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20},
	)
}

func TestTreePrinter_PrtLinuxStyle(t *testing.T) {
	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		tp   *TreePrinter
		args args
	}{
		// Case 1
		{
			name: "Case 1",
			tp:   &TreePrinter{},
			args: args{root: tree1()},
		},
		// Case 2
		{
			name: "Case 2",
			tp:   &TreePrinter{},
			args: args{root: tree2()},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.tp.PrtLinuxStyle(tt.args.root)
		})
	}
}

func TestTreePrinter_PrtHorizontalStyle(t *testing.T) {
	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		tp   *TreePrinter
		args args
	}{
		// Case 1
		{
			name: "Case 1",
			tp:   &TreePrinter{},
			args: args{root: tree1()},
		},
		// Case 2
		{
			name: "Case 2",
			tp:   &TreePrinter{},
			args: args{root: tree2()},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.tp.PrtHorizontalStyle(tt.args.root)
		})
	}
}
