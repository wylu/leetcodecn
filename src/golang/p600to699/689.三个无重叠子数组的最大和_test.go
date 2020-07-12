package p600to699

import (
	"reflect"
	"testing"
)

func Test_maxSumOfThreeSubarrays(t *testing.T) {
	type args struct {
		nums []int
		k    int
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
				nums: []int{1, 2, 1, 2, 6, 7, 5, 1},
				k:    2,
			},
			want: []int{0, 3, 5},
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				nums: []int{7, 13, 20, 19, 19, 2, 10, 1, 1, 19},
				k:    3,
			},
			want: []int{1, 4, 7},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxSumOfThreeSubarrays(tt.args.nums, tt.args.k); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("maxSumOfThreeSubarrays() = %v, want %v", got, tt.want)
			}
		})
	}
}
