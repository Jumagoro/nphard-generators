"""Simple sandbox. Can be overwritten any time"""

import numpy as np
from nphard_generators import MCPRandomFactory
from nphard_generators import HCPRandomFactory

a = MCPRandomFactory.generate_instance(20, 0.1)

b = HCPRandomFactory.generate_instance(20, 0.1)
