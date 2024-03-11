## About this repository
This repository contains a test framework based on Page Object Model for website testing using python and selenium. It automates the search queries on google and runs the following tests:
- <b>test 1</b>: there are nonzero results on typed search query.
- <b>test 2</b>: the topmost link that matches the search query should contain atleast 5 instances of the searched keyword on its homepage.


The results are automated and they look like shown below
<video width = "1920" height="1080" controls src="recording.mp4" title="Title"></video>

## How to run
To run, type one of the following in the commnad line/terminal:
1. <code>pytest</code> : run the tests without generating reports on Microsoft Edge browser.
2. <code>pytest --browser=firefox</code> : run the tests without generating report, but on Firefox browser. `--browser=chrome` would run it on Google Chrome. In any other case, it runs on Microsoft Edge.
3. <code>pytest --browser=chrome --html=reports/report.html</code> : run the tests on chrome browser, with reports which are stored in `reports/report.html`.

## Dependencies
The code has been tested on python 3.11 with the following packages
<pre>
attrs             23.2.0
certifi           2024.2.2
cffi              1.16.0
colorama          0.4.6
ddt               1.7.2
et-xmlfile        1.1.0
h11               0.14.0
idna              3.6
iniconfig         2.0.0
Jinja2            3.1.3
MarkupSafe        2.1.5
openpyxl          3.1.2
outcome           1.3.0.post0
packaging         24.0
pip               24.0
pluggy            1.4.0
pycparser         2.21
PySocks           1.7.1
pytest            8.1.1
pytest-html       4.1.1
pytest-metadata   3.1.1
selenium          4.18.1
setuptools        65.5.0
sniffio           1.3.1
sortedcontainers  2.4.0
trio              0.24.0
trio-websocket    0.11.1
typing_extensions 4.10.0
urllib3           2.2.1
wsproto           1.2.0
</pre>

The `requirements.txt` file is also included.