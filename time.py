import time
import wavl
import bst
import avl 
import rbtree
def main1():
	b=bst.BST()
	print("BST RUNTIME:")
	for i in range(500):
		b.insert(i+1)
start_time = time.time()
main1()
print("­­­---%s seconds---" % (time.time()-start_time))
def main2():
	a=avl.AvlTree()
	print('AVL RUNTIME:')
	for i in range (500):
		a.insert(i)
start_time = time.time()
main2()
print("­­­---%s seconds---" % (time.time()-start_time))
def main():
	d=wavl.WAVL()
	print("WAVL RUNTIME:")
	for i in range (500):
		d.insert(i)
start_time = time.time()
main()
print("­­­---%s seconds---" % (time.time()-start_time))
def main3():
	f=rbtree.RedBlackTree()
	print("REDBLACKTREE RUNTIME:")
	for i in range (500):
		f.add(i)
start_time = time.time()
main3()
print("­­­---%s seconds---" % (time.time()-start_time))
