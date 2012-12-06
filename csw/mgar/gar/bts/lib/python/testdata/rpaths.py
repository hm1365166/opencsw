all_rpaths = set([
     '$ORIGIN',
     '$ORIGIN/..',
     '$ORIGIN/../../../usr/lib/v9',
     '$ORIGIN/../../usr/lib',
     '$ORIGIN/../lib',
     '$ORIGIN/../ure-link/lib',
     '../../../../../dist/bin',
     '../../../../dist/bin',
     '../../../dist/bin',
     '../../dist/bin',
     '/bin',
     '/export/home/buysse/build/expect-5.42.1/cswstage/opt/csw/lib',
     '/export/home/phil/build/gettext-0.14.1/gettext-tools/intl/.libs',
     '/export/medusa/kenmays/build/qt-x11-free-3.3.3/lib',
     '/export/medusa/kenmays/build/s_qt/qt-x11-free-3.3.3/lib',
     '/export/medusa/kenmays/build/sparc_qt/qt-x11-free-3.3.4/lib',
     '/export/medusa/kenmays/build/sparc_qt/qt-x11-free-3.3.4/plugins/designer',
     '/export/medusa/kenmays/build/sparc_qt/qt-x11-free-3.3.4/plugins/sqldrivers',
     '/home/harpchad/local/sparc/lib',
     '/lib',
     '/lib/sparcv9',
     '/opt/SUNWcluster/lib',
     '/opt/SUNWmlib/lib',
     '/opt/SUNWspro/lib',
     '/opt/SUNWspro/lib/rw7',
     '/opt/SUNWspro/lib/stlport4',
     '/opt/SUNWspro/lib/v8',
     '/opt/SUNWspro/lib/v8plus',
     '/opt/SUNWspro/lib/v8plusa',
     '/opt/SUNWspro/lib/v8plusb',
     '/opt/SUNWspro/lib/v9',
     '/opt/build/michael/synce-0.8.9-buildroot/opt/csw/lib',
     '/opt/csw/$ISALIST',
     '/opt/csw//lib',
     '/opt/csw/X11/lib',
     '/opt/csw/X11/lib/',
     '/opt/csw/X11/lib/$ISALIST',
     '/opt/csw/X11/lib/64',
     '/opt/csw/apache2/lib',
     '/opt/csw/apache2/lib/$ISALIST',
     '/opt/csw/bdb33/lib',
     '/opt/csw/bdb33/lib/$ISALIST',
     '/opt/csw/bdb4/lib',
     '/opt/csw/bdb4/lib/',
     '/opt/csw/bdb4/lib/$ISALIST',
     '/opt/csw/bdb42/lib',
     '/opt/csw/bdb42/lib/$ISALIST',
     '/opt/csw/bdb42/lib/64',
     '/opt/csw/bdb43/lib',
     '/opt/csw/bdb43/lib/$ISALIST',
     '/opt/csw/bdb43/lib/64',
     '/opt/csw/bdb44/lib',
     '/opt/csw/bdb44/lib/$ISALIST',
     '/opt/csw/bdb44/lib/64',
     '/opt/csw/bdb47/lib',
     '/opt/csw/bdb47/lib/$ISALIST',
     '/opt/csw/bdb47/lib/64',
     '/opt/csw/bdb48/lib',
     '/opt/csw/bdb48/lib/$ISALIST',
     '/opt/csw/bdb48/lib/64',
     '/opt/csw/gcc3/lib',
     '/opt/csw/gcc3/lib/$ISALIST',
     '/opt/csw/gcc3/lib/.',
     '/opt/csw/gcc3/lib/sparcv9',
     '/opt/csw/gcc4/lib',
     '/opt/csw/gcc4/lib/$ISALIST',
     '/opt/csw/gcc4/lib/64',
     '/opt/csw/gcc4/lib/gcj-4.3.3-9',
     '/opt/csw/gcc4/lib/sparcv9',
     '/opt/csw/kde-gcc/lib',
     '/opt/csw/kde-gcc/lib/kde3',
     '/opt/csw/kde/lib',
     '/opt/csw/lib',
     '/opt/csw/lib/',
     '/opt/csw/lib/$',
     '/opt/csw/lib/$$ISALIST',
     '/opt/csw/lib/$ISALIST',
     '/opt/csw/lib/$ISALIST/ogle',
     '/opt/csw/lib/-R/opt/csw/lib',
     '/opt/csw/lib/.',
     '/opt/csw/lib/32',
     '/opt/csw/lib/64',
     '/opt/csw/lib/SALIST',
     '/opt/csw/lib/X11',
     '/opt/csw/lib/\\$ISALIST',
     '/opt/csw/lib/\\SALIST',
     '/opt/csw/lib/amanda',
     '/opt/csw/lib/courier-authlib',
     '/opt/csw/lib/dia',
     '/opt/csw/lib/evolution/1.4',
     '/opt/csw/lib/evolution/2.2',
     '/opt/csw/lib/evolution/2.6',
     '/opt/csw/lib/evolution/2.8',
     '/opt/csw/lib/evolution/2.8/components',
     '/opt/csw/lib/evolution/nss/lib',
     '/opt/csw/lib/gnopernicus-1.0',
     '/opt/csw/lib/gnucash',
     '/opt/csw/lib/graphviz',
     '/opt/csw/lib/htdig',
     '/opt/csw/lib/htdig_db',
     '/opt/csw/lib/lib',
     '/opt/csw/lib/libsunmath.so',
     '/opt/csw/lib/mozilla',
     '/opt/csw/lib/mysql',
     '/opt/csw/lib/octave-3.0.0',
     '/opt/csw/lib/ogle',
     '/opt/csw/lib/perl/5.8.8/CORE',
     '/opt/csw/lib/purple-2',
     '/opt/csw/lib/sasl2',
     '/opt/csw/lib/sparcv8',
     '/opt/csw/lib/sparcv8plus',
     '/opt/csw/lib/sparcv8plus+vis',
     '/opt/csw/lib/sparcv9',
     '/opt/csw/lib/svn',
     '/opt/csw/lib/xfce4/modules',
     '/opt/csw/libexec/firefox/lib/firefox-1.5.0.6',
     '/opt/csw/libexec/firefox/lib/firefox-1.5.0.7',
     '/opt/csw/mozilla/firefox/lib',
     '/opt/csw/mozilla/thunderbird/lib',
     '/opt/csw/mysql4//lib/mysql',
     '/opt/csw/mysql4/lib/mysql',
     '/opt/csw/mysql4/lib/mysql/$ISALIST',
     '/opt/csw/mysql4/lib/mysql/sparcv9',
     '/opt/csw/mysql5/lib',
     '/opt/csw/mysql5/lib/$ISALIST',
     '/opt/csw/mysql5/lib/$ISALIST/mysql',
     '/opt/csw/mysql5/lib/64',
     '/opt/csw/mysql5/lib/64/$ISALIST/mysql',
     '/opt/csw/mysql5/lib/64/mysql',
     '/opt/csw/mysql5/lib/mysql',
     '/opt/csw/mysql5/lib/mysql/$ISALIST',
     '/opt/csw/nagios/lib',
     '/opt/csw/nagios/lib/\\$ISALIST',
     '/opt/csw/openoffice.org/basis3.1/program',
     '/opt/csw/openoffice.org/ure/lib',
     '/opt/csw/postgresql/lib',
     '/opt/csw/postgresql/lib/$ISALIST',
     '/opt/csw/postgresql/lib/sparcv9',
     '/opt/csw/ssl/lib',
     '/opt/cw/gcc3/lib',
     '/opt/forte8/SUNWspro/lib',
     '/opt/forte8/SUNWspro/lib/rw7',
     '/opt/forte8/SUNWspro/lib/rw7/v9',
     '/opt/forte8/SUNWspro/lib/v8',
     '/opt/forte8/SUNWspro/lib/v9',
     '/opt/schily/lib',
     '/opt/sfw/lib',
     '/opt/studio/SOS10/SUNWspro/lib',
     '/opt/studio/SOS10/SUNWspro/lib/rw7',
     '/opt/studio/SOS10/SUNWspro/lib/v8',
     '/opt/studio/SOS10/SUNWspro/lib/v8plus',
     '/opt/studio/SOS11/SUNWspro/lib',
     '/opt/studio/SOS11/SUNWspro/lib/rw7',
     '/opt/studio/SOS11/SUNWspro/lib/rw7/v9',
     '/opt/studio/SOS11/SUNWspro/lib/stlport4',
     '/opt/studio/SOS11/SUNWspro/lib/stlport4/v9',
     '/opt/studio/SOS11/SUNWspro/lib/v8',
     '/opt/studio/SOS11/SUNWspro/lib/v8plus',
     '/opt/studio/SOS11/SUNWspro/lib/v9',
     '/opt/studio/SOS8/SUNWspro/lib',
     '/opt/studio/SOS8/SUNWspro/lib/rw7',
     '/opt/studio/SOS8/SUNWspro/lib/rw7/v9',
     '/opt/studio/SOS8/SUNWspro/lib/v8',
     '/opt/studio/SOS8/SUNWspro/lib/v8plusa',
     '/opt/studio/SOS8/SUNWspro/lib/v9',
     '/opt/studio10/SUNWspro/lib',
     '/opt/studio10/SUNWspro/lib/rw7',
     '/opt/studio10/SUNWspro/lib/rw7/v9',
     '/opt/studio10/SUNWspro/lib/stlport4',
     '/opt/studio10/SUNWspro/lib/stlport4/v9',
     '/opt/studio10/SUNWspro/lib/v8',
     '/opt/studio10/SUNWspro/lib/v9',
     '/oracle/product/9.2.0/lib32',
     '/usr/X/lib',
     '/usr/ccs/lib',
     '/usr/ccs/lib/sparcv9',
     '/usr/dt/lib',
     '/usr/lib',
     '/usr/lib/sparcv9',
     '/usr/local/lib',
     '/usr/local/openldap-2.3/lib',
     '/usr/openwin/lib',
     '/usr/openwin/lib/64',
     '/usr/sfw/lib',
     '/usr/ucblib',
     '/usr/xpg4/lib',
     'RIGIN/../lib'])