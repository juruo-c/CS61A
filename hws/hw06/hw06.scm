(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)


(define (sign num)
  'YOUR-CODE-HERE
  (cond
    ((< num 0) -1)
    ((> num 0) 1)
    (else 0)
  )
)


(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE
  (cond 
    ((= x 1) 1)
    ((= y 1) x)
    ((= y 0) 1)
    (else (* (square x) (pow x (- y 2))))
  )
)

