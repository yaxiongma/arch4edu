#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends = ['torch7-git', 'torch7-paths-git', 'torch7-sys-git']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
