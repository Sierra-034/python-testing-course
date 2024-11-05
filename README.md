- First you need to install this package locally: `pip install -e .`
- To run unittest tests, you need: `python -m unittest discover -s test_unittest`
- To run pytest tests, you first need pytest installed: `pip install pytest`, then: `pytest test_pytest`

- You can also run individual or set of test: `pytest test_pytest/test_main.py::TestExample::test_suma_dos_numeros`
- To see standard output you'll need to set `-s`: `pytest -s <path_to_test>`
- To run test marked you need to mark them previous to execute with decorator: `@pytest.mark.<mark_name>`
- Run marked tests: `pytest -m <mark_name>`

- To use coverage tools, you need to install it first: `pip install coverage`
- Then you need to run your test: `coverage run -m pytest <path_to_test>`
- Or you can use unittest: `coverage run -m unittest <arguments/options>`
- First we need to run tests through coverage, then generate report: `coverage report`
- Now we can generate a html coverage report: `coverage html`

- You can start a http server: `python -m http.server`
