; Вызывающие выражения

(+ 1 2 3 4)

(+)

(*)

(- 12)

(- 20 1 2 3 4 5)

(/ (+ (* (- (* 2 2 2 2 2 3 3 3) 1) 7) 1) 3)

(number? 12)

(integer? 3.3)

(zero? 2)

; Определения

(define (square x) (* x x))

(define (average x y) (/ (+ x y) 2))

(define (abs x)
  (if (< x 0)
      (- x)
      x))

(define (sqrt x)
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess)
    (if (= (square guess) x)
        guess
        (sqrt-iter (improve guess))))
  (sqrt-iter 1))

; Списки

(cons 1 2)
(cons 1 (cons 2 nil))
(cons 1 (cons 2 (cons 3 4)))
(cons (cons 1 2) 2)
(cons (cons 1 2) nil)
(cons (cons 1 (cons 2 nil)) nil)
(cons (cons 1 2) (cons 3 nil))

(pair? (cons 1 2))
(pair? (cons 1 (cons 2 nil)))
(pair? nil)
(null? nil)
(null? (cons 1 2))

(list 1 2)
(list 1 2 3 4)
(cdr (list 1 2 3 4))

(define x (cons 1 2))
(list (car x) (cdr x))
(cons (car x) (cons (cdr x) nil))

(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

(define squares (list 1 4 9 16 25))

(length squares)

; треугольник Серпинского

(define (repeat k fn)
  ; Повторить fn k раз.
  (if (> k 1)
      (begin (fn) (repeat (- k 1) fn))
      (fn)))

(define (tri fn)
  ; Повторить fn раза 3 с поворотом на 120 градусов за ход.
  (repeat 3 (lambda () (fn) (lt 120))))

(define (sier d k)
  ; Рисует три ребра треугольника Серпинского глубины d.
  (tri (lambda ()
         (if (= k 1) (fd d) (leg d k)))))

(define (leg d k)
  ; Рисует одно ребро Серпинского глубины d.
  (sier (/ d 2) (- k 1))
  (penup)
  (fd d)
  (pendown))

(sier 400 6)