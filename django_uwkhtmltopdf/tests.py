import unittest
import os
from utils import parse_options
from utils import render_to_tmp_file

contest = {}
files_to_remove = []

class TestSequenceFunction(unittest.TestCase):
    def test_no_parameter1(self):
        options = {'no_images': ''}
        self.assertEqual(parse_options(options, contest), ([], []))

    def test_no_parameter2(self):
        options = {'no-images': ''}
        self.assertEqual(parse_options(options, contest), (['--no-images'], []))

    def test_one_parameter(self):
        options = {'minimum-font-size': 10}
        self.assertEqual(parse_options(options, contest), (['--minimum-font-size', 10], []))

    def test_two_parameters(self):
        options = {'cookie': ('name', 12)}
        self.assertEqual(parse_options(options, contest), (['--cookie', 'name', 12], []))

    def test_template_needed(self):
        options = {'header-html': 'header.html'}
        header_template = render_to_tmp_file(options['header-html'], contest)
        files_to_remove.append(header_template)
        self.assertEqual(parse_options(options, contest), (['--header-html', header_template], [header_template]))

    def test_with_more_options(self):
        options = {'no-images': '', 'minimum-font-size': 10, 'header-html': 'header.html'}
        header_template = render_to_tmp_file(options['header-html'], contest)
        files_to_remove.append(header_template)
        self.assertEqual(parse_options(options, contest), (['--no-images', '--header-html', header_template, '--minimum-font-size', 10], [header_template]))

for f in files_to_remove:
    os.remove(f)
 
if __name__=='__main__':
    unittest.main()
