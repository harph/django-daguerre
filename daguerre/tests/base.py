import ImageChops
import os

import daguerre


class DaguerreTestCaseMixin(object):
	def get_test_file(self, test_path):
		"""Given a path relative to daguerre/tests/data/, returns an open file."""
		return open(self.get_test_file_path(test_path))

	def get_test_file_path(self, test_path):
		"""Given a path relative to daguerre/tests/data/, returns an absolute path."""
		return os.path.abspath(os.path.join(os.path.dirname(daguerre.__file__), 'tests', 'data', test_path))

	def assertImageEqual(self, im1, im2):
		# Image comparisons according to http://effbot.org/zone/pil-comparing-images.htm
		self.assertTrue(ImageChops.difference(im1, im2).getbbox() is None)