package main 
import "fmt"
//else should be in the same line as } for the preceeding condition
//Prinln does not print the value of the %d or wharever but Printf does
func main() {
	x:=5
	y:=0
	if x<y{
		fmt.Printf("%d is less than %d \n",x,y)
	}else if x==y{
		fmt.Printf("%d is equal to %d \n",x,y)
	}else{
		fmt.Printf("%d is greater than %d \n",x,y)
	}
	//swith case
	num:=2
	switch num{
		case 1:
			fmt.Println("number is 1")
		case 2:
			fmt.Println("number is 2")
		default:
			fmt.Println("number is not 1 or 2")
	}
}
