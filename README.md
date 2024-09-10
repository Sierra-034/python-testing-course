- First you need to install this package locally: `pip install -e .`
- To run unittest tests, you need: `python -m unittest discover -s test_unittest`
- To run pytest tests, you first need pytest installed: `pip install pytest`, then: `pytest test_pytest`

- You can also run individual or set of test: `pytest test_pytest/test_main.py::TestExample::test_suma_dos_numeros`
- To see standard output you'll need to set `-s`: `pytest -s <path_to_test>`
