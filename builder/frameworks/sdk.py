# WizIO 2022 Georgi Angelov
#   http://www.wizio.eu/
#   https://github.com/Wiz-IO/wizio-pico

from __future__ import print_function
from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
platform = "sdk"
module = platform + "-" + env.BoardConfig().get("build.core")
m = __import__(module)
globals()[module] = m
m.dev_init(env, platform)
#print( env.Dump() )
