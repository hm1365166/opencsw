.. _getting-started-optional-steps:

-------------------------------
Getting started, optional steps
-------------------------------

.. _selecting-catalog-release:

Optional: Selecting the catalog release
=======================================

By default, ``pkgutil`` is configured to use the ``testing`` catalog.  See
:ref:`catalog releases <catalog-releases>` for information on releases.

You might want change it to ``unstable`` on your development hosts to catch any
issues before they hit the ``testing`` catalog. Or you can switch it to
``stable`` if you want no updates (except for new stable releases).

You can verify the setting with ``pkgutil -V`` ::

  ...
  maxpkglist              10000 (default: 10000)
  mirror                  http://mirror.opencsw.org/opencsw/unstable
                          (default: http://mirror.opencsw.org/opencsw/unstable)
  noncsw                  false (default: false)
  ...

On the next catalog update with ``pkgutil -U`` the catalogs indexes are
downloaded from the new mirror.

.. _setting-up-cryptograhic-verification:

Optional: Cryptographic verification
====================================

The catalog is signed with PGP and it is a good idea to set up your system to
verify the integrity of the catalog. As the catalog itself contains hashes for
all packages in the catalog this ensures you actually install the packages
which were officially released. First you need to install ``cswpki`` (of course
with pkgutil!)::

  pkgutil -y -i cswpki

Then you need to import the public key::

  root# cswpki --import

The current fingerprint looks like this::

  # gpg --homedir=/var/opt/csw/pki/ --fingerprint board@opencsw.org
  pub   1024D/9306CC77 2011-08-31
        Key fingerprint = 4DCE 3C80 AAB2 CAB1 E60C  9A3C 05F4 2D66 9306 CC77
  uid                  OpenCSW catalog signing <board@opencsw.org>
  sub   2048g/971EDE93 2011-08-31

You may also trust the key once you verified the fingerprint::

  root# gpg --homedir=/var/opt/csw/pki --edit-key board@opencsw.org trust

Now everything is in place for enabling security in ``pkgutil``. Edit the ``/etc/opt/csw/pkgutil.conf``
and uncomment the two lines with ``use_gpg`` and ``use_md5`` so they look like this::

  use_gpg=true
  use_md5=true

You can verify that it worked with ``pkgutil -V``::

  root@login [login]:/etc/opt/csw > pkgutil -V
  ...
  show_current            true (default: true)
  stop_on_hook_soft_error not set (default: false)
  use_gpg                 true (default: false)
  use_md5                 true (default: false)
  wgetopts                not set (default: none)

On the next ``pkgutil -U`` you should see a catalog integrity verification wit ``gpg``::

  ...
  Checking integrity of /var/opt/csw/pkgutil/catalog.mirror_opencsw_current_sparc_5.10 with gpg.
  gpg: Signature made Thu Oct 03 00:32:57 2013 CEST using DSA key ID 9306CC77
  gpg: Good signature from "OpenCSW catalog signing <board@opencsw.org>"
  gpg: WARNING: This key is not certified with a trusted signature!
  gpg:          There is no indication that the signature belongs to the owner.
  Primary key fingerprint: 4DCE 3C80 AAB2 CAB1 E60C  9A3C 05F4 2D66 9306 CC77
  Looking for packages that can be upgraded ...
  Solving needed dependencies ...
  Solving dependency order ...
  
  Nothing to do.
  ...

.. _selecting-mirror:

Optional: Selecting your mirror
===============================

For faster downloads, you can select a mirror geographically close to you.

  http://www.opencsw.org/get-it/mirrors/

Please uncomment the line with ``mirror`` in ``/etc/opt/csw/pkgutil.conf``
so it looks similar to this with the URL replaced by the mirror you picked::

  mirror=http://mirror.opencsw.org/opencsw/unstable


Continue to :ref:`Full setup <installation-full-setup>`.
