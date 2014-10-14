

.PHONY: nvim_funcs.py
nvim_funcs.py:
	./apigen.py > $@

run: nvim_funcs.py
	./main.py

rundbg: nvim_funcs.py
	./main.py -d
