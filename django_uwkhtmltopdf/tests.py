import unittest
import os
from utils import parse_options
from utils import render_to_tmp_file

class TestSequenceFunction(unittest.TestCase):
    def test_wrong_options(self):
        options = {'no_images': ''}
        self.assertEqual(parse_options(options, ''), ([], []))

    def test_no_parameter(self):
        options = {'no-images': ''}
        self.assertEqual(parse_options(options, ''), (['--no-images'], []))

    def test_one_parameter(self):
        options = {'minimum-font-size': 10}
        self.assertEqual(parse_options(options, ''), (['--minimum-font-size', 10], []))

    def test_two_parameters(self):
        options = {'cookie': ('name', 12)}
        self.assertEqual(parse_options(options, ''), (['--cookie', 'name', 12], []))

    def test_template_needed(self):
        files_to_remove = []
        context = {}
        options = {'header-html': 'header.html'}
        header_template = render_to_tmp_file(options['header-html'], context)
        files_to_remove.append(header_template)
        self.assertEqual(parse_options(options, context), (['--header-html', header_template], [header_template]))
        for f in files_to_remove:
            os.remove(f)

    def test_with_more_options(self):
        files_to_remove = []
        context = {}
        options = {'no-images': '', 'minimum-font-size': 10, 'header-html': 'header.html'}
        header_template = render_to_tmp_file(options['header-html'], context)
        files_to_remove.append(header_template)
        self.assertEqual(parse_options(options, context), (['--no-images', '--header-html', header_template, '--minimum-font-size', 10], [header_template]))
        for f in files_to_remove:
            os.remove(f)
 
if __name__=='__main__':
    unittest.main()
