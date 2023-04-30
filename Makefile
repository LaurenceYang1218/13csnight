PYTHON = python3

all: 
	$(PYTHON) app.py 
sort:
	$(PYTHON) sort.py
	cat sort.csv
clean:
	rm data.csv sort.csv
	touch data.csv sort.csv
