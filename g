; Лабораторная работа №5
; NASM x64 для SASM

global main

extern scanf
extern printf
extern MessageBoxA

section .data

    fmtIn      db "%lf %lf",0
    fmtOut     db "Гипотенуза = %.6lf",10,0

    cat1       dq 0.0
    cat2       dq 0.0
    hypotenuse dq 0.0

    msgText    db "Повторить ввод данных?",0
    msgCaption db "Лабораторная работа №5",0

    MB_YESNO   equ 4
    IDYES      equ 6

section .text

main:

start:

    ; scanf("%lf %lf", &cat1, &cat2)

    sub rsp, 32

    mov rcx, fmtIn
    mov rdx, cat1
    mov r8,  cat2

    call scanf

    add rsp, 32

    ; Вычисление:
    ; hypotenuse = sqrt(cat1^2 + cat2^2)
    ; через математический сопроцессор x87

    fld qword [cat1]
    fmul st0, st0

    fld qword [cat2]
    fmul st0, st0

    faddp st1, st0

    fsqrt

    fstp qword [hypotenuse]

    ; printf("Гипотенуза = %.6lf\n", hypotenuse)

    sub rsp, 40

    mov rcx, fmtOut

    movsd xmm0, [hypotenuse]
    movq rdx, xmm0

    call printf

    add rsp, 40

    ; MessageBoxA(NULL,
    ;             "Повторить ввод данных?",
    ;             "Лабораторная работа №5",
    ;             MB_YESNO)

    sub rsp, 32

    xor rcx, rcx
    mov rdx, msgText
    mov r8,  msgCaption
    mov r9d, MB_YESNO

    call MessageBoxA

    add rsp, 32

    cmp eax, IDYES
    je start

    xor eax, eax
    ret
