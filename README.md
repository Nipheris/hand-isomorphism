Poker Hand Isomorphisms
=======================

author: Kevin Waugh (waugh@cs.cmu.edu)
date: April 7, 2013

This repository contains a C library for efficiently mapping poker hands to and
from a tight set of indices.  Poker hands are isomorphic with respect to
permutations of the suits and ordering within a betting round.  That is,
AsKs, KdAd and KhAh all map to the same index preflop.

Please see:

K. Waugh, 2013. A Fast and Optimal Hand Isomorphism Algorithm.  In the Second
Computer Poker and Imperfect Information Symposium at AAAI

for more details, and src/hand_index.h for the API's description.


How to Build
============

1. *Windows only:* Install Windows SDK (for example, through WinGet: `winget install Microsoft.WindowsSDK`). `Windows SDK for Desktop C++ {amd64/x86} Apps` features are required.
1. *Visual Studio 2019:* Install Desktop C++ or C++ build tools workload.
1. Install Python 3.7+
1. *Visual Studio 2019:* Open Developer PowerShell for VS 2019 and change the execution policy to `Unrestricted` (for example: `Set-ExecutionPolicy Unrestricted -Scope Process`).
1. Change working directory to the repository root.
1. Invoke `python -m venv .venv` to create Python virtual environment
1. Activate Python virtual environment (see [venv module docs](https://docs.python.org/3/library/venv.html) for more options):
	- bash on POSIX: `$ source .venv/bin/activate`
	- PowerShell on Windows: `PS C:\> .venv\Scripts\Activate.ps1`
1. Install Conan within virtual environment: `pip install conan==1.35.0`
1. Build library and create a binary package using `conan create` command:
```
conan create . <version>@<user>/<channel>
	-s arch=<arch>
	-s os=<os>
	-s build_type=RelWithDebInfo
	-s compiler=<compiler>
	-s compiler.runtime=MT
	-s compiler.version=<compiler_version>
```
where:
- `<version>` is a current library version
- `<user>` and `<channel>` - Conan user and channel you want to use with your build of a library (see [Conan docs](https://docs.conan.io/en/1.35/reference/conanfile/attributes.html#user-channel) for details)
- `<arch>` is a target machine architecture, for example `x86_64`
- `<os>` is a target operating system, for example `Windows`
- `<compiler>` and `<compiler_verson>` - see supported compilers and versions in [default settings of Conan](https://github.com/conan-io/conan/blob/1.35.0/conans/client/conf/__init__.py#L61)

for example (PowerShell):
```
conan create . 0.1.0@kevin/testing `
	-s arch=x86_64 `
	-s os=Windows `
	-s build_type=RelWithDebInfo `
	-s compiler="Visual Studio" `
	-s compiler.runtime=MT `
	-s compiler.version=16
```
