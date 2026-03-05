PYTHON ?= python3

.PHONY: build verify serve clean

build:
	$(PYTHON) scripts/build_site.py

verify:
	$(PYTHON) scripts/verify_consistency.py

serve:
	cd public && $(PYTHON) -m http.server 8787

clean:
	rm -rf public
