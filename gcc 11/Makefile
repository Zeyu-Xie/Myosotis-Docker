.PHONY: ALL main clean clean_win

ALL: main

main: main.cpp
	g++ main.cpp -o main --std=c++11

clean:
	rm -f main main.exe

# clean command for windows powershell
clean_win:
	del main main.exe