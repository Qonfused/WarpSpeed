## @file
# Contains the version string of WarpSpeed.
#
# Copyright (c) 2023, The WarpSpeed Authors. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
##

# This project uses Semantic Versioning (https://semver.org/)
_MAJOR_VERSION = '0'
_MINOR_VERSION = '0'
_PATCH_VERSION = '0'

# Note that setup.py uses this version.
__version__ = '.'.join([_MAJOR_VERSION, _MINOR_VERSION, _PATCH_VERSION, 'dev'])
