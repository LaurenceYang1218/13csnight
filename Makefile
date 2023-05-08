PYTHON3 = python

all: 
	$(PYTHON3) app.py 
py: 
	python app.py
sort:
	$(PYTHON3) sort.py
	cat sort.csv
clean:
	rm data.csv sort.csv
	touch data.csv sort.csv