PYTHON3 = python3

all: 
	$(PYTHON3) app.py 
py: 
	python app.py
sort:
	$(PYTHON3) sort.py
	cat sort.csv
clean:
	rm data.csv
	touch data.csv