This represents the first significant project in my github with hopefully more to come.

This is an autograder for homeworks which is specifically designed for the CS-UY 1113 intro to programming course at NYU

It utilizes the following libraries in order to test student code, and exports a spread sheet for easy viewing containing the student names, as well as
the results of any given test.

It utilizes the following python libraries:

import os
import subprocess
import unittest
import sys
from unittest.mock import patch
from io import StringIO
import pandas as pd
import importlib.util


Remaining Work:
Further testing for students submitting work. 
