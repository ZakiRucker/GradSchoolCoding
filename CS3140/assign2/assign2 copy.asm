;   created by:     Rucker, Zaki
;   submitted on:   27 October
;   class:          CS3140
;   project:        assignment 2
;   to assemble:    nasm -f elf64 -g assign2.asm
;   to link:        ld -o assign2 -m elf_x86_64 assign2.o
;   cl arguments:   none

bits 64

section .text

global _start

; do not rename or delete any of the labels in this program
_start:
        mov     edx, ARRAY_LEN - 1              ; use to index array
        mov     ebx, 0                          ; initialize my passes counter
        mov     r8d, 0                          ; initialize my swaps counter            
        mov     r9d, 0                          ; initialize my last swap number
outerloop:
        mov     ecx, 0                          ; this will count how many chars are put into position
innerloop:
        mov     ax, [array + ecx]               ; move the first two chars into a general register
        cmp     al, ah                          ; compare the first two chars
        jge     next                            ; if the first is smaller than or equal to the second jump past the exchange
        xchg    al, ah                          ; swap the two chars
        inc     r8d                             ; increment the swaps counter
        mov     [swaps], r8d                    ; move the swap counter to swaps
        mov     [array + ecx], ax               ; place the newly sorted chars back into the array
next:
        inc     ecx                             ; move to the index of the next two chars
        cmp     ecx, edx                        ; check that we are not at the end of the array
        jl      innerloop                       ; restart the inner loop (sort the next byte)
endinner:
        cmp     dword   [swaps], 0              ; check if the bubbles start off sorted
        jz      iliketomoveitmoveit             ; the bubbles started sorted (edge case)                    
        cmp     [swaps], r9d                    ; compare the last value to the current value
        jz      iliketomoveitmoveit             ; jump if there was no change
        mov     r9d, [swaps]                    ; save swap value to check next time around
        inc     ebx                             ; increment passes counter
        mov     [passes], ebx                   ; move the passes counter to passes
        dec     edx                             ; the first char should be in place. we do not need to sort to this position again
        jnz     outerloop                       ; start the outerloop again to begin to move the next byte into position
iliketomoveitmoveit:
        mov     edx, ARRAY_LEN                  ; use to limit copies to length of the array
        mov     ecx, 0                          ; use for offset
moveit:
        mov     al, [array + ecx]               ; copy from source to al
        mov     [output + ecx], al              ; copy from al to destination
        inc     ecx                             ; increment the offset
        cmp     ecx, edx                        ; index to array length
        jl      moveit                          ; do it again, you're not done
done:
        mov     edi, [passes]                   ; passes to edi to return
        mov     eax, 60                         ; setup for syscall
        syscall                                 ; close the file

section .data


; ------ DO NOT CHANGE ANYTHING BETWEEN HERE ----------
; This variable must remain named exactly 'array'
array: db 'Will you please sort this string for me?'
ARRAY_LEN equ $-array
pad: times (256 - ARRAY_LEN) db 0
; ------------------ AND HERE -------------------------

passes:     dd  0                               ; variable to count the passes of the inner loop
swaps:      dd  0                               ; variable to count the number of swaps conducted

section .bss

output:     resb 256                            ; reserve 256 byte array for output
