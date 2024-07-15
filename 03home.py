import os
from colorama import Fore, Style

def print_directory_structure(path, level=0):

  for item in os.listdir(path):
    item_path = os.path.join(path, item)
    if os.path.isdir(item_path):
      print(f"{level * '  '} {Fore.BLUE}{item}{Style.RESET_ALL}/")
      print_directory_structure(item_path, level + 1)
    else:
      print(f"{level * '  '} {Fore.GREEN}{item}{Style.RESET_ALL}")

if __name__ == "__main__":
  import argparse
  parser = argparse.ArgumentParser(description='Visualize directory structure')
  parser.add_argument('path', help='Path to the directory')
  args = parser.parse_args()

  try:
    print_directory_structure(args.path)
  except FileNotFoundError:
    print(f"Error: Directory '{args.path}' not found.")
  except NotADirectoryError:
    print(f"Error: '{args.path}' is not a directory.")