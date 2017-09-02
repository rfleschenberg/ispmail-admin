#! /bin/bash
set -xe

coverage run -m py.test "$@" && coverage report -m
