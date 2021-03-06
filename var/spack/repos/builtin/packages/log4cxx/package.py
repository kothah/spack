# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Log4cxx(AutotoolsPackage):
    """A C++ port of Log4j"""

    homepage = "https://logging.apache.org/log4cxx/latest_stable/"
    url      = "http://mirror.netcologne.de/apache.org/logging/log4cxx/0.10.0/apache-log4cxx-0.10.0.tar.gz"

    version('0.10.0', 'b30ffb8da3665178e68940ff7a61084c')

    depends_on('apr-util')
    depends_on('apr')
    depends_on('zip')

    build_directory = 'spack-build'

    # patches from https://aur.archlinux.org/packages/log4cxx/
    patch('log4cxx-0.10.0-missing_includes.patch')
    patch('log4cxx-0.10.0-narrowing-fixes-from-upstream.patch')

    def configure_args(self):
        args = ['--disable-static']

        return args
