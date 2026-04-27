SRC = src

NAME = $(SRC)/a_maze_ing.py
CONFIG = config.txt

VENV = .venv

run: install
	uv run $(NAME) $(CONFIG)

install: $(VENV)

# create a virtual enviroment in inside existing folder
$(VENV): pyproject.toml uv.lock	
	pipx install uv
	uv venv --python 3.10
	uv sync

debug:
	uv run python -m pdb $(NAME) $(CONFIG)

clean:
	rm -rf $(VENV) */__pycache__ .mypy_cache .pytest_cache

lint:
	uvx flake8 $(SRC)
	uvx mypy $(SRC)

lint-strict:
	uvx flake8 $(SRC)
	uvx mypy --strict $(SRC)

test:
	uvx pytest 

.PHONY: run install debug clean lint lint-strict test