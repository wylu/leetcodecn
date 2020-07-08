package interview

import (
	"reflect"
	"testing"
)

func Test_divingBoard(t *testing.T) {
	type args struct {
		shorter int
		longer  int
		k       int
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
				shorter: 1,
				longer:  2,
				k:       3,
			},
			want: []int{3, 4, 5, 6},
		},
		// Case 2
		{
			name: "Case 2",
			args: args{
				shorter: 1,
				longer:  2,
				k:       0,
			},
			want: []int{},
		},
		// Case 3
		{
			name: "Case 3",
			args: args{
				shorter: 1,
				longer:  1,
				k:       3,
			},
			want: []int{3},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := divingBoard(tt.args.shorter, tt.args.longer, tt.args.k); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("divingBoard() = %v, want %v", got, tt.want)
			}
		})
	}
}
