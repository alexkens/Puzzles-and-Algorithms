
fun binarySearch(parameter1: IntArray, number: Int): Int {
    var array = parameter1
    var length = array.size
    while (length > 1) {
        println(array.joinToString())
        println(array[length/2])
        println()
        
        if (array[length/2] > number) {
            array = array.sliceArray(0..length/2-1)
        } else {
            array = array.sliceArray(length/2..length-1)
        }
        length = array.size
    }
    // length is 1 so only the searched element is left
    return array[0]
}

fun main() {
    
    var array = IntArray(10)   
    for(i in 0..9) {
        array[i] = i + 1
    }
    println(array.joinToString())
    println()
    
    var result = binarySearch(array, 10)
    println(result)
  
}