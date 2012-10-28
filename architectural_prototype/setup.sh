#!/bin/bash
virtualenv venv --distribute
source venv/bin/activate
pip install Flask boto pycrypto

