#!/usr/bin/env python
# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2014, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------
"""
Takes in a datafile generated by Avogadro, and prepares it for use
with run_anomaly.py (from https://github.com/subutai/nupic.subutai)

- Adds header
- Converts "nan" to 0

TODO: Allow correct handling of monotonically increasing values
"""

import csv
import datetime
import sys



def run(dataPath, outPath):
  with open(dataPath) as csvfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(open(outPath, "wb"))

    # Add header
    writer.writerow(["name", "value", "dttm"])

    for row in reader:
      name = row[0]
      value = row[1]
      timestamp = datetime.datetime.fromtimestamp(int(row[2]))

      # Convert "nan" to 0
      value = value if value != "nan" else "0"

      writer.writerow([name, value, str(timestamp)])



if __name__ == "__main__":
  if len(sys.argv) < 3:
    print ("Usage: {0} "
           "/path/to/data.csv /path/to/outfile.csv").format(sys.argv[0])
    sys.exit(0)

  dataPath = sys.argv[1]
  outPath = sys.argv[2]
  run(dataPath, outPath)