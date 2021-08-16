package p500to599

import "testing"

func Test_countArrangement(t *testing.T) {
	type args struct {
		n int
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
				n: 1,
			},
			want: 1,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				n: 2,
			},
			want: 2,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{
				n: 3,
			},
			want: 3,
		},
		// Case 4
		{
			name: "Case 4",
			args: args{
				n: 4,
			},
			want: 8,
		},
		// Case 5
		{
			name: "Case 5",
			args: args{
				n: 5,
			},
			want: 10,
		},
		// Case 6
		{
			name: "Case 6",
			args: args{
				n: 15,
			},
			want: 24679,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := countArrangement(tt.args.n); got != tt.want {
				t.Errorf("countArrangement() = %v, want %v", got, tt.want)
			}
		})
	}
}
