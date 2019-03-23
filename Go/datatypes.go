package main 
import "fmt"
func main() {
	var name string="Golang"
	fmt.Println(name+" this is a string")
	var num int=49
	var logic bool=true
	//also it is easier to do var num since go will just infer the datatype
	//you can also create variables using eg name:="VAriable value" (shorthand method)
	//myname,myage:='value0,value1'
	fmt.Println(num)
	//%T will give you the data type of the variable
	//const -> used instead of var for constants
	myage:=1.6
	fmt.Printf("name is :%T\n num is:%T\n logic is :%T\n myage is: %T\n",name,num,logic,myage)
}