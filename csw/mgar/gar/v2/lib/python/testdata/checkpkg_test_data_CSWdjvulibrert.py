# $Id$
pkg_data = {
 'all_filenames': ['license',
                   'libdjvulibre.so.15',
                   'libdjvulibre.so.21.1.0',
                   'libdjvulibre.so.21.1.0'],
 'basic_stats': {'catalogname': 'djvulibre_rt',
                 'parsed_basename': {'arch': 'sparc',
                                     'catalogname': 'djvulibre_rt',
                                     'full_version_string': '3.5.22,REV=2010.03.17',
                                     'osrel': 'SunOS5.8',
                                     'revision_info': {'REV': '2010.03.17'},
                                     'vendortag': 'CSW',
                                     'version': '3.5.22',
                                     'version_info': {'major version': '3',
                                                      'minor version': '5',
                                                      'patchlevel': '22'}},
                 'pkg_basename': 'djvulibre_rt-3.5.22,REV=2010.03.17-SunOS5.8-sparc-CSW.pkg.gz',
                 'pkg_path': '/tmp/pkg_60J_Gm/djvulibre_rt-3.5.22,REV=2010.03.17-SunOS5.8-sparc-CSW.pkg.gz',
                 'pkgname': 'CSWdjvulibrert',
                 'stats_version': 2L},
 'binaries': ['opt/csw/lib/libdjvulibre.so.15',
              'opt/csw/lib/sparcv9/libdjvulibre.so.21.1.0',
              'opt/csw/lib/libdjvulibre.so.21.1.0'],
 'binaries_dump_info': [{'base_name': 'libdjvulibre.so.15',
                         'needed sonames': ['libjpeg.so.62',
                                            'libpthread.so.1',
                                            'libiconv.so.2',
                                            'libm.so.1',
                                            'libCstd.so.1',
                                            'libCrun.so.1',
                                            'libc.so.1'],
                         'path': 'opt/csw/lib/libdjvulibre.so.15',
                         'runpath': ('/opt/csw/lib/$ISALIST',
                                     '/opt/csw/lib',
                                     '/opt/SUNWspro/lib/rw7',
                                     '/opt/SUNWspro/lib/v8',
                                     '/opt/SUNWspro/lib',
                                     '/usr/ccs/lib',
                                     '/lib',
                                     '/usr/lib',
                                     '/usr/lib/$ISALIST',
                                     '/usr/lib',
                                     '/lib/$ISALIST',
                                     '/lib'),
                         'soname': 'libdjvulibre.so.15',
                         'soname_guessed': False},
                        {'base_name': 'libdjvulibre.so.21.1.0',
                         'needed sonames': ['libjpeg.so.7',
                                            'libpthread.so.1',
                                            'libm.so.1',
                                            'libCstd.so.1',
                                            'libCrun.so.1',
                                            'libc.so.1'],
                         'path': 'opt/csw/lib/sparcv9/libdjvulibre.so.21.1.0',
                         'runpath': ('/opt/csw/X11/lib/$ISALIST',
                                     '/opt/csw/X11/lib/64',
                                     '/opt/csw/lib/$ISALIST',
                                     '/opt/csw/lib/64',
                                     '/opt/studio/SOS11/SUNWspro/lib/rw7/v9',
                                     '/opt/studio/SOS11/SUNWspro/lib/v9',
                                     '/opt/SUNWspro/lib/v9',
                                     '/usr/ccs/lib/sparcv9',
                                     '/lib/sparcv9',
                                     '/usr/lib/sparcv9',
                                     '/usr/lib/$ISALIST',
                                     '/usr/lib',
                                     '/lib/$ISALIST',
                                     '/lib'),
                         'soname': 'libdjvulibre.so.21',
                         'soname_guessed': False},
                        {'base_name': 'libdjvulibre.so.21.1.0',
                         'needed sonames': ['libjpeg.so.7',
                                            'libpthread.so.1',
                                            'libm.so.1',
                                            'libCstd.so.1',
                                            'libCrun.so.1',
                                            'libc.so.1'],
                         'path': 'opt/csw/lib/libdjvulibre.so.21.1.0',
                         'runpath': ('/opt/csw/X11/lib/$ISALIST',
                                     '/opt/csw/X11/lib',
                                     '/opt/csw/lib/$ISALIST',
                                     '/opt/csw/lib',
                                     '/opt/studio/SOS11/SUNWspro/lib/rw7',
                                     '/opt/studio/SOS11/SUNWspro/lib/v8',
                                     '/opt/studio/SOS11/SUNWspro/lib',
                                     '/opt/SUNWspro/lib/v8',
                                     '/opt/SUNWspro/lib',
                                     '/usr/ccs/lib',
                                     '/lib',
                                     '/usr/lib',
                                     '/usr/lib/$ISALIST',
                                     '/usr/lib',
                                     '/lib/$ISALIST',
                                     '/lib'),
                         'soname': 'libdjvulibre.so.21',
                         'soname_guessed': False}],
 'depends': [('CSWcommon',
              'CSWcommon common - common files and dirs for CSW packages '),
             ('CSWisaexec',
              'CSWisaexec isaexec - sneaky wrapper around Sun isaexec '),
             ('CSWjpeg',
              'CSWjpeg jpeg - JPEG library and tools by the Independent JPEG Group ')],
 'isalist': ('sparcv9+vis2',
             'sparcv9+vis',
             'sparcv9',
             'sparcv8plus+vis2',
             'sparcv8plus+vis',
             'sparcv8plus',
             'sparcv8',
             'sparcv8-fsmuld',
             'sparcv7',
             'sparc'),
 'binaries_elf_info': {
     'opt/csw/lib/libdjvulibre.so.15': {
       'version definition': [],
       'version needed': [],
       'symbol table': [
         { 'soname': 'libjpeg.so.62', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libpthread.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libiconv.so.2', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libm.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libCstd.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libCrun.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libc.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         ],
       },
     'opt/csw/lib/sparcv9/libdjvulibre.so.21.1.0': {
       'version definition': [],
       'version needed': [],
       'symbol table': [
         { 'soname': 'libjpeg.so.7', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libpthread.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libm.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libCstd.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libCrun.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libc.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         ],
       },
     'opt/csw/lib/libdjvulibre.so.21.1.0': {
       'version definition': [],
       'version needed': [],
       'symbol table': [
         { 'soname': 'libjpeg.so.7', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libpthread.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libm.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libCstd.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libCrun.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         { 'soname': 'libc.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
         ],
       },
     },
 'overrides': [],
 'pkginfo': {'ARCH': 'sparc',
             'CATEGORY': 'application',
             'CLASSES': 'none',
             'EMAIL': 'hson@opencsw.org',
             'HOTLINE': 'http://www.opencsw.org/bugtrack/',
             'NAME': 'djvulibre_rt - DjVu standalone viewer, browser plug-in, command line tools - runtime package',
             'OPENCSW_CATALOGNAME': 'djvulibre_rt',
             'OPENCSW_MODE64': '32/64/isaexec',
             'OPENCSW_REPOSITORY': 'https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/pkg/djvulibre/trunk@9213',
             'PKG': 'CSWdjvulibrert',
             'PSTAMP': 'hson@build8s-20100317033724',
             'VENDOR': 'http://djvu.sourceforge.net/ packaged for CSW by Roger Hakansson',
             'VERSION': '3.5.22,REV=2010.03.17',
             'WORKDIR_FIRSTMOD': '../build-isa-sparcv8'},
 'pkgmap': [{'class': None,
             'group': None,
             'line': ': 1 15667',
             'mode': None,
             'path': None,
             'type': '1',
             'user': None},
            {'class': 'none',
             'group': None,
             'line': '1 s none /opt/csw/lib/libdjvulibre.so=libdjvulibre.so.21.1.0',
             'mode': None,
             'path': '/opt/csw/lib/libdjvulibre.so',
             'type': 's',
             'user': None},
            {'class': 'none',
             'group': 'bin',
             'line': '1 f none /opt/csw/lib/libdjvulibre.so.15 0755 root bin 2179976 17791 1268791023',
             'mode': '0755',
             'path': '/opt/csw/lib/libdjvulibre.so.15',
             'type': 'f',
             'user': 'root'},
            {'class': 'none',
             'group': None,
             'line': '1 s none /opt/csw/lib/libdjvulibre.so.21=libdjvulibre.so.21.1.0',
             'mode': None,
             'path': '/opt/csw/lib/libdjvulibre.so.21',
             'type': 's',
             'user': None},
            {'class': 'none',
             'group': 'bin',
             'line': '1 f none /opt/csw/lib/libdjvulibre.so.21.1.0 0755 root bin 2316572 5640 1268790998',
             'mode': '0755',
             'path': '/opt/csw/lib/libdjvulibre.so.21.1.0',
             'type': 'f',
             'user': 'root'},
            {'class': 'none',
             'group': None,
             'line': '1 s none /opt/csw/lib/sparcv9/libdjvulibre.so=libdjvulibre.so.21.1.0',
             'mode': None,
             'path': '/opt/csw/lib/sparcv9/libdjvulibre.so',
             'type': 's',
             'user': None},
            {'class': 'none',
             'group': None,
             'line': '1 s none /opt/csw/lib/sparcv9/libdjvulibre.so.21=libdjvulibre.so.21.1.0',
             'mode': None,
             'path': '/opt/csw/lib/sparcv9/libdjvulibre.so.21',
             'type': 's',
             'user': None},
            {'class': 'none',
             'group': 'bin',
             'line': '1 f none /opt/csw/lib/sparcv9/libdjvulibre.so.21.1.0 0755 root bin 2950128 36235 1268791033',
             'mode': '0755',
             'path': '/opt/csw/lib/sparcv9/libdjvulibre.so.21.1.0',
             'type': 'f',
             'user': 'root'},
            {'class': 'none',
             'group': 'bin',
             'line': '1 d none /opt/csw/share/doc/djvulibre_rt 0755 root bin',
             'mode': '0755',
             'path': '/opt/csw/share/doc/djvulibre_rt',
             'type': 'd',
             'user': 'root'},
            {'class': 'none',
             'group': 'bin',
             'line': '1 f none /opt/csw/share/doc/djvulibre_rt/license 0644 root bin 17989 29204 1268793418',
             'mode': '0644',
             'path': '/opt/csw/share/doc/djvulibre_rt/license',
             'type': 'f',
             'user': 'root'},
            {'class': None,
             'group': None,
             'line': '1 i copyright 76 7217 1268793418',
             'mode': None,
             'path': None,
             'type': 'i',
             'user': None},
            {'class': None,
             'group': None,
             'line': '1 i depend 187 16539 1268793444',
             'mode': None,
             'path': None,
             'type': 'i',
             'user': None},
            {'class': None,
             'group': None,
             'line': '1 i pkginfo 560 47879 1268793447',
             'mode': None,
             'path': None,
             'type': 'i',
             'user': None}]}
