# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyPywavelets(PythonPackage):
    """PyWavelets is a free Open Source library for wavelet transforms
       in Python"""

    homepage = "https://github.com/PyWavelets"
    url = "https://pypi.io/packages/source/P/PyWavelets/PyWavelets-0.5.2.tar.gz"

    version('0.5.2', 'aedda732f064cf9395f03d37f1003d1a')

    import_modules = ['pywt', 'pywt.data']

    depends_on('py-setuptools', type='build')
    depends_on('py-cython', type='build')
    depends_on('py-numpy@1.9.1:',  type=('build', 'run'))
