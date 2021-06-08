targets/docker-image:  Dockerfile requirements.txt
	docker build -t type_hinting . > targets/docker-image

targets/mypy:  targets/docker-image type_hinting/.* mypy.ini
	docker run --rm  -v "$(shell pwd)/type_hinting:/type_hinting" -v "$(shell pwd)/mypy.ini:/mypy.ini" type_hinting python3 -m mypy --config-file mypy.ini -p type_hinting > targets/mypy

type-check: targets/mypy
	cat targets/mypy