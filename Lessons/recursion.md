## Recursion

#### What is recursion?

- Two main instances of recursion
  1. Is a technique in which a function makes one or more calls to itself. More common and our major focus for now.
  2. When a data structure uses smaller instances of the exact same type of data structure when it represent itself.

#### Why use recursion?

- It provides a powerful alternative for performing repetitions os tasks in which a loop is not ideal.
- Most modern programming languages support recursion
- Recursion servers as a great tool for building out particular data structures

#### Examples

1. Factorial example =>
   n! = n x (n-1) x (n-2) ... 3 x 2 x 1
   n! = n x (n-1)!
   0! = 1

   Recursive case is: n! = n x (n-1)!
   Base case is: n = 0 because 0! = 1

   Whenever you are trying to develop a recursive solution it is very important to think about the base case, as your solution will need to return the base case once all the recursive cases have been worked through.

#### Memoization

Memoization effectively refers to remembering ('memoization' -> 'memorandum' -> to be remembered) results of method calls based on the method inputs and then returning the remembered result rather than computing the result again. You can think of it as a cache for method results. We'll use this in some of the interview problems as improved versions of a purely recursive solution.
