import time
import wavl1
import bst
def main():
    n=int(input("ENTER THE NUMBER OF STUDENTS: \n"))
    b=bst.BST()
    w=wavl1.WAVL()
    for i in range (n):
        print("\nENTER THE DETAILS OF STUDENT ",i+1,":")
        key=int(input("Enter the roll num:        "))
        name=input("Enter name:        ")
        add=input("Enter the address:        ")
        mob=int(input("Enter the mobile number:        "))
        course=input("Enter the course:        ")
        print('Enter the marks in three subjects:')
        m1=int(input("First subject:    "))
        m2=int(input("Second subject:    "))
        m3=int(input("Third subject:    "))
        total=m1+m2+m3
        percent=total/3
        b.insert(key)
        w.insert(key,name,add,mob,course,m1,m2,m3,total,percent)
    print("\nBST TRAVERSAL\n")
    b.inorder()
    print("DO YOU  WANT TO DELETE ANY KEYS IN THE TREE ?")
    print("IF YES ENTER y  OR Y\n")
    ch=input()
    if ch == 'y' or ch == 'Y':
        while ch == 'y' or ch == 'Y':
            print("\nEnter the number to be deleted\n")
            num=int(input())
            b.remove(num)
            print("Enter y or Y to continue:\n")
            ch=input()
        print("AFTER THE DELETION :\n")
        b.inorder()
    print("\nDO YOU  WANT TO SEARCH ANY KEYS IN THE TREE ? ")
    print("IF YES ENTER y  OR Y\n")
    ch=input()
    while ch == 'y' or ch == 'Y':
        print("\nEnter the key to be searched :\n")
        num=int(input())
        b.search(num)
        print("Enter y or Y to continue:\n")
        ch=input()
    print("\n*************************END OF BST OPERATIONS*******************************\n")
    print("\nWAVL TRAVERSAL\n")
    w.inorder_degug()
    print("\nDO YOU  WANT TO ANY RECORDS TO BE DELETED  ? ")
    print("IF YES ENTER y  OR Y\n")
    ch=input()
    if ch == 'y' or ch == 'Y':
        while ch == 'y' or ch == 'Y':
            print("\nENTER THE ROLL NUMBER OF THE STUDENT WHOSE RECORD TO BE DELETED:\n")
            num=int(input())
            w.remove(num)
            print("Enter y or Y to continue:\n")
            ch=input()
        print("\nAFTER THE DELETION:\n")
        w.inorder_degug()
    
    print("\nDO YOU  WANT TO SEARCH FOR ANY STUDENT DETAILS ? ")
    print("IF YES ENTER y  OR Y\n")
    ch=input()
    while ch == 'y' or ch == 'Y':
            print("\nENTER THE ROLL NUMBER OF THE STUDENT WHOSE RECORD TO BE FOUND:\n")
            num=int(input())
            w.search(num)
            print("\nEnter y or Y to continue:\n")
            ch=input()
 
    print("***********************END**********************************************")

    


if __name__ == '__main__':
	main()
	
