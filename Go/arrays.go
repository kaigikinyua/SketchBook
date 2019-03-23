//you have to know the size of the array
package main 
import "fmt"

func main(){
	//there are arrays and slices
	var languages[5] string
	languages[0]="Python"
	languages[1]="JavaScript"
	languages[2]="Html + Css"
	languages[3]="C++"
	languages[4]="Golang!!"
	fmt.Println(languages)
	//declare and assin
	jobs:=[3] string {"Web Developer","System Admin","Hacker"}
	fmt.Println(jobs)
	//slices
	mySlice:=[] string {"1","2","3"}
	fmt.Println(mySlice)
	//getting length
	fmt.Println(len(mySlice))
	//printing values with range
	fmt.Println(languages[0:4])

}