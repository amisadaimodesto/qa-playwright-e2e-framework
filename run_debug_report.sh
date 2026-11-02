#!/bin/bash
PWDEBUG=1 pytest -s --tracing=on --alluredir=reports/allure-results
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
