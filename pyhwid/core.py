import platform

from .mac import get_mac_address

from .cpu import get_cpu_cores
from .cpu import get_cpu_name


class PyHWID:
  def __init__(self):
    self.platform = platform.system()
    pass

  def generate(self):
    pass

x = PyHWID()
print(x.get_mac_address())
print(x.get_cpu())