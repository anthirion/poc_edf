import excel
import sys


def main():
  if len(sys.argv) > 1:
    filename = sys.argv[1]
    excel.fill_excel(filename)
  else:
    print("Please provide the Excel file name as a command-line argument.")


if __name__ == "__main__":
  main()
