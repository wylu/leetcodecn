package p200to299

import "testing"

func Test_computeArea(t *testing.T) {
	type args struct {
		ax1 int
		ay1 int
		ax2 int
		ay2 int
		bx1 int
		by1 int
		bx2 int
		by2 int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{-5, -5, -4, 0, -3, -3, 3, 3},
			want: 41,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{-5, -5, 0, -4, -3, -3, 3, 3},
			want: 41,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{-2, -5, 1, 3, -3, -3, 3, 3},
			want: 42,
		},
		// Case 4
		{
			name: "Case 4",
			args: args{-3, -5, 0, 5, -3, -3, 3, 3},
			want: 48,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := computeArea(tt.args.ax1, tt.args.ay1, tt.args.ax2, tt.args.ay2, tt.args.bx1, tt.args.by1, tt.args.bx2, tt.args.by2); got != tt.want {
				t.Errorf("computeArea() = %v, want %v", got, tt.want)
			}
		})
	}
}
