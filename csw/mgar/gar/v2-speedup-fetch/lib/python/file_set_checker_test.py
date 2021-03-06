#!/usr/bin/env python2.6
# coding=utf-8
# vim:set sw=2 ts=2 sts=2 expandtab:

# Try to use unittest2, fall back to unittest
try:
  import unittest2 as unittest
except ImportError:
  import unittest

import file_set_checker
import tag

SAMPLE_FILES = [
  # This file intentionally missing.
  # '/home/experimental/maciej/libnspr4-4.8.6,REV=2010.10.16-SunOS5.9-i386-CSW.pkg.gz',
  '/home/experimental/maciej/libnspr4-4.8.6,REV=2010.10.16-SunOS5.9-sparc-CSW.pkg.gz',
  '/home/experimental/maciej/libnspr4_devel-4.8.6,REV=2010.10.16-SunOS5.9-i386-CSW.pkg.gz',
  '/home/experimental/maciej/libnspr4_devel-4.8.6,REV=2010.10.16-SunOS5.9-sparc-CSW.pkg.gz',
  '/home/experimental/maciej/nspr-4.8.6,REV=2010.10.16-SunOS5.9-all-CSW.pkg.gz',
  '/home/experimental/maciej/nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-i386-CSW.pkg.gz',
  '/home/experimental/maciej/nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-sparc-CSW.pkg.gz',
]

class FileSetCheckerUnitTest(unittest.TestCase):

  def testMissingArchitecture(self):
    fc = file_set_checker.FileSetChecker()
    expected = [tag.CheckpkgTag(None, 'i386-SunOS5.9-missing', 'libnspr4')]
    self.assertEqual(expected, fc.CheckFiles(SAMPLE_FILES))

  def testMissingArchitectureWithOsrel(self):
    files = [
        'foo-1.0,REV=2011.03.30-SunOS5.9-i386-CSW.pkg.gz',
        'foo-1.0,REV=2011.03.30-SunOS5.9-sparc-CSW.pkg.gz',
        'foo-1.0,REV=2011.03.30-SunOS5.10-i386-CSW.pkg.gz',
        # Intentionally missing
        # 'foo-1.0,REV=2011.03.30-SunOS5.10-sparc-CSW.pkg.gz',
    ]
    fc = file_set_checker.FileSetChecker()
    expected = [tag.CheckpkgTag(None, 'sparc-SunOS5.10-missing', 'foo')]
    self.assertEqual(expected, fc.CheckFiles(files))

  def testUncommitted(self):
    fc = file_set_checker.FileSetChecker()
    expected = [
        tag.CheckpkgTag(
          None, 'bad-vendor-tag',
          'filename=nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-sparc-UNCOMMITTED.pkg.gz expected=CSW actual=UNCOMMITTED'),
        tag.CheckpkgTag(
          None, 'bad-vendor-tag',
          'filename=nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-i386-UNCOMMITTED.pkg.gz expected=CSW actual=UNCOMMITTED'),
    ]
    files = ['/home/experimental/maciej/'
             'nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-sparc-UNCOMMITTED.pkg.gz',
             '/home/experimental/maciej/'
             'nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-i386-UNCOMMITTED.pkg.gz']
    self.assertEqual(expected, fc.CheckFiles(files))

  def testBadInput(self):
    fc = file_set_checker.FileSetChecker()
    expected = [
        tag.CheckpkgTag(None, 'bad-arch-or-os-release', 'csw-upload-pkg arch=pkg osrel=unspecified'),
        tag.CheckpkgTag(None, 'bad-vendor-tag', 'filename=csw-upload-pkg expected=CSW actual=UNKN'),
    ]
    files = ['csw-upload-pkg']
    self.assertEqual(expected, fc.CheckFiles(files))


if __name__ == '__main__':
	unittest.main()
