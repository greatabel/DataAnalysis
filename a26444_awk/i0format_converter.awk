# Set the field separator to any whitespace character
BEGIN { FS = "[[:space:]]+" }

# Find the number of points
/NUMBER OF POINTS/ {
  num_points = $4
  print "Number of Points: " num_points
}

# Find the coordinates of each point
/^[0-9]+/ {
  x = $2
  y = $3
  z = $4
  print "Point " $1 " (" x ", " y ", " z ")"
}

# Find the number of triangles
/NUMBER OF TRIANGLES/ {
  num_triangles = $4
  print "Number of Triangles: " num_triangles
}

# Find the vertices of each triangle
/^[0-9]+ [0-9]+ [0-9]+ [0-9]+/ {
  print "Triangle " $1 " (" $2 ", " $3 ", " $4 ")"
}

# Ignore comments and blank lines
/^#/ || NF == 0 { next }

# If we get here, the line is invalid
{ print "Invalid line: " $0 }
