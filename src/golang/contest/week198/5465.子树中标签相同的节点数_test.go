package week198

import (
	"reflect"
	"testing"
)

func Test_countSubTrees(t *testing.T) {
	type args struct {
		n      int
		edges  [][]int
		labels string
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{
				n: 3,
				edges: [][]int{
					[]int{0, 1},
					[]int{0, 2},
				},
				labels: "aab",
			},
			want: []int{2, 1, 1},
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				n: 7,
				edges: [][]int{
					[]int{0, 1},
					[]int{0, 2},
					[]int{1, 4},
					[]int{1, 5},
					[]int{2, 3},
					[]int{2, 6},
				},
				labels: "abaedcd",
			},
			want: []int{2, 1, 1, 1, 1, 1, 1},
		},
		// Case 3
		{
			name: "Case 3",
			args: args{
				n: 5,
				edges: [][]int{
					[]int{0, 1},
					[]int{0, 2},
					[]int{2, 3},
					[]int{2, 4},
				},
				labels: "abaed",
			},
			want: []int{2, 1, 1, 1, 1},
		},
		// Case 4
		{
			name: "Case 4",
			args: args{
				n: 4,
				edges: [][]int{
					[]int{0, 2},
					[]int{0, 3},
					[]int{1, 2},
				},
				labels: "aeed",
			},
			want: []int{1, 1, 2, 1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := countSubTrees(tt.args.n, tt.args.edges, tt.args.labels); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("countSubTrees() = %v, want %v", got, tt.want)
			}
		})
	}
}
