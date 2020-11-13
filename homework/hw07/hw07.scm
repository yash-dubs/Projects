(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond ((> num 0) 1) ((= num 0) 0) (else -1))
)


(define (square x) (* x x))

(define (pow x y)
(cond (= 0 y) (1)
    (even? (* y 2)) (square (pow x y))
    (odd? (+ (* 2 y) 1)) (* x (pow x y))

))

;(if (= 0 y) 1
 ; (if (even? y) (square (pow x (/ y 2)))
  ;    ( (* x (square( (pow x (- y 1)))))
  ;)
  ;)
;)
;)


(define (unique s)
  'YOUR-CODE-HERE
)


(define (replicate x n)
  'YOUR-CODE-HERE
  )


(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
)


(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
)

