4.1 Write a function that returns the factorial of a number.
(define (factorial x)
    (if (< x 2) 
        1 
        (* x (factorial (- x 1)))
    )
)

4.2 Tutorial: Write a function that returns the n
th Fibonacci number.
(define (fib n)
    (if (< n 2)
        n
        (+ (fib (- n 1)) (fib (- n 2)))
    )
)
scm> (fib 0)
0
scm> (fib 1)
1
scm> (fib 10)
55

5.1 Write a function which takes two lists and concatenates them.
Notice that simply calling (cons a b) would not work because it will create a
deep list. Do not call the builtin procedure append, which does the same thing as
my-append.
(define (my-append a b)
    (if null? a 
        b 
        (cons (car a) (my-append (cdr a) b))
    )
)
scm> (my-append '(1 2 3) '(2 3 4))
(1 2 3 2 3 4)

5.2 Tutorial: These short questions are meant to help refresh your memory of topics
covered in lecture and lab this week before tackling more challenging problems.
Describe the difference between the following two Scheme expressions. Hint: which
defines a new procedure?
Expression A:
(define x (+ 1 2 3))
Expression B:
(define (x) (+ 1 2 3))
Write an expression that selects the value 3 from the list below.
(define s '(5 4 (1 2) 3 7))

(car (cdr (cdr (cdr s))))


5.3 Tutorial: Write a Scheme function that, when given a list, such as (1 2 3 4),
duplicates every element in the list (i.e. (1 1 2 2 3 3 4 4)).
(define (duplicate lst)
    (if null? lst
        lst 
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
    )
)

5.4 Tutorial: Write a Scheme function that, when given an element, a list, and an
index, inserts the element into the list at that index.
(define (insert element lst index)
    (if (= index 0)
        (cons element lst)
        (cons (car lst) (insert element (cdr lst) (- index 1)))
    )
)