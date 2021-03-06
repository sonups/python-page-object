![Screenshot](icon.png)



# Python page object model 

> Automated tests are demonstrated on 
> https://www.xeneta.com/demo 
> https://www.xeneta.com/careers
## Tools

- python 3.6, 3.7, 3.8, 3.9
- [pytest](https://pypi.org/project/pytest/) framework
- [selenium](https://selenium.dev/) library
- [allure](https://docs.qameta.io/allure/) reporting
- [docker] (https://docker.io/) headless automation
- [jenkins](https://www.jenkins.io/) continous testing

## Quick start
From the root directory of your shell follow the below steps:

1. Clone the repository `https://github.com/sonups/python-page-object`
2. `pip install -r requirements.txt` to install all project dependenciesc
3. In Linux run below bash script to change permission of webdriver executable
>	`sh linux_setup.sh`
4. to run tests
>  	`pytest -m smoke`

## To run tests without requiring any setup, please use jenkins hosted in azure vm
Open the url http://40.80.88.6/

1. Run the job Spin-Up-Browsers-in-Docker-for-selenium-Tests to spin up headless browser instances
2. Run the job Xeneta-Run-UI-Selenium-Test to run the tests
3. Navigate to the Allure report section in under the UI test job to view the test results




## Allure report

![Screenshot](demoauto/image/allure.png)

## Local report in test-report.html

Open `test-report.html` file to see detailed testing report e.g:

![Screenshot](demoauto/image/report.png)

## Link to overview PPT document

> https://github.com/sonups/python-page-object/blob/master/xeneta-ppt.pptx

## Other repositories
python-selenium-hub-docker-dev 
> https://github.com/sonups/python-selenium-hub-docker-dev

xeneta-jenkins
> https://github.com/sonups/xeneta-jenkins

### Meta
Author – Sonu Sadasivan.


You can reach out me at:
* [sonu.sadasivan@gmail.com](sonu.sadasivan@gmail.com)
* [https://github.com/sonups](https://github.com/sonups)
* [https://www.linkedin.com/in/spnups](https://www.linkedin.com/in/sonups)




