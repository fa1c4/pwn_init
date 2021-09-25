from pwn import *

url, port = "", 
filename = ""
elf = ELF(filename)
libc = ELF("")
context(arch="amd64", os="linux")
# context(arch="i386", os="linux")

local = 1
if local:
    context.log_level = "debug"
    io = process(filename)
    # context.terminal = ['tmux', 'splitw', '-h']
    # gdb.attach(io)
else:
    io = remote(url, port)

def B():
    gdb.attach(io)
    pause()




def pwn():



if __name__ == "__main__":
    pwn()
    io.interactive()