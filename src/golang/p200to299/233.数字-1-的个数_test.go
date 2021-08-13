package p200to299

import "testing"

func Test_countDigitOne(t *testing.T) {
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
				n: 11,
			},
			want: 4,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				n: 534,
			},
			want: 214,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{
				n: 530,
			},
			want: 213,
		},
		// Case 4
		{
			name: "Case 4",
			args: args{
				n: 504,
			},
			want: 201,
		},
		// Case 5
		{
			name: "Case 5",
			args: args{
				n: 514,
			},
			want: 207,
		},
		// Case 6
		{
			name: "Case 6",
			args: args{
				n: 10,
			},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := countDigitOne(tt.args.n); got != tt.want {
				t.Errorf("countDigitOne() = %v, want %v", got, tt.want)
			}
		})
	}
}
