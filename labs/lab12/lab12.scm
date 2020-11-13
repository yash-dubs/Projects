
(define-macro (def func args body)
    
      
      `(define ,(cons func args) ,body
      
      
      )
      
      


)



(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define all-three-multiples
  (begin
    (define (threes n)
      (cons-stream (+ 3 n) (threes (+ 3 n)))
  )
  (threes 0)
)
)


(define (compose-all funcs)
  'YOUR-CODE-HERE
)


(define (partial-sums stream)
  'YOUR-CODE-HERE
  (helper 0 stream)
)

