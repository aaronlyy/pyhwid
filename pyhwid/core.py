from uuid import getnode


class PyHWID:
  def __init__(self):
    pass

  def generate(self):
    pass

  def get_mac_address(self) -> str:
    """Get the MAC address as a 48bit integer

    Note: Using this methods MAC address as part of an HWID is unsafe
    because the uuid package fakes the MAC address if it is unable to get the actual address

    Returns:
        str: MAC address as 48bit integer
    """
    mac_address = getnode() # use uuid to get the mac address as 48bit integer
    return mac_address

  def get_cpu(self) -> str:
    pass

  def get_gpu(self) -> str:
    pass

x = PyHWID()
print(x.get_mac_address())