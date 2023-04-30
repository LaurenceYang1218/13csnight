PYTHON = python3

all: 
	$(PYTHON) app.py 
	
clean:
	rm data.csv
	touch data.csv