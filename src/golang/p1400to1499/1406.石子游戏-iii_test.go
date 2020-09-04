package p1400to1499

import "testing"

func Test_stoneGameIII(t *testing.T) {
	type args struct {
		stones []int
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// Test Case 1
		{
			name: "Test Case 1",
			args: args{
				stones: []int{1, 2, 3, 7},
			},
			want: "Bob",
		},
		// Test Case 2
		{
			name: "Test Case 2",
			args: args{
				stones: []int{1, 2, 3, -9},
			},
			want: "Alice",
		},
		// Test Case 3
		{
			name: "Test Case 3",
			args: args{
				stones: []int{1, 2, 3, 6},
			},
			want: "Tie",
		},
		// Test Case 4
		{
			name: "Test Case 4",
			args: args{
				stones: []int{1, 2, 3, -1, -2, -3, 7},
			},
			want: "Alice",
		},
		// Test Case 5
		{
			name: "Test Case 5",
			args: args{
				stones: []int{-1, -2, -3},
			},
			want: "Tie",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := stoneGameIII(tt.args.stones); got != tt.want {
				t.Errorf("stoneGameIII() = %v, want %v", got, tt.want)
			}
		})
	}
}
