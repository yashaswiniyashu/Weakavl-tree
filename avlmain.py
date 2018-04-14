import bst
import wavl
b=bst.BST()
b.insert(5)
b.insert(1)
b.insert(7)
b.insert(2)
b.insert(6)
b.insert(12)
b.insert(4)
b.insert(0)
b.insert(11)
b.insert(13)
b.insert(14)
b.insert(15)
b.insert(16)
b.insert(17)
b.insert(18)
b.insert(19)
b.inorder()
print("bst test")
ch='y'
while ch == 'y' or ch == 'Y':
	print("enter the number to be deleted")
	num=int(input())
	b.remove(num)
	print("enter y or Y to continue:")
	ch=input()
print("after the deletion:")
b.inorder()
print("height of the binary search tree is:")
print(b.height())
ch='y'
while ch == 'y':
	print("enter the number to be searched")
	num=int(input())
	b.search(num)
	print("enter y to continue:")
	ch=input()
print("wavl test")
w=wavl.WAVL()
w.insert(6)
w.insert(11)
w.insert(2)
w.insert(15)
w.insert(21)
w.insert(19)
w.inorder_debug()
ch='y'
while ch == 'y' or ch == 'Y':
	print("enter the number to be deleted")
	num=int(input())
	w.remove(num)
	print("enter y or Y to continue:")
	ch=input()

print("after the deletion:")
w.inorder_debug()
print("height of the weak avl tree")
print(w.height())
ch='y'
while ch == 'y' or ch == 'Y':
	print("enter the number to be searched")
	num=int(input())
	w.search(num)
	print("enter y or Y to continue:")
	ch=input()





