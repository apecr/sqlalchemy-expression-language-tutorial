#!/bin/sh

coverage run --source . -m pytest && coverage report --omit=tests/*.py && coverage xml -o coverage-reports/coverage.xml