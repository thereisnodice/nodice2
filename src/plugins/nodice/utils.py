# utils.py
# 工具模块，负责各个模块之间的交互

import re

from .calculator import getCalculator
from .message import getGlobalMsg,format_string
from .deck import getDeck
from .sqlite import *
from .others import get_jrrp,get_rules
from .character import *
        