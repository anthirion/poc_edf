import excel
import sys


def main():
  if len(sys.argv) > 1:
    filename = sys.argv[1]
  else:
    filename = "countries_info.xlsx"
  excel.fill_excel(filename)


if __name__ == "__main__":
  main()
