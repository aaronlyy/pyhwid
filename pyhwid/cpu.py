import platform
import os

def get_cpu_name() -> str:
  """Get CPU name

  Returns:
      str: CPU name
  """
  if platform.system() == 'Windows':
    return platform.processor()
  elif platform.system() == 'Darwin':
    pass
  elif platform.system() == 'Linux':
    pass
  else:
    pass

def get_cpu_cores() -> int:
  """Get CPU cores as int

  Returns:
      int: CPU cores
  """
  cores = os.cpu_count()
  if cores == None:
    return 0
  return cores

if __name__ == '__main__':
  print(get_cpu_name())
  print(get_cpu_cores())