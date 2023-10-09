from uuid import getnode

def get_mac_address() -> str:
  """Get the MAC address as a 48bit integer

    Note: Using this methods MAC address as part of an HWID is unsafe
    because the uuid package fakes the MAC address if it is unable to get the actual address

  Returns:
      str: MAC address as 48bit integer
  """
  return str(getnode())

if __name__ == '__main__':
  print(get_mac_address())