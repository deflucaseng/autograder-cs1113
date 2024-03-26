import os
import subprocess
import unittest
import sys
from unittest.mock import patch
from io import StringIO
import pandas as pd
import importlib.util

#Step 1 getting the information about the homework in terms of its size so it can be more easily
# navigated


class run_tests:

	def __init__(self):
		homework_num = input("Enter the homework number: ")
		problem_questions = input("Enter the names of the problems separated by a space (1 2a 2b 3 4 etc...): ")
		self.problem_list = problem_questions.split()

		#Step 2 create a dictionary containing information about each student which will be loaded. 
		with open('studentnames.txt', 'r') as file:
			lines = file.readlines()
			count_students = sum(1 for line in lines if line.strip())
			for question in self.problem_list:
				self.questions_dict["hw"+str(homework_num)+"_q"+question] = [""] * count_students
			self.df = pd.DataFrame(self.questions_dict, index = lines)


	def import_from_file(file_path):
		spec = importlib.util.spec_from_file_location("module.name", file_path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		return module

	def run_test(self, submission_path, test_path):
		    # Import the student's submission
		submission_module = self.import_from_file(submission_path)
		
		# Import the test module
		test_module = self.import_from_file(test_path)

		# Create a test suite and add the test cases from the test module
		suite = unittest.TestLoader().loadTestsFromModule(test_module)
		
		# Run the tests
		runner = unittest.TextTestRunner(verbosity=2)
		result = runner.run(suite)
		
		return result.wasSuccessful()

		


	def generate_results(self):
		directory_name = input("Enter the directory name: ")
		for dirpath, dirnames, filenames in os.walk(directory_name):
			for filename in filenames:
				if filename.endswith('.py'):
					question_num = filename.split('_')[1][1:len(filename) - 3]
					with open(filename, 'r') as file:
						lines = file.readlines()
						author = lines[0].split()[-1:-3]
					submission_filepath = os.path.join(dirpath, filename)
					test_filepath = os.path.join("test_cases", filename)
					success = self.run_test(submission_filepath, test_filepath)
					if success:
						self.df.at[author, "hw1_q"+question_num] = "Correct"
					else:
						self.df.at[author, "hw1_q"+question_num] = "Incorrect"





	
	def write_results(self):
		self.df.to_csv('output.csv', index=False)



def main():
	homework_autograder = run_tests()
	homework_autograder.generate_results()
	homework_autograder.write_results()


if __name__ == '__main__':
	main()
