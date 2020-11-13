(define (rle s)
    ;need helper, outside helper usual null nill call helper 

     (define (helperz num carz n) ;helper

        (if (null? num) (cons-stream (list carz n) nil)

        (if (not(= carz (car num))) ;small else
                
        (cons-stream (list carz n) (helperz (cdr-stream num) (car num) 1)) 
        
        (helperz (cdr-stream num) carz (+ n 1)))));big else // recursive
                 

                 

    (begin
    (if (null? s) nil

    (helperz (cdr-stream s) (car s) 1)

    )
    )
)





(define (group-by-nondecreasing s)
    (define helper
    ;hwrecoveryneeded
        (0)
    )
)

(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

