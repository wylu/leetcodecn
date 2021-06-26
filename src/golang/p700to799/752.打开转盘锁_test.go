package p700to799

import "testing"

func Test_openLock(t *testing.T) {
	type args struct {
		deadends []string
		target   string
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
				deadends: []string{
					"0201", "0101", "0102", "1212", "2002",
				},
				target: "0202",
			},
			want: 6,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				deadends: []string{
					"0000",
				},
				target: "8888",
			},
			want: -1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := openLock(tt.args.deadends, tt.args.target); got != tt.want {
				t.Errorf("openLock() = %v, want %v", got, tt.want)
			}
		})
	}
}
