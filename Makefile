image:
	docker build -t type_hinting .

type-check:
	docker run --rm  -v "$(shell pwd)/type_hinting:/type_hinting" -v "$(shell pwd)/mypy.ini:/mypy.ini" type_hinting python3 -m mypy --config-file mypy.ini -p type_hinting