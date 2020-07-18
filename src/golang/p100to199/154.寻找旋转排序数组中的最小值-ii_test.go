package p100to199

import "testing"

func Test_findMin154(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{
				nums: []int{1, 2, 3, 4, 5},
			},
			want: 1,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				nums: []int{5, 4, 3, 2, 1},
			},
			want: 1,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{
				nums: []int{1, 1, 1, 0, 1},
			},
			want: 0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findMin154(tt.args.nums); got != tt.want {
				t.Errorf("findMin154() = %v, want %v", got, tt.want)
			}
		})
	}
}
