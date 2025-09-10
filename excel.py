from openpyxl import load_workbook
from time import sleep
import sys
from api import (
    get_country_data,
    get_capital_city,
    get_region,
)


def get_column_indexes(sheet):
  headers = [cell.value for cell in sheet[1]]
  try:
    country_col_idx = headers.index("Country") + 1
    capital_col_idx = headers.index("Capital city") + 1
    region_col_idx = headers.index("Region") + 1
    return country_col_idx, capital_col_idx, region_col_idx
  except ValueError as e:
    print(f"Error: Missing column in Excel file - {e}")
    return


def update_columns(sheet, country_col_idx, columns_to_update):
  for row in range(2, sheet.max_row + 1):
    country_cell = sheet.cell(row=row, column=country_col_idx)
    country_name = country_cell.value
    country_data = get_country_data(country_name)
    if not country_data:
      raise ValueError(f"The country {country_name} was not found")

    capital_cell = sheet.cell(row=row, column=columns_to_update[0])
    capital_cell.value = get_capital_city(country_data)
    region_cell = sheet.cell(row=row, column=columns_to_update[1])
    region_cell.value = get_region(country_data)
    sleep(1)  # respect the rate limit of 1 call per second


def fill_excel(filename):
  """
  Updates the capital cities and regions in an Excel file by calling the CountryLayer API
  """

  try:
    workbook = load_workbook(filename)
    sheet = workbook.active

    country_col_idx, *columns_to_update = get_column_indexes(sheet)
    update_columns(sheet, country_col_idx, columns_to_update)

    workbook.save(filename)
    print(f"Successfully saved changes to {filename}")

  except FileNotFoundError:
    print(f"Error: The file {filename} was not found.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
  fill_excel("countries_info.xlsx")
