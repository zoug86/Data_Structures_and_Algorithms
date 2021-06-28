###### First topic: RECURSION - June 02 2021 ######
# Recursion: a process that calls itself -
# Base case: a condition for the recursion to stop

# Example 1: factorial
'''
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(6))
'''

# Example 2: productOfArray
# Write a function called productOfArray which takes in an array
# of numbers and returns the product of them all.

#--In JavaScript--#
'''
// productOfArray([1, 2, 3]) // 6
// productOfArray([1, 2, 3, 10]) // 60

function productOfArray(arr){
    if (arr.length === 0){
        return 1;
    }
    return arr[0] * productOfArray(arr.slice(1));
}
'''
#--In Python--#
'''
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0]*productOfArray(arr[1:])

print(productOfArray([1, 2, 3]))
print(productOfArray([1, 2, 3, 10]))
'''

# Example 3: recursiveRange
# Write a function called recursiveRange  which accepts a number and adds
# up all the numbers from 0 to the number passed to the function .

#--In JavaScript--#
'''
function recursiveRange(num){
    if(num === 0){
        return 0;
    }
   return num+recursiveRange(num-1);
}
'''
#--In Python--#

'''
def recursiveRange(num):
    if num == 0:
        return 0
    return num+recursiveRange(num-1)

print(recursiveRange(6))
print(recursiveRange(10))
'''

# Example 4: Fibonacci
# Write a recursive function called fib which accepts a number and returns the nth number in the Fibonacci sequence.
# Recall that the Fibonacci sequence is the sequence of whole numbers 1, 1, 2, 3, 5, 8, ...
# which starts with 1 and 1, and where every number thereafter is equal to the sum of
# the previous two numbers. .

#--In JavaScript--#
'''
// fib(4) // 3
// fib(10) // 55
// fib(28) // 317811
// fib(35) // 9227465

function fib(num){
    if (num === 1 | | num == = 2){
       return 1;
    }
   return fib(num - 1) + fib(num - 2);
}
'''

#--In Python--#
'''
def fib(num):
    if num == 1 or num == 2:
        return 1
    return fib(num-1)+fib(num-2)

print(fib(7))
'''

# Example 5: String Reverse
# Write a recursive function called fib which accepts a string and returns a new string in reverse.

#--In JavaScript--#

'''
function reverse(str){
  // add whatever parameters you deem necessary - good luck!
  let strRev = "";
  function helper(temp){
      if(temp.length === 0){
        return strRev;
  }
  
      strRev += temp[temp.length-1];
     let temp2 = temp.substring(0,temp.length - 1);
      helper(temp2);
  }
  
  helper(str);
  return strRev;
  
}

// reverse('awesome') // 'emosewa'
// reverse('rithmschool') // 'loohcsmhtir'
'''

#--In Python--#

'''
str_rev = ""

def reverse(temp):
    global str_rev
    if len(temp) == 0:
        return str_rev
    str_rev += temp[len(temp)-1]
    temp2 = temp[0:len(temp)-1]
    return reverse(temp2)

#print(reverse('awesome'))
print(reverse('rithmschool'))
'''

# Example 6: Palindrome
# Write a recursive function called isPalindrome  which returns true if the string passed to it is a palindrome
# (reads the same forward and backward). Otherwise it returns false..

#--In JavaScript--#

'''
// isPalindrome('awesome') // false
// isPalindrome('foobar') // false
// isPalindrome('tacocat') // true
// isPalindrome('amanaplanacanalpanama') // true
// isPalindrome('amanaplanacanalpandemonium') // false
let new_str = "";
function isPalindrome(temp){
  // add whatever parameters you deem necessary - good luck
  let end = temp.length;
  let start = 0;
 
   if(temp[start] !== temp[end-1]){
     return false;
   }
   start++;
   end--;
   if(end === 2){
     return true;
   }
   new_str = temp.substring(start, end);
   return isPalindrome(new_str);
}
'''

#--In Python--#

'''
new_str = ""

def isPalindrome(str):
    global new_str
    start = 0
    end = len(str)
    if str[start] != str[end-1]:
        return False
    start += 1
    end -= 1
    if end == 2:
        return True
    new_str = str[start:end]
    return isPalindrome(new_str)

print(isPalindrome('amanaplanacanalpanama'))
'''


###### Second topic: Searching Algorithms - June 03 2021 ######

           ###########Binary Search#############


#--In JavaScript--#

'''
function binarySearch(arr, num){
  // add whatever parameters you deem necessary - good luck!
  let left = 0;
  let right = arr.length - 1;
  let mid = Math.floor((right + left )/ 2);
 
  while(num !== arr[mid] && left <= right){
      if(num > arr[mid]) left = mid + 1;
      else right = mid - 1;
      mid = Math.floor((right + left )/ 2);
  }
   return num === arr[mid] ? mid : -1;
}
'''

#--In Python--#

'''
import math

def binary_search(arr, num):
    left = 0
    right = len(arr) - 1
    mid = math.floor((right + left) // 2)
    while left <= right and num != arr[mid]:
        if num > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
        mid = math.floor((right + left) // 2)
    if num == arr[mid]:
        return mid
    return -1


print(binary_search([1, 2, 3, 4, 5], 2))
print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5], 5))
print(binary_search([1, 2, 3, 4, 5], 6))
print(binary_search([5,6,10,13,14,18,30,34,35,37,40,44,64,79,84,86,95,96,98,99], 10))
print(binary_search([5,6,10,13,14,18,30,34,35,37,40,44,64,79,84,86,95,96,98,99], 95))
print(binary_search([5,6,10,13,14,18,30,34,35,37,40,44,64,79,84,86,95,96,98,99], 100))
'''

### Naive String Search: Find the recurrence of a substring in a string

#--In JavaScript--#
'''
function subString(lg_str, sm_str){
    let count = 0;
    for(let i = 0; i < lg_str.length; i++){
        for(let j = 0; j< sm_str.length; j++){
           if(lg_str[i] !== sm_str[j]){
              break;
           }
           if(j === sm_str.length - 1){
           count++;
        }
    } 
    return count;
}
'''

#--In Python--#

'''
def sub_string(lg_str, sm_str):
    count = 0
    k = 0
    for i in range(len(lg_str)):
        for j in range(len(sm_str)):
            if lg_str[i+k] != sm_str[j]:
                break
            else:
                k += 1
        if k == len(sm_str):
            count += 1
        k = 0
    return count


print(sub_string('myhellonameishelhoussemloandhelloagain','houssem'))
'''

### KMP Algorithm: Find the recurrence of a substring in a string


#--In JavaScript--#

'''
'''

#--In Python--#

'''
def compute_lps_array(short, m, lps_arr):
    i = 0
    j = 1
    lps_arr[0] = 0
    while j < m:
        if short[j] == short[i]:
            lps_arr[j] = i + 1
            i += 1
            j += 1
        else:
            if i != 0:
                i = lps_arr[i-1]
            else:
                lps_arr[j] = 0
                j += 1


def KMP_search(large, short):
    count = 0
    n = len(large)
    m = len(short)
    lps_arr = [0]*m
    compute_lps_array(short, m, lps_arr)

    i = 0
    j = 0
    while i < n:
        if large[i] == short[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps_arr[j-1]
            else:
                i += 1
        if j == m:
            count += 1
            j = lps_arr[j-1]
    return count

print(KMP_search('myhellonameishelhoussemloandhelloagain','hello'))
'''

###### Third topic: Sorting Algorithms - June 05 2021 ######

           ###########Bubble Sort#############


#--In JavaScript--#
'''
function BubbleSort(arr){
    let temp;
    let noSwaps;
    for(let i = arr.length; i >= 0; i--){
        noSwaps = true;
        for(let j = 0; j < i-1; j++){
            if(arr[j] > arr[j+1]){
                temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
                noSwaps = true;
            }
        }
        if(noSwaps) break;
    }
    return arr;
}
'''

#--In Python--#

'''
def bubble_sort(arr):

    for i in range(len(arr), 0, -1):
        noSwaps = True
        for j in range(0, i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                noSwaps = False
        if noSwaps:
            break
    return arr


print(bubble_sort([12, 34, 5, 56, 11, 99, 123, 3, -12, 234, 11, 66, 11, 7789, 1234, 10, 1, -11, 123456, -1234]))
'''

                              ###########Selection Sort#############


#--In JavaScript--#
'''
function SelectionSort(arr){
    let temp;
    for(let i = 0; i < arr.length; i++){
        let i = lowest;
        for(let j = i+1; j < arr.length ; j++){
            if(arr[j] < arr[lowest]){
                lowest = j;
            }
        }
        if( i !== lowest){
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    return arr;
}
'''

#--In Python--#

'''
def selection_sort(arr):
    for i in range(len(arr)):
        lowest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j
        if i != lowest:
            print(arr)
            temp = arr[i]
            arr[i] = arr[lowest]
            arr[lowest] = temp
    return arr


print(selection_sort([0, 2, 34,22,10,19,17]))
'''

                            ###########Insertion Sort#############


#--In JavaScript--#
'''
function InsertionSort(arr){
    for(let i = 1; i < arr.length; i++){
        let currentVal = arr[i];
        for(let j = i-1; j >= 0 && arr[j] > currentVal ; j--){
            arr[j+1] = arr[j];
        }
         arr[j+1] = currentVal;
    }
    return arr;
}
'''

#--In Python--#

'''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_val = arr[i]
        j = i - 1
        while j >= 0 and current_val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_val
    return arr


print(insertion_sort([12, 11, 13, 5, 6]))
'''

                        ###########Merge Sort#############


#--In JavaScript--#
'''
function Merge(arr1, arr2){
    let n = arr1.length;
    let m = arr2.length;
    let i = 0;
    let j = 0;
    let arr = [];

    while( (i < n) && (j < m)){
        if(arr1[i] < arr2[j]){
            arr.push(arr1[i]);
            i++;
        } else{
            arr.push(arr2[j]);
            j++;
        }
    while(i < n){
        arr.push(arr1[i]);
            i++;
    }
    while(j < m){
        arr.push(arr2[j]);
            j++;
    }
    return arr;
}

function mergeSort(arr){
   if(arr.length === 1) return arr;
   let mid = Math.floor(arr.length / 2);
   let left = mergeSort(arr.slice(0, mid));
   let right = mergeSort(arr.slice(mid));
   return merge(left, right);
}
'''

#--In Python--#

'''
import math

def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    arr = []
    i = 0
    j = 0

    while (i < n) and (j < m):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    while i < n:
        arr.append(arr1[i])
        i += 1
    while j < m:
        arr.append(arr2[j])
        j += 1

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = math.floor(len(arr)/2)
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    return merge(left_arr, right_arr)


print(merge_sort([24, 10, 76, 73, 11]))
'''


                 ###########Quick Sort#############


#--In JavaScript--#
'''
function pivot(arr, start, end){
   let piv = arr[start];
   let piv_index = start;
   let temp;
   for(let i = start + 1; i < end; i++){
        if(arr[i] < piv){
            piv_index++;
            temp = arr[piv_index];
            arr[piv_index] = arr[i];
            arr[i] = temp;
        }
   }
   arr[0] = arr[piv_index];
   arr[piv_index] - piv;
   return piv_index;
}

function quickSort(arr, left = 0, right = arr.length - 1){
   if( left < right){
     let pivotIndex = pivot(arr, left, right);
     // left side of the partition
     quickSort(arr, left, pivotIndex - 1);
     // right side of the partition
     quickSort(arr, pivotIndex + 1, right);
   }
   return arr;
}
'''

#--In Python--#

'''
def pivot(arr, start, end):
    piv = arr[start]
    piv_index = start
    for i in range(start+1, end+1):
        if arr[i] < piv:
            piv_index += 1
            temp = arr[piv_index]
            arr[piv_index] = arr[i]
            arr[i] = temp
    arr[start] = arr[piv_index]
    arr[piv_index] = piv
    #print(piv_index)
    return piv_index


def quick_sort(arr, left, right):
    if left < right:
        pivot_index = pivot(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)
    return arr

arr1 = [4,8,2,1,0,-2]
n = len(arr1)
print(quick_sort(arr1, 0, n-1))
'''


                       ###########Radix Sort#############


#--In JavaScript--#
'''
function getDigit(num, i){
    return Math.floor(Math.abs(num) // Math.pow(10, i)) % 10;
}

function digitCount(num){
    if(num === 0) return 1;
    return Math.floor(Math.log10(Math.abs(num))) + 1;
}

function mostDigits(arr){
    let maxDigits = 0;
    for(let i = 0; i < arr.length; i++){
        maxDigits = max(maxDigits, digitCount(arr[i]));
    }
    return maxDigits;
}

function radixSort(arr):
    maxDigit = mostDigits(arr);

    for(let i = 0; i < maxDigit; i++){
        let bucket = Array.from({length: 10}, () => []);
        for(let j = 0; j < arr.length; j++){
            let index = getDigit(arr[j], i);
            bucket[index].push(arr[j]);
        arr = [].concat(...bucket);
    }
    return arr;
'''

#--In Python--#

'''
import math


def get_digit(num, i):
    return math.floor(abs(num) // math.pow(10, i)) % 10

def digit_count(num):
    if num == 0:
        return 1
    return math.floor(math.log10(abs(num))) + 1

def most_digits(arr):
    max_digits = 0
    for i in range(len(arr)):
        max_digits = max(max_digits, digit_count(arr[i]))
    return max_digits

def radix_sort(arr):
    max_digit = most_digits(arr)

    for i in range(max_digit):
        bucket = [[] for k in range(10)]
        for j in range(len(arr)):
            index = get_digit(arr[j], i)
            bucket[index].append(arr[j])
        arr = []
        for k in range(len(bucket)):
            if bucket[k]:
                arr += bucket[k]
    return arr
    
print(radix_sort([10, 5, 123, 78, 2, 3456, 9999]))
'''

###### Fourth topic: Data Structures - June 10 2021 ######

    ##1##     ###########Singly LinkedLists#############

#--In JavaScript--#

'''
class Node{
    constructor(val){
      this.val = val;
      this.next = null;
    }
}

class SinglyLinkedList{
  constructor(){
     this.head = null;
     this.tail = null;
     this.length = 0;
  }
  // push method
  push(val){
    let newNode = new Node(val);
    if(! this.head){
       this.head = newNode;
       this.tail = this.head;
    } else{
       this.tail.next = newNode;
       this.tail = newNode;
    }
    this.length++;
    return this;
  }
   // unshift method
  unshift(val){
      let newNode = new Node(val);
      if(!this.head){
          this.head = newNode;
          this.tail = this.head;
      } else{
          let currentHead = this.head;
          newNode.next = currentHead;
          this.head = newNode; 
      }
      this.length++;
      return this;
  }
  // get method
  get(index){
      let count = 0;
      let current = this.head;
      if(index < 0 || index >=  this.length) return undefined;
      else{
          while(count < index){
              current = current.next;
              count++;
          }
      }
      return current;
  }
    // set method
  set(index, newVal){
      let current = this.get(index)
      if(current){
          current.val = newVal;
           return true;
      }    
      return false;
  }
  // insert method
  insert(index, val){
      if(index < 0 || index > this.length) return false;
      if(index === this.length) return !!this.push(val);
      if(index === 0) return !!this.unshift(val);

      let newNode = new Node(val);
      let previous = this.get(index - 1);
      let temp = previous.next;
      previous.next = newNode;
      newNode.next = temp;
      this.length++;
      return true;
  }
  // remove method
  remove(index){
      if(index < 0 || index >= this.length) return false;
      if(index === this.length - 1) return !!this.pop();
      if(index === 0) return !!this.shift();

      let previous = this.get(index - 1);
      let deletedNode = previous.next;
      previous.next = deletedNode.next;
      this.length--;
      return deletedNode;
  }
  // reverse method
  reverse(){
      if(this.length === 0) return undefined;
      let count = 0;
      let node = this.head;
      this.head = this.tail;
      this.tail = node;
      let previousNode = null;
      let nextNode;
     
      while(count < this.length){
         nextNode = node.next;
         node.next = previousNode;
         previousNode = node;
         node = nextNode;
          count++;
      }
      return this;
  }
}
'''

#--In Python--#

'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        if not self.head:
            return "undefined"
        current = self.head
        new_tail = current
        while current.next:
            new_tail = current
            current = current.next
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1
        return current

    def shift(self):
        if not self.head:
            return "undefined"
        current_head = self.head
        self.head = current_head.next
        self.length -= 1
        return current_head

    def unshift(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            return 0 ## we want to return undefined
        count = 0
        current = self.head
        while count < index:
            current = current.next
            count += 1
        return current

    def set(self, index, new_val):
        current = self.get(index)
        if current:
            current.val = new_val
            return True
        return False

    def insert(self, index, val):
        if index < 0 or index > self.length:
            return "undefined"
        if index == self.length:
            return not not self.push(val)
        if index == 0:
            return not not self.unshift(val)
        new_node = Node(val)
        previous = self.get(index - 1)
        temp = previous.next
        previous.next = new_node
        new_node.next = temp
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return "undefined"
        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.shift()

        previous_node = self.get(index - 1)
        deleted_node = previous_node.next
        previous_node.next = deleted_node.next
        self.length -= 1
        return deleted_node

    def reverse(self):
        if self.length == 0:
            return "undefined"
        node = self.head
        self.head = self.tail
        self.tail = node
        previous_node = None
        count = 0
        while count < self.length:
            next_node = node.next
            node.next = previous_node
            previous_node = node
            node = next_node
        return self


list = SinglyLinkedList()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)

#print(list.insert(4, 'houssem'))
#print(list.length)
print(list.remove(2).val)
print(list.length)
'''


                    ##2##     ###########Doubly LinkedLists############# June 19 2021


#--In JavaScript--#

'''
class Node{
    constructor(val){
      this.val = val;
      this.next = null;
      this.prev = null;
    }
}

class DoublyLinkedList{
  constructor(){
     this.head = null;
     this.tail = null;
     this.length = 0;
  }
  
  // push method: adding a node to the end of the DLL
  push(val){
    let newNode = new Node(val);
    if(!this.head){
      this.head = newNode;
      this.tail = this.head;
    } else{
      this.tail.next = newNode;
      newNode.prev = this.tail;
      this.tail = newNode;
    }
     this.length++;
     return this;
  }
  // pop method: deleting the last item (the tail) and return it
  pop(){
    if(this.length === 0){
      return undefined;
    }
    let currentTail = this.tail;
    if(this.length === 1){
      this.head = null;
      this.tail = null;
      this.length--;
      return currentTail;
    }
    this.tail = currentTail.prev;
    this.tail.next = null;
    currentTail.prev = null;
    this.length--;
    return currentTail;
  }
  // shift method: removes a node from the beginning of DLL
  shift(){
    if(!this.head) return undefined;
    let oldHead = this.head;
    if(this.length === 1){
      this.head = null;
      this.tail = null;
    } else{
      this.head = oldHead.next;
      this.head.prev = null;
      oldHead.next = null;
    }
    this.length--;
    return oldHead;
  }
   // unshift method: adding a node at the beginning of the DLL
  unshift(val){
    let newNode = new Node(val);
    if(this.length === 0){
      this.head = newNode;
      this.tail = newNode;
    } else{
      this.head.prev = newNode;
      newNode.next = this.head;
      this.head = newNode
    }
    this.length++;
    return this;
  }
  // get method: accessing a node in DLL by its position
  get(index){
    if(index < 0 || index >= this.length){
      return null;
    }
    
    if(index <= this.length / 2){
      let nextNode = this.head;
      let count = 0;
      while(count !== index){
          nextNode = nextNode.next;
          count++;
      }  
       return nextNode;
    } else{
        let prevNode = this.tail;
        let count = this.length - 1;
        while(count !== index){
          prevNode = prevNode.prev;
          count--;
        }
        return prevNode;  
      }
  }
  // set method: replacing the value of a node at a specific position
  set(val, index){
     let node = this.get(index);
     if(node){
       node.val = val;
       return true;
     }
     return false;
  }
  // insert method: adding a node in DLL by a certain position
  insert(val, index){
    let newNode = new Node(val);
    if(index < 0 || index > this.length) return false;
    if(index === 0) return !!this.unshift(val);
    if(index === this.length) return !!this.push(val);
    let prevNode = this.get(index - 1);
    newNode.prev = prevNode;
    newNode.next = prevNode.next;
    prevNode.next.prev = newNode
    prevNode.next = newNode;
    this.length++;
    return true;
  }
  // remove method
  remove(index){
    if(index < 0 || index >= this.length) return undefined;
    if(index === 0) return this.shift();
    if(index === this.length - 1) return this.pop();
    let deletedNode = this.get(index);
    deletedNode.prev.next = deletedNode.next;
    deletedNode.next.prev = deletedNode.prev;
    deletedNode.prev = null;
    deletedNode.next = null;
    this.length--;
    return deletedNode;
  }
  
}
'''

#--In Python--#

'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = 0

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        if self.length == 0:
            return "undefined"
        current_tail = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = current_tail.prev
            self.tail.next = None
            current_tail.prev = None
        self.length -= 1
        return current_tail

    def shift(self):
        if self.length == 0:
            return "undefined"
        old_head = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = old_head.next
            self.head.prev = None
            old_head.next = None
        self.length -= 1
        return old_head

    def unshift(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index <= self.length / 2:
            next_node = self.head
            count = 0
            while count != index:
                next_node = next_node.next
                count += 1
            return next_node
        else:
            prev_node = self.tail
            count = self.length - 1
            while count != index:
                prev_node = prev_node.prev
                count -= 1
            return prev_node

    def set(self, val, index):
        node = self.get(index)
        if node:
            node.val = val
            return True
        return False

    def insert(self, val, index):
        new_node = Node(val)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return not not self.unshift(val)
        if index == self.length:
            return not not self.push(val)
        prev_node = self.get(index - 1)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return "undefined"
        if index == 0:
            return self.shift()
        if index == self.length - 1:
            return self.push()
        deleted_node = self.get(index)
        deleted_node.prev.next = deleted_node.next
        deleted_node.next.prev = deleted_node.prev
        self.length -= 1
        return deleted_node


list = DoublyLinkedList()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)
#list.unshift(10)
#list.unshift(99)
#list.insert(99, 4)
print(list.remove(0).val)
#print(list.insert(4, 'houssem'))
#print(list.length)
#print(list.remove(2).val)
#print(list.head.next.prev.val)
#print(list.pop().val)
#print(list.shift().val)
#print(list.head.val)
#print(list.get(4))
#print(list.set(6, 0))
print(list.length)
print(list.head.val)
'''


                ##3##     ###########Stacks + Queues############# June 20 2021

##STACKS##

# --In JavaScript--#

'''
class Node{
    constructor(val){
        this.val = val;
        this.next = null;
    }
}

class Stack{
    constructor(){
        this.first = null;
        this.last = null;
        this.size = 0;
    }
     // push here is similar to unshift in Single Linked Lists
    push(val){
        let newNode = new Node(val);
        if(this.size === 0){
            this.first = newNode;
            this.last = newNode;
        }else{
            let current = this.first;
            this.first = newNode;
            newNode.next = current;
        }
        return this.size++;
    }
     // pop here is similar to shift in Single Linked Lists
    pop(){
        if(!this.first) return null;
        let current = this.first;
        if(this.size === 1){
            this.last = null;
        }
        this.first = current.next;
        this.size--;
        return current.val;
    }
}


let list = new Stack();

list.push(1);
list.push(2);
list.push(3);
list.push(4);
list.push(5);
}

'''

# --In Python--#

'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, val):
        new_node = Node(val)
        if self.size == 0:
            self.first = new_node
            self.last = new_node
        else:
            current = self.first
            self.first = new_node
            new_node.next = current
        self.size += 1
        return self.size

    def pop(self):
        if self.size == 0:
            return None
        if self.size == 1:
            self.last = None
        current = self.first
        self.first = current.next
        self.size -= 1
        return current.val


list = Stack()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)

print(list.pop())
print(list.pop())
print(list.pop())
print(list.pop())
print(list.pop())
print(list.pop())
'''

##QUEUES##

# --In JavaScript--#

'''
class Node{
    constructor(val){
        this.val = val;
        this.next = null;
    }
}

class Queue{
    constructor(){
        this.first = null;
        this.last = null;
        this.size = 0;
    }
    enqueue(val){
        let newNode = new Node(val);
     if(this.size === 0){
         this.first = newNode;
         this.last = newNode;
     } else{
         let currentLast = this.last;
         this.last = newNode;
         currentLast.next = newNode;
     }
     return this.size++;

    }
    dequeue(){
      if(this.size === 0) return null;
      if(this.size === 1){
          this.last = null;
      }
      let current = this.first;
      this.first = current.next;
      this.size--;
      return current.val;
    }
}


let list = new Queue();

list.enqueue(1);
list.enqueue(2);
list.enqueue(3);
list.enqueue(4);
list.enqueue(5);
'''

# --In Python--#

'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, val):
        new_node = Node(val)
        if self.size == 0:
            self.first = new_node
            self.last = new_node
        else:
            current_last = self.last
            self.last = new_node
            current_last.next = new_node
        self.size += 1
        return self.size

    def dequeue(self):
        if self.size == 0:
            return None
        if self.size == 1:
            self.last = None
        current = self.first
        self.first = current.next
        self.size -= 1
        return current.val


list = Queue()

list.enqueue(1)
list.enqueue(2)
list.enqueue(3)
list.enqueue(4)
print(list.dequeue())
'''


            ##4##     ###########BINARY SEARCH TREES############# June 20 2021

# --In JavaScript--#
'''
class Node{
    constructor(val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree{
    constructor(){
        this.root = null;
    }

    insert(val){
        let newNode = new Node(val);
        
        if(!this.root){
            this.root = newNode;
        } else{
            let current = this.root;
            while(true){
                if(val < current.val){
                    if(current.left === null){
                        current.left = newNode;
                        return this;
                    }
                        current = current.left;
                } else if(val > current.val){
                    if(current.right === null){
                        current.right = newNode;
                        return this;
                    }
                         current = current.right;
                  } else{
                      return undefined;
                  }
             }
         }
    }
    find(val){
        if(!this.root) return false;
        let current = this.root;
            while(true){
                if(val < current.val){
                    if(current.left === null){
                        return false;
                    }
                        current = current.left;
                } else if(val > current.val){
                    if(current.right === null){
                        return false;
                    }
                         current = current.right;
                  } else{
                      return true;
                  }
             }
    }
    ##Breadth First Search##
    BFS(){
       let queue = [];
        let data = [];
        let node = this.root;
        queue.push(node);
        while(queue.length){
            node = queue.shift()
            data.push(node.val);
            if(node.left) queue.push(node.left);
            if(node.right) queue.push(node.right)
        }
        return data;
    }
     // Depth First Search: PreOrder
    DFSPreorder(){
        let data = [];
        let current = this.root;
        function preOrder(node){
            data.push(node.val);
            if(node.left) preOrder(node.left);
            if(node.right) preOrder(node.right);
        }
        preOrder(current);
        return data; 
    }
    // Depth First Search: PostOrder
    DFSPostorder(){
        let data = [];
        let current = this.root;
        function postOrder(node){
            if(node.left) postOrder(node.left);
            if(node.right) postOrder(node.right);
             data.push(node.val);
        }
        postOrder(current);
        return data; 
    }
    // Depth First Search: InOrder
    DFSInorder(){
        let data = [];
        let current = this.root;
        function inOrder(node){
            if(node.left) inOrder(node.left);
             data.push(node.val);
            if(node.right) inOrder(node.right);
        }
        inOrder(current);
        return data; 
    }
    
}


let newBst = new BinarySearchTree();

newBst.insert(10);
newBst.insert(5);
newBst.insert(2);
newBst.insert(7);
newBst.insert(13);
newBst.insert(11);
newBst.insert(16);
'''

# --In Python--#
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while True:
                if val < current.val:
                    if not current.left:
                        current.left = new_node
                        return self
                    current = current.left
                elif val > current.val:
                    if not current.right:
                        current.right = new_node
                        return self
                    current = current.right
                else:
                    return "undefined"

    def find(self, val):
        if not self.root:
            return False
        else:
            current = self.root
            while True:
                if val < current.val:
                    if not current.left:
                        return False
                    current = current.left
                elif val > current.val:
                    if not current.right:
                        return False
                    current = current.right
                else:
                    return True
    # Breadth First Search
    def BFS(self):
        queue = []  # implemented an array type queue
        data = []
        node = self.root
        queue.append(node)
        while len(queue):
            node = queue.pop(0)
            data.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return data

    # Depth First Search: PreOrder
    def DFS_preorder(self):
        data = []
        current = self.root
        def pre_order(node):
            data.append(node.val)
            if node.left:
                pre_order(node.left)
            if node.right:
                pre_order(node.right)
        pre_order(current)
        return data

    # Depth First Search: PostOrder
    def DFS_postorder(self):
        data = []
        current = self.root
        def post_order(node):
            if node.left:
                post_order(node.left)
            if node.right:
                post_order(node.right)
            data.append(node.val)
        post_order(current)
        return data

    # Depth First Search: InOrder
    def DFS_inorder(self):
        data = []
        current = self.root

        def in_order(node):
            if node.left:
                in_order(node.left)
            data.append(node.val)
            if node.right:
                in_order(node.right)
        in_order(current)
        return data



newBst = binary_search_tree()
newBst.insert(10)
newBst.insert(6)
newBst.insert(15)
newBst.insert(3)
newBst.insert(8)
newBst.insert(20)

#print(new_bst.root.left.left.left)

#print(newBst.DFS_preorder())
#print(newBst.DFS_postorder())
print(newBst.DFS_inorder())
'''


                 ##5##     ###########BINARY HEAPS############# June 28 2021

# --In JavaScript--#
'''
class MaxBinaryHeap{
    constructor(){
        this.values = [];
    }
    insert(val){
        this.values.push(val);
        let index = this.values.length - 1;
        let parentIndex = Math.floor((index - 1)/2);
        while(this.values[parentIndex] < this.values[index] && index > 0){
            let temp = this.values[index];
            this.values[index] = this.values[parentIndex];
            this.values[parentIndex] = temp;
            index = parentIndex;
            parentIndex = Math.floor((index - 1)/2);
        }
        return this.values;
    }
}


let heap = new MaxBinaryHeap();

heap.insert(41);
heap.insert(39);
heap.insert(33);
heap.insert(18);
heap.insert(27);
heap.insert(12);
'''

# --In Python--#
import math
class max_binary_heap:
    def __init__(self):
        self.values = []

    def insert(self, val):
        self.values.append(val)
        index = len(self.values) - 1
        parent_index = math.floor((index-1)/2)
        while (self.values[parent_index] < self.values[index]) and index > 0:
            temp = self.values[index]
            self.values[index] = self.values[parent_index]
            self.values[parent_index] = temp
            index = parent_index
            parent_index = math.floor((index - 1) / 2)
        return self.values


heap = max_binary_heap()
heap.insert(41)
heap.insert(39)
heap.insert(33)
heap.insert(18)
heap.insert(27)
heap.insert(12)
heap.insert(55)
heap.insert(1)
heap.insert(100)

print(heap.values)