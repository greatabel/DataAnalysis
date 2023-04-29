# Usage:
# awk -f mesh_converter.awk -v output_format=<format> input.txt > output_file
# where <format> is either "povray" or "dxf"

# awk -f i0mesh_converter.awk -v output_format=povray input.txt > output_povray_file.pov

# awk -f i0mesh_converter.awk -v output_format=dxf input.txt > output_dxf_file.dxf

BEGIN { FS = "[[:space:]]+" }

# Handle input
{
  # Find the number of points
  if (/NUMBER OF POINTS/) {
    num_points = $4
  }
  # Find the coordinates of each point
  else if (/^[0-9]+/) {
    x = $2
    y = $3
    z = $4
    vertices[NR - 1] = sprintf("<%s, %s, %s>", x, y, z)
  }
  # Find the number of triangles
  else if (/NUMBER OF TRIANGLES/) {
    num_triangles = $4
    getline
    for (i = 1; i <= num_triangles; ++i) {
      split($0, ids, " ")
      triangles[i] = sprintf("<%s, %s, %s>", ids[1] - 1, ids[2] - 1, ids[3] - 1)
      getline
    }
  }
  # Ignore comments and blank lines
  else if (/^#/ || NF == 0) {
    next
  }
  # If we get here, the line is invalid
  else {
    print "Invalid line: " $0
  }
}

# Handle output
END {
  if (output_format == "povray") {
    print "// Mesh description in POV-Ray format\n\nmesh2 {"
    print "  vertex_vectors {\n    " num_points
    print vertices[1]
    for (i = 2; i <= num_points; ++i) {
      print ",\n" vertices[i]
    }
    print "  }\n\n  face_indices {\n    " num_triangles
    print triangles[1]
    for (i = 2; i <= num_triangles; ++i) {
      print ",\n" triangles[i]
    }
    print "  }\n}"
  } else if (output_format == "dxf") {
    print "0\nSECTION\n2\nENTITIES"
    for (i = 1; i <= num_triangles; ++i) {
      split(triangles[i], ids, "[^0-9]+")
      print "0\n3DFACE"
      for (j = 1; j <= 4; ++j) {
        split(vertices[ids[j + 1]], coords, "[^0-9.-]+")
        printf "1%d\n%s\n2%d\n%s\n3%d\n%s\n", j, coords[2], j, coords[3], j, coords[4]
      }
    }
    print "0\nENDSEC\n0\nEOF"
  } else {
    print "Error: Unsupported output format '" output_format "'. Supported formats are 'povray' and 'dxf'."
  }
}
