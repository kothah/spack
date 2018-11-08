# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyNumexpr3(PythonPackage):
    """Numexpr3 is a fast numerical expression evaluator for NumPy. With it,
    expressions that operate on arrays (like "3*a+4*b") are accelerated and
    use less memory than doing the same calculation in Python.
    In addition, its multi-threaded capabilities can make use of all your
    cores, which may accelerate computations, most specially if they are not
    memory-bounded (e.g. those using transcendental functions).
    Compared to NumExpr 2.6, functions have been re-written in a fashion such
    that gcc can auto-vectorize them with SIMD instruction sets such as
    SSE2 or AVX2, if your processor supports them. Use of a newer version of
    gcc such as 5.4 is strongly recommended."""
    homepage = "https://github.com/pydata/numexpr/tree/numexpr-3.0"
    url = "https://pypi.io/packages/source/n/numexpr3/numexpr3-3.0.1a1.tar.gz"

    version('3.0.1.a1', '9fa8dc59b149aa1956fc755f982a78ad')
    # TODO: Add CMake build system for better control of passing flags related
    # to CPU ISA.

    depends_on('python@2.6:2.8,3.3:', type=('build', 'run'))
    depends_on('py-numpy@1.7:', type=('build', 'run'))
    depends_on('py-setuptools@18.2:', type='build')