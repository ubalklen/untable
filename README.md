# Untable

A lightweight Python module to scrape HTML tables.

```
>>> import untable
>>> import requests
>>> from pprint import pprint
>>> html = requests.get("https://www.w3schools.com/html/html_tables.asp").text
>>> data = untable.multi(html)
>>> pprint(data)
[{'Company': 'Alfreds Futterkiste',
  'Contact': 'Maria Anders',
  'Country': 'Germany'},
 {'Company': 'Centro comercial Moctezuma',
  'Contact': 'Francisco Chang',
  'Country': 'Mexico'},
 {'Company': 'Ernst Handel', 'Contact': 'Roland Mendel', 'Country': 'Austria'},
 {'Company': 'Island Trading', 'Contact': 'Helen Bennett', 'Country': 'UK'},
 {'Company': 'Laughing Bacchus Winecellars',
  'Contact': 'Yoshi Tannamuri',
  'Country': 'Canada'},
 {'Company': 'Magazzini Alimentari Riuniti',
  'Contact': 'Giovanni Rovelli',
  'Country': 'Italy'}]
```

## Installation
```
pip install untable
```

## Usage
Untable can extract data from two types of tables: single and multi-entity.

Multi-entity tables are like the one in the example above, where a table carries information for multiple items. They have headers on their first row and data on the others. Use [`untable.multi`](untable.py#91) on them.

Single entity tables carry data from only one entity, in a form-like structure. They can have headers and data on the same row. For example:

|                 |              |
| -------------   | ------------ |
| **Name:**       | Ada Lovelace |
| **DOB:**        | 12-10-1815   |
| **Profession:** | Programmer   |

Use [`untable.single`](untable.py#5) on this type of table. You may need to play with the `threshold` parameter to get the extraction right.

Read [untable.py](untable.py) to find more information.

## Contribute
PRs welcome!