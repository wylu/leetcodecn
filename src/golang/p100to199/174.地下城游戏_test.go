package p100to199

import "testing"

func Test_calculateMinimumHP(t *testing.T) {
	type args struct {
		dungeon [][]int
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
				dungeon: [][]int{
					[]int{-2, -3, 3},
					[]int{-5, -10, 1},
					[]int{10, 30, -5},
				},
			},
			want: 7,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				dungeon: [][]int{
					[]int{0},
				},
			},
			want: 1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := calculateMinimumHP(tt.args.dungeon); got != tt.want {
				t.Errorf("calculateMinimumHP() = %v, want %v", got, tt.want)
			}
		})
	}
}
