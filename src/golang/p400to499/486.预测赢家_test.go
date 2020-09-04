package p400to499

import "testing"

func TestPredictTheWinner(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// Test Case 1
		{
			name: "Test Case 1",
			args: args{
				nums: []int{1, 5, 2},
			},
			want: false,
		},
		// Test Case 2
		{
			name: "Test Case 2",
			args: args{
				nums: []int{1, 5, 233, 7},
			},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := PredictTheWinner(tt.args.nums); got != tt.want {
				t.Errorf("PredictTheWinner() = %v, want %v", got, tt.want)
			}
		})
	}
}
