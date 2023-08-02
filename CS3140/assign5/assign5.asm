;   created by:     Rucker, Zaki
;   submitted on:   7 Decamber
;   class:          CS3140
;   project:        assignment 5 "NetCat"
;   to assemble:    nasm -f elf64 -g assign5.asm
;   to link:        ld -o assign5 -m elf_x86_64 assign5.o assign3.o assign4.o dns64.o
;   cl arguments:   url and port
;   Can you write a program in assembly that behaves similar to netcat?

bits 64

extern  resolv
extern  l_atoi

%define SC_READ 0       ; rdi = int fd, rsi = char *buf, rdx = size_t len
%define SC_WRITE 1      ; rdi = int fd, rsi = char *buf, rdx = size_t len
%define SC_FORK 57      ; rdi = 
%define SC_EXECVE 59    ; rdi = char *file, rsi = char **argv, rdx = char **envp
%define SC_EXIT 60      ; rdi = retval
%define SC_WAIT4 61     ; rdi = pid_t pid, rsi = int*wstatus, rdx = int options, r10 = struct rusage *rusage
%define SC_CLOSE 3      ; rdi = fd
%define SC_SOCKET 41    ; rdi = int family, rsi = int type, rdx = int protocol
%define SC_CONNECT 42   ; rdi = sock fd, rsi = sock address, rdx = sock len
%define SC_DUP2 33      ; rdi = old fd, rsi = new fd
%define SC_KILL 62      ; rdi = pid, rsi = signal

%define AF_INET 2       
%define SOCK_STREAM 1
%define FD_SOCKET 0

%define SIGTERM 15
%define STD_IN 0
%define STD_OUT 1
%define RQD_ARGS 3
%define NOT_ENOUGH_ARGS 1
%define CONNECTION_FAILED 3
%define SUCCESS 1
%define FAIL -1

;   sockaddr_in struct             
struc sockaddr_in
    .sin_family:    resw 1
    .sin_port:      resw 1
    .sin_addr:      resd 1
    .sin_pad:       resb 8
endstruc

section .data

bad_resolution: db  "unable to resolve host", 0xA, 0
len_br equ $-bad_resolution

cnkt_failed: db "connection attempt failed", 0xA, 0
len_cf equ $-cnkt_failed

assign3: db "./assign3", 0
len_a3 equ $-assign3

as3:    db "assign3",0

server: istruc sockaddr_in
     at   sockaddr_in.sin_family,    dw AF_INET
     at   sockaddr_in.sin_port,      dw 0
     at   sockaddr_in.sin_addr,      dd 0
iend


section .text

global _start

_start:

;   receive three command line arguments (program name, host to connect to, port number)
;       if not exit with status code (1)

    cmp     byte[rsp], RQD_ARGS     ; check for three arguments 
    jz      resolve
    mov     edi, NOT_ENOUGH_ARGS    ; set return value

done:
    mov     eax, SC_EXIT            ; exit
    syscall

;   resolve the host name of argv[1]to an IP address 
;       (use dns64.o: unsigned int resolv(const char *hostName))
;       if unsuccessful: resolv will return (-1)
;           print "unable to resolve host\n"
;           exit with code (2)

resolve:
    mov     rdi, [rsp + 0x10]       ; load argv[1] to rdi
    call    resolv                  ; call resolv
    mov     [server + sockaddr_in.sin_addr], eax
    cmp     rax, FAIL               ; check for resolution success
    jg      parse                   ; success move to prepare the port
    mov     rsi, bad_resolution     ; failure move failure message to be loaded
    mov     rdi, STD_OUT            ; where
    mov     rdx, len_br             ; how much
    mov     rax, SC_WRITE           ; write
    syscall                         ; execute
    jmp     done                    ; prepare to exit


;   parse the port number (perhaps l_atoi)
;   convert to network ordering (flip the two bytes)

parse:
    mov     rdi, [rsp + 0x18]   ; load argv[2] to ax
    call    l_atoi              
    xchg    ah, al              ; network order the bytes
    mov     [server + sockaddr_in.sin_port], ax

;   create a tcp socket with argv[1] on port argv[2]
;       if unsuccessful:
;           print "connection attempt failed\n"
;           close the socket
;           exit with code (3)                                                               

    xor     rax, rax            ; zeroize
    xor     rdx, rdx            ; stream defaults the protocol to TCP
    mov     rsi, SOCK_STREAM
    mov     rdi, AF_INET
    mov     eax, SC_SOCKET
    syscall
    mov     r15, rax            ; store the socket fd
    cmp     rax, FAIL
    jz      done


; connect(sockfd(rdi), sockaddr_struct *(rsi), 16)

connekt:
    xor     rax, rax
    mov     rdx, sockaddr_in_size
    mov     rsi, server
    mov     rdi, r15            ; stored socket fd
    mov     rax, SC_CONNECT
    syscall
    cmp     rax, FAIL
    jg      foork
    mov     rsi, cnkt_failed
    mov     edi, STD_OUT
    mov     rdx, len_cf
    mov     eax, SC_WRITE
    syscall
    mov     edi, CONNECTION_FAILED
    JMP     done                                         


foork:

; build a stack to call for assign3

    push    0
    push    as3                 ; filename
    push    0
    push    assign3             ; file path
    push    0
    lea     r11, [rsp+0x58]     ; envp
    push    r11
    mov     eax, SC_FORK
    syscall
    mov     r13, rax            ; save the child a pid
    cmp     rax, 0              
    jnz     parent

;   fork twice to create child A and child B (understand how to derive envp)
                 
;   child A:
;       duplicate the connected socket to stdin (fd 0)
;       close the socket (close)
;       execve assign3 (pass only argv[0] and a null pointer)
;           int execve(const char *imageName, char *const argv[rsp+8], char *const envp[rsp+40])

child_a:
    mov     rdi, r15            ; load the socket fd
    mov     rsi, STD_IN
    mov     eax, SC_DUP2
    syscall
    cmp     rax, FAIL 
    jz      done
    mov     rdi, r15            ; load the original socket fd
    mov     eax, SC_CLOSE
    syscall
    mov     rdi, [rsp+0x20]     ; pointer to assign3
    lea     rsi, [rsp+0x10]     ; pointer to argv[]
    lea     rdx, [rsp+0x58]     ; pointer to envp[]
    mov     eax, SC_EXECVE
    syscall
;    jmp     done               ; don't leave the child in an loop

;   child B:
;       duplicate the connected socket to stdout (fd 1)
;       close the socket (close)
;       execve assign3 (pass only argv[0] and a null pointer)

child_b:
    mov     rdi, r15            ; load the socket fd
    mov     rsi, STD_OUT
    mov     eax, SC_DUP2
    syscall            
    cmp     rax, FAIL
    jz      done
    mov     rdi, r15            ; load the old socket fd
    mov     eax, SC_CLOSE
    syscall
    mov     rdi, [rsp+0x20]     ; pointer to assign3 filename
    lea     rsi, [rsp+0x10]     ; pointer to argv[]
    lea     rdx, [rsp+0x58]     ; pointer to envp[]
    mov     eax, SC_EXECVE
    syscall
    jmp     done                ; don't leave the child in an loop
               

;   parent:
;       close the socket descriptor
;       wait for child A to complete (research wait4 systemcall)
;           send SIGTERM to child B (research kill systemcall)
;       wait for child B to complete (research wait4 systemcall)

parent:
    mov     eax, SC_FORK
    syscall
    cmp     rax, 0          ; check for child or parent
    jz      child_b
    mov     r14, rax        ; save child b pid
    mov     rdi, r15        ; load the socket fd
    mov     eax, SC_CLOSE
    syscall


; wait4
;     pid_t wait4(pid_t pid, int *wstatus, int options,
;                   struct rusage *rusage);
;   wait4(rdi, rsi(create an interger somewhere and have rsi point to it, we don't need it), 0)

    mov     rdi, r13        ; pid_t pid (child_a)
    mov     rsi, r12        ; int*wstatus
    mov     rdx, r12        ; int options
    mov     r10, r12        ; struct rusage *rusage
    mov     eax, SC_WAIT4
    syscall

; send SIGTERM to child_b

    mov     rdi, r14
    mov     rsi, SIGTERM
    mov     eax, SC_KILL
    syscall             

;   exit

    JMP     done
