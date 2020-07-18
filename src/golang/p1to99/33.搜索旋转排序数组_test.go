package p1to99

import "testing"

func Test_search(t *testing.T) {
	type args struct {
		nums   []int
		target int
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
				nums:   []int{1, 3},
				target: 3,
			},
			want: 1,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				nums:   []int{1, 2, 3, 4, 5},
				target: 3,
			},
			want: 2,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{
				nums:   []int{1, 2, 3, 4, 5},
				target: 0,
			},
			want: -1,
		},
		// Case 4
		{
			name: "Case 4",
			args: args{
				nums:   []int{5, 4, 3, 2, 1},
				target: 1,
			},
			want: 4,
		},
		// Case 5
		{
			name: "Case 5",
			args: args{
				nums:   []int{4, 5, 6, 7, 0, 1, 2},
				target: 0,
			},
			want: 4,
		},
		// Case 6
		{
			name: "Case 6",
			args: args{
				nums:   []int{4, 5, 0, 1, 2},
				target: 5,
			},
			want: 1,
		},
		// Case 7
		{
			name: "Case 7",
			args: args{
				nums:   []int{4, 5, 6, 7, 8, 1, 2, 3},
				target: 8,
			},
			want: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := search(tt.args.nums, tt.args.target); got != tt.want {
				t.Errorf("search() = %v, want %v", got, tt.want)
			}
		})
	}
}
