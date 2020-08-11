package p1to99

import "testing"

func Test_recoverTree(t *testing.T) {
	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		args args
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{
				root: &TreeNode{
					Val: 1,
					Left: &TreeNode{
						Val: 3,
						Right: &TreeNode{
							Val: 2,
						},
					},
				},
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			recoverTree(tt.args.root)
		})
	}
}
