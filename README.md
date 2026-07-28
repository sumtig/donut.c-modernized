# donut.c modernized
the infamous donut.c program, modernized to work with modern gcc.

# how to compile for the noobies
**arch:**
`gcc donut.c -o donut -lm`

**windows:**
if you are using MSYS2 MinGW: `gcc donut.c -o donut.exe -lm`

**macOS:**
if you have Xcode commandline tools: `clang donut.c -o donut -lm`
or you can also use `gcc donut.c -o donut -lm`

you might notice the command being exactly the same most of the time.
the old donut.c (`donut.c.old`) has a very low chance you can compile it with modern tools. have fun!
