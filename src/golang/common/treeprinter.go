package common

import (
	"fmt"
	"strconv"
	"strings"
)

// TreePrinter print binary tree in a human friendly style.
type TreePrinter struct{}

// PrtLinuxStyle print binary tree in linux style.
//
// z
// ├── c
// │   ├── a
// │   └── b
// └── d
//
// @param root Root of binary tree.
// @return
func (tp *TreePrinter) PrtLinuxStyle(root *TreeNode) {
	fmt.Println(tp.GetLinuxStyle(root))
}

// GetLinuxStyle generate linux style string.
//
// @param root Root of binary tree.
// @return
func (tp *TreePrinter) GetLinuxStyle(root *TreeNode) string {
	outs := []string{}
	tp.linuxStyle(root, &outs, "", "")
	return strings.Join(outs, "")
}

func (tp *TreePrinter) linuxStyle(root *TreeNode, outs *[]string, prefix, childPrefix string) {
	if root == nil {
		return
	}
	*outs = append(*outs, prefix, strconv.Itoa(root.Val), "\n")
	tp.linuxStyle(root.Right, outs, childPrefix+"├── ", childPrefix+"│   ")
	tp.linuxStyle(root.Left, outs, childPrefix+"└── ", childPrefix+"    ")
}

// PrtHorizontalStyle print binary tree in horizontal style.
//
//                  /----- 20
//                  |       \----- 15
//          /----- 14
//          |       \----- 13
//  /----- 12
//  |       |       /----- 11
//  |       \----- 10
//  |               \----- 9
// 8
//  |               /----- 7
//  |       /----- 6
//  |       |       \----- 5
//  \----- 4
//          |       /----- 3
//          \----- 2
//                  \----- 1
//
// @param root Root of binary tree.
// @return
func (tp *TreePrinter) PrtHorizontalStyle(root *TreeNode) {
	fmt.Println(tp.GetHorizontalStyle(root))
}

// GetHorizontalStyle generate horizontal style string.
//
// @param root Root of binary tree.
// @return
func (tp *TreePrinter) GetHorizontalStyle(root *TreeNode) string {
	outs := []string{}

	if root.Right != nil {
		tp.horizontalStyle(root.Right, &outs, true, "")
	}
	outs = append(outs, strconv.Itoa(root.Val), "\n")
	if root.Left != nil {
		tp.horizontalStyle(root.Left, &outs, false, "")
	}

	return strings.Join(outs, "")
}

func (tp *TreePrinter) horizontalStyle(root *TreeNode, outs *[]string, isRight bool, indent string) {
	if root.Right != nil {
		tp.horizontalStyle(root.Right, outs, true, tp.getIndent(indent, isRight))
	}
	*outs = append(*outs, indent)
	if isRight {
		*outs = append(*outs, " /")
	} else {
		*outs = append(*outs, " \\")
	}
	*outs = append(*outs, "----- ", strconv.Itoa(root.Val), "\n")
	if root.Left != nil {
		tp.horizontalStyle(root.Left, outs, false, tp.getIndent(indent, !isRight))
	}
}

func (tp *TreePrinter) getIndent(indent string, isRight bool) string {
	if isRight {
		return indent + "        "
	}
	return indent + " |      "
}
