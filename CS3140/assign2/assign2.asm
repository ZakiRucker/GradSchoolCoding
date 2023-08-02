; bubble sort in assembly
; created by Zaki
; used in low level II with Chris Eagle
:
; assembled with: nasm -f macho32 -g assign2.asm
; linked with: ld -o assign3 -m elf_x86_64 assign3.o   


;bits 64

global start

section .text


; do not rename or delete any of the labels in this program
start:
        mov     edx, ARRAY_LEN - 1
outerloop:
        mov     ecx, 0
innerloop:
        mov     ax, [array + ecx]
        cmp     al, ah
        jl      next
        xchg    al, ah
        mov     [array + ecx], ax
next:
        inc     ecx
        cmp     ecx, edx
        jl      innerloop
endinner:
        dec     edx
        jnz     outerloop
done:
        mov     edi, 0
        mov     eax, 60
        syscall 

section .data

; ------ DO NOT CHANGE ANYTHING BETWEEN HERE ----------
; This variable must remain named exactly 'array'
array: db 'Will you please sort this string for me?'
ARRAY_LEN equ $-array
pad: times (256 - ARRAY_LEN) db 0
; ------------------ AND HERE -------------------------

