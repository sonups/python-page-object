![Screenshot](icon.png)



# Python page object model (PyPOM)
> Represent most popular OOD pattern for Web UI automation using python programming language ).
>
> Automated tests are demonstrated on http://newtours.demoaut.com/mercurywelcome.php web application. 

## Tools

### Production
- python 3.6, 3.7, 3.8, 3.9
- [pytest](https://pypi.org/project/pytest/) framework
- [selenium](https://selenium.dev/) library
- [allure](https://docs.qameta.io/allure/) reporting


> In addition a source code is **fully** [type annotated](https://docs.python.org/3/library/typing.html) ⭐

## Quick start
From the root directory of your shell run following command:

```bash
./run-tests.sh help

Tool allows to simplify run of automated tests for POM sample project.

Available actions:
 - smoke                 run automated smoke tests
 - unittest              run automated unittest tests
 - all                   run all automated tests
 - help                  display help

Note:            help will be provided in case of no input parameters
```

### Tests (html) report sample
Run a bunch of tests (e.g smoke) via following command:
```bash
./run-tests.sh smoke
```

Then please open `test-report.html` file to see detailed testing report e.g:

![Screenshot](demoauto/image/report.png)

### Generate allure report
Please follow next instruction to generate allure report (mac OS example):
1. Update java via `brew cask install adoptopenjdk`
2. Install allure via `brew install allure`
3. Generate allure project via `allure serve report`

![Screenshot](demoauto/image/allure.png)

## Development notes

### Release History

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta
Author – Sonu Sadasivan.


You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)


1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependenciesc
4. In Linux run below bash script to change permission of webdriver executable
	`sh linux_setup.sh`


