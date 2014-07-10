;
; 1.
;    1
;    1
;    1
;    1
;    a
;    a
;
;
; STk> (if (or #t (/ 1 0)) 1 (/ 1 0))
; ? two time attempted division by zero -> error ?
; 
; ok, dynamic language ;-) : the "#t" -true is evaluated
; since "true" the first div. by zero is evaluated.
; so the whole block (or...) returns "true" so "1"
; is returned, the else-block (second div. by zero)
; is not considered.
;
; STk> (if (> 4 3) (+ 1 2 3 4) (+ 3 4 (* 3 2)))
; ? returns "10"
;
; STk> ((if (< 4 3) + -) 4 100)
; ? false, "-" is returned, so the operator to combine the 
; numbers is "-". 4-100 = -96

; some tests
(define ( identity x ) ( + x ))
(define (square x) (* x x))

; "nil" as a synonym for the empty list is not build in MIT scheme
; so lets' define it
(define nil '())

(define (sin x)
  (if (< x 0.000001)
    x
    (let ( (recursive-step (sin (/ x 3))) )
      (- (* 3 recursive-step)
         (* 4 (expt recursive-step 3))))))
;
; 4.1 Questions
; 1. Write a function that calculates factorial. (Note how you haven’t been told any meth-
;                                                      ods for iteration.)
(define (factorial x)
  ( if ( = x 0) 
     1 
     (* x (factorial (- x 1)))))    

; 2. Write a function that calculates the Nth fibonacci number
(define (fib n)
  (if (< n 2)
    1
    (+ (fib (- n 1)) (fib (- n 2)))))

; 1. Define map where the first argument is a function and the second a list. This should
;    work like Python’s map.
;
; YESSS - it works!!!
(define (map fn lst)
  (if (null? (cdr lst))
    (cons (fn (car lst)) nil)  ; return a pair with 2. element nil
    (cons (fn (car lst)) (map fn (cdr lst)))))

; 2. Define reduce where the first argument is a function that takes two arguments, the
;    second a default value and the third a list. This should work like Python’s reduce.

( define add + )
(define (reduce fn s lst)
  (if (null? (cdr lst))
    (fn s (car lst))
    (reduce fn (fn s (car lst)) (cdr lst))))



