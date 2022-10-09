(define (split-at lst n)
  'YOUR-CODE-HERE
  (if (or (null? lst) (= n 0))
    (cons nil lst)
    (cons (append (cons (car lst) nil) (car (split-at (cdr lst) (- n 1)))) (cdr (split-at (cdr lst) (- n 1))))
  )
)


(define (compose-all funcs)
  'YOUR-CODE-HERE
  (if (null? funcs)
      (lambda (x) x)
      (lambda (x)
        ((compose-all (cdr funcs)) ((car funcs) x))
      )
  )
)

