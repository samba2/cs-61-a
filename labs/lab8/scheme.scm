; CS61A Lab 5b

; Cubes the input x
(define (cube x)
   (* x x x)) 

; Calculates the factorial of x recursively
(define (factorial_recursive x)
  (if ( = 0 x ) 
    1
    ( *  x (factorial_recursive (- x 1)))))

; Calculates the factorial of x iterativel
(define (factorial_iterative x)
    (fac-iter 1 1 x))

( define (fac-iter sum cnt max_cnt)
    (if (> cnt max_cnt)
      sum
      (fac-iter (* sum cnt) (+ cnt 1) max_cnt ))) 

(define structure 
  (cons (cons 1 '() ) (cons 2 (cons (cons 3 4) (cons 5 '()) )) )
)

; solution:
; (define structure (cons (cons 1 '()) (cons 2 (cons (cons 3 4) (cons 5 '())))))

(define (remove item lst)
   (cond ((null? lst) '())
         (( = item (car lst )) ( remove item (cdr lst)))
         (else (cons (car lst) (remove item (cdr lst))))))

; solution:
;  (cond ((null? lst) '())
;  ((equal? item (car lst)) (remove item (cdr lst)))
;  (else (cons (car lst) (remove item (cdr lst))))))
; 
; my stuff didn't work since "else" was missing. now it's running fine.


; yepp
(define (filter f lst)
   (cond ((null? lst) '())
         (( f (car lst )) (cons (car lst) (filter f (cdr lst))))
         (else (filter f (cdr lst))))) 

; manually...
; if pred is true for each element of the list then the whole list is true
; as soon as pred check fails recursion stopps and "false" is signaled
(define (all_satisfies lst pred)
    (cond ((null? lst) #t)
          ( (pred (car lst)) (all_satisfies (cdr lst) pred))
          (else #f)))

; solution reused "filter":
; (define (all_satisfies lst pred)
;   (= (length (filter pred lst)) (length lst)))

