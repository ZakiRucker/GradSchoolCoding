;   created by:     Rucker, Zaki
;   submitted on:   7 November
;   class:          CS3140
;   project:        assignment 3
;   to assemble:    nasm -f elf64 -g assign3.asm
;   to link:        ld -o assign3 -m elf_x86_64 assign3.o
;   cl arguments:   none

bits 64

%define STDIN 0
%define BUF_LEN 1000

section .text

;global _start

;_start:
read:   
        mov     rdi, STDIN      ; from stdin
        mov     rsi, buf        ; point location of my buffer
        mov     rdx, BUF_LEN    ; set max read length
        mov     rax, 0          ; setup syscode to read
        syscall                 ; execute read call
        cmp     rax, 1          ; compare return value to 1
        jge     flip            ; catch all return values other than 1

done:
        mov     edi, 0          ; desired value to return
        mov     eax, 60         ; setup syscode to exit
        syscall                 ; execute exit syscall


flip:   
        mov     rcx, 0
next:   
        cmp     rax, rcx
        jz      write
        mov     sil, byte [buf+rcx]     ; set up message 
        cmp     sil, 0x41               ; compare to upper case floor
        jl      nope                    ; smaller than ASCII jump to next character
        cmp     sil, 0x5a               ; compare to upper case ceiling
        jle     .flop                   ; catches upper case only
        cmp     sil, 0x7a               ; compare to lower case ceiling
        jg      nope                    ; catch greater than ASCII
        cmp     sil, 0x61               ; compare to lower case floor
        jl      nope                    ; the non alphebet ASCII characters between the cases
.flop:  xor     sil, 0x20               ; flip the bit to change the case
nope:  
        mov     byte [buf+rcx], sil     ; be sure to return the byte
        inc     rcx                     ; increment counter
        jmp     next                    ; loop back to read more
        
write:  
        mov     rsi, buf        ; set to write from buf
        mov     rdi, 1          ; to stdout
        mov     rdx, rax        ; set output to write of read
        mov     rax, 1          ; syscode to write
        syscall                 ; execute the write
        jmp     read            ; prepare to do it all again
       
section .bss

buf:     resb 1000

