package p300to399

import (
	"reflect"
	"testing"
)

func Test_countSmaller(t *testing.T) {
	type args struct {
		nums []int
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
				nums: []int{5, 2, 6, 1},
			},
			want: []int{2, 1, 1, 0},
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				nums: []int{-1},
			},
			want: []int{0},
		},
		// Case 3
		{
			name: "Case 3",
			args: args{
				nums: []int{-1, -1},
			},
			want: []int{0, 0},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := countSmaller(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("countSmaller() = %v, want %v", got, tt.want)
			}
		})
	}
}
