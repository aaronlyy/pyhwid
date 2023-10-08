from .core import PyHWID

def generate_hwid():
  hwid = PyHWID()
  return hwid.generate()