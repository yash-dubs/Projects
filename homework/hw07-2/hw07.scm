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
  (cond ((= 0 y) 1) ; base
    ((even? y) (square (pow x (/ y 2)))) ; (b^k)^2
    (else (* x (pow x (- y 1)))) ; b(b^k)^2

)
)

;(if (= 0 y) 1
 ; (if (even? y) (square (pow x (/ y 2)))
  ;    ( (* x (square( (pow x (- y 1)))))
  ;)
  ;)
;)
;)


(define (unique s)
  (cond ((null? s) 
  
    nil)

  
      ; base case, null/nil; recursive, create new list, car begin, use filter with lambda (recursive call included)
      ;rest of items; filter returns bool and lst, and applies bool to lst


     ;item 1
    ;(define (unique-helper y x)
    
    ;(cons
    ;(y)
    ;(filter (not (equal? x (car s))) (unique (cdr s))))
    

      (else 
      
      (cons
      (car s)
      (filter (lambda (elem) (not (equal? elem (car s)))) ; filter w/lambda
      
      (unique (cdr s))) ; recursive call on rest of the list
      
      )
      )
      
      ) 
    
    )
  
  
  






(define (replicate x n)
 (define (replicate-helper y z lst)

     (if (= z 0) 
        lst
        (replicate-helper y (- z 1) (cons y lst))
     
      )
  
  
  )

  (replicate-helper x n nil)
  
  )

  ;(define (replicate x n)
	;(if (= n 0)
  ;nil
	;	(cons x (replicate x (- n 1)))))


(define (accumulate combiner start n term)

  (if (= n 0) start


    (accumulate combiner (combiner start (term n)) (- n 1) term)
  
  
  )



)



(define (accumulate-tail combiner start n term)
  (if (= n 0) start


    (accumulate combiner (combiner start (term n)) (- n 1) term)
  
  
  )
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  (define lst nil)
  (for var in lst)
   (if filter-expr:)
          (cons map-expr(var), lst)

  (lst)
)

