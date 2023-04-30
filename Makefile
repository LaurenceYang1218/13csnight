PYTHON3 = python3

all: 
	$(PYTHON3) app.py 
sort:
	$(PYTHON3) sort.py
	cat sort.csv
clean:
	rm data.csv sort.csv
	touch data.csv sort.csv
