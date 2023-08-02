;   created by:     Rucker, Zaki
;   submitted on:   26 November
;   class:          CS3140
;   project:        assignment 4
;   to build:       nasm -f elf64 -g assign4.asm
;                   gcc -o assign4 -m64 main.c assign4.o start.o -nostdlib -nodefaultlibs -fno-builtin -nostartfiles
;   cl arguments:   none

bits 64


section .text

;global _start          ; _start is provided in start.asm
global l_strlen         ; make l_strlen visible to the linker
global l_strcmp         ; make l_strcmp visible to the linker
global l_gets           ; make l_gets visible to the linker
global l_puts           ; make l_puts visible to the linker
global l_write          ; make l_write visible to the linker
global l_open           ; make l_open visible to the linker
global l_close          ; make l_close visible to the linker
global l_exit           ; make l_exit visible to the linker
global l_atoi           ; make l_atoi visible to the linker
global l_itoa           ; make l_itoa visible to the linker
global l_rand           ; make l_rand visible to the linker

; passing parameters: rdi, rsi, rdx, rcx, r8, r9
; can be changed(clobberable): rdi, rsi, rdx, rcx, r8, r9, r10, r11
; return value placed in: rax

;_start:

l_strlen:           
; return the length of a null terminated string
; int l_strlen(char *str);

    mov     rax, 0
.loop:
    cmp     byte[rdi+rax], 0
    jz      .done
    inc     rax
    jmp     .loop
.done:
    ret

l_strcmp:           
; return 0 if two strings are equal                                                
; int l_strcmp(char *strl, char *str2);
; given rdi & rsi

    mov     rax, 0
.loop:
    mov     dl, byte[rsi+rax]
    cmp     byte[rdi+rax], dl
    jnz     .nopotatoe
    cmp     byte[rdi+rax], 0
    jz      .done
.inc:
    inc     rax
    jmp     .loop
.nopotatoe:
    mov     rax, 1
    ret
.done:
    mov     rax, 0
    ret

l_gets:             
; read from file and place in buffer
; int l_gets(int fd, char *buf, int len);
; given rdi, rsi, rdx

    mov     r8, 0                   ; prepare an indexer to offset in the buffer
    cmp     rdx, 0                  ; compare bytes passed to 0
    jnz     .g2go                   ; fail: we are good to go further
    jmp     .done                   ; success: terminate 
.g2go:
    dec     rdx                     ; decrement rdx so we read 1 less
    mov     r9, rdx                 ; move len -1 to r9, to track
    mov     rdx, 1                  ; set rdx to read 1 byte at a time
.loop:
    mov     sil, byte[rsi+r8]       ; prepare to read one byte (was erroring changed from rsi)
    mov     rax, 0                  ; setup read call
    syscall                         ; read
    cmp     sil, 0x0a               ; check for a line feed (*see line 83)
    jz      .nl                     ; success: terminate early
    inc     r8                      ; fail: increment the indexer
    cmp     r9, r8                  ; check for len -1
    jnz     .loop                   ; fail: loop until incrementer = len -1
.done:                               ; success: .done
    mov     byte[rsi+r8+1], 0       ; place null after last read byte
    mov     rax, [r8]               ; setup the incrementer value to be returned
    ret                             ; return
.nl:
    inc     r8                      ; if the new line was present count it in the incrementer
    jmp     .done                   ; terminate early

l_puts:             
; write string in buffer to stdout
; void l_puts(const char *buf);
; given rdi

    mov     r9, rdi                 ; copy buffer pointer because I need rdi
    mov     r8, 0                   ; prepare an indexer
    mov     rdx, 1                  ; initialize the length of the write systemcall
.loop:
    cmp     byte[r9+r8], 0          ; compare current byte to null (see *106)
    jz      .done                   ; success: jump to done
    lea     rsi, [r9+r8]            ; initialize the byte to be written
    mov     rdi, 1                  ; output = stdout
    mov     rax, 1                  ; prep kernel to write
    syscall                         ; invoke kernel to write
    inc     r8                      ; increment the counter
    jmp     .loop                   ; return to loop
.done:
    ret                             ; return     

l_write:            ; write buffer to file
; int l_write(int fd, char *buf, int len, int *err);
; given:  rdi, rsi, rdx, rcx

    mov     rbx, rcx                ; 
    mov     rax, 1                  ; prep kernel to write
    syscall                         ; invoke kernel to write
    cmp     rax, 0                  ; check the return value
    jns     .ok                     ; success: jmp to prepare to return
    neg     rax                     ; fail: change the sign of the return value (error message)
    mov     [rcx], rax              ; move the error message to the error pointer
    mov     rax, -1                 ; return a value that indicates an error
.ok:
    ret                             ; return

l_open:             
; open a file
; int l_open(const char *name, int flags, int mode, int *err);
; given: rdi, rsi, rdx, rcx
; open systemcall needs: 
    
    mov     rax, 2                  ; setup open syscall
    syscall                         ; invoke system call
    mov     rcx, 0                  ; set error code to 0
    cmp     rax, 0                  ; check the return value
    jns     .ok                     ; success: jmp to prepare to return
    neg     rax                     ; fail: abs value the error value
    mov     [rcx], rax              ; move error message to the error pointer
    mov     rax, -1                 ; setup error indicator to return
.ok:
    ret

l_close:            
; close a file
; int l_close(int fd, int *err);
; given: rdi, rsi    
    
    mov     rax, 3                  ; setup close syscall
    syscall                         ; invoke system call
    mov     rsi, 0                  ; set error code to 0
    cmp     rax, 0                  ; check the return value
    jns     .ok                     ; success: jmp to prepare to return
    neg     rax                     ; fail: abs value the error value
    mov     [rsi], rax              ; move error message to the error pointer
    ;mov     rsi, rax 
    mov     rax, -1                 ; setup error indicator to return
.ok:
    ret
   
l_exit:             
; terminate with exit code rc.
; void l_exit(int rc);
; given: rdi
   
    mov     rax, 60                 ; setup exit system call
    syscall

;              NEXT LEVEL STUFF

l_atoi:             
; ascii to integer conversion
; unsigned int l_atoi(char *value);
; given: rdi

    mov     rbx, rdi                  ; intialize rax to use al 
    mov     rcx, 0                  ; intialize an indexer
    mov     rax, 0
    mov     r9, 0
.check:
    cmp     byte[rbx+rcx], 0x30     ; check for a byte less than 0x30
    jl      .done                   ; success: not ascii numeral
    cmp     byte[rbx+rcx], 0x39     ; check for byte greater than 0x39
    jg      .done                  ; success: not ascii numeral
    sub     byte[rbx+rcx], 0x30                ; convert the ascii byte value to the numeral it represents
;    mov     al, byte[rbx,rcx]
    mov     r8, 10                  ; setup to mul by 10
    mul     r8                      ; multiply the byte by 10
    movzx   r9, byte[rbx+rcx]
    add     rax, r9
    inc     rcx
    jmp     .check
.done:
    ret

l_itoa:             
; integer to ascii conversion
; char *l_itoa(unsigned int value, char *buffer);
; given rdi, rsi

    mov     rax, rdi                ; move int to register to work on
    push    rsi
;    mov     rbx, rsi                ; destination buffer to return
    mov     r9, 0                   ; initialize
    mov     rcx, 0                  ; initialize counter
    mov     r8, 10                  ; initialize for arithmetic operations
.loop:
    mov     rdx, 0                  ; initialize
    div     r8                      ; divide 
    add     dl, 0x30                ; convert a decimal to ascii range
    mov     byte[rsi+rcx], dl       ; move the resultant to rbx
    inc     rcx
    cmp     rax, 0                  ; check for completion
    jnz     .loop
    pop     rax
    mov     r12, rcx
    shr     r12, 1
.done:    
    dec     rcx
    mov     r11b, byte[rsi+rcx]
 ;   mov     r10b, byte[rax+r9]
 ;   mov     byte[rsi+rcx], r10b
    mov     byte[rax+r9], r11b
;    xchg    byte[rax+r9],byte[rsi+rcx] 
    inc     r9
    dec     r12
    cmp     r12, 0
    jnz     .done
    ret

l_rand:             
; generate a random number
; unsigned int l_rand(unsigned int n);
; given: rdi

    mov     rdi, random
    mov     rsi, 0
    mov     rdx, 0
.done:
    ret             ; return to caller

section .data
random: db '/dev/urandom'
random_len equ $-random
pad: times (256 - random_len) db 0


section .bss

msg:    resb 1000   ;
