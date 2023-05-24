# awk -f i1povray_to_dxf.awk output_povray_file.pov > output_dxf_file1.dxf

BEGIN {
  is_reading_vertices = 0
  is_reading_faces = 0
  vertex_index = 0
  face_index = 0
}

{
  # Remove leading and trailing spaces
  gsub(/^[[:space:]]+|[[:space:]]+$/,"")

  # Skip empty lines and comments
  if ($0 ~ /^\/\// || $0 ~ /^$/) {
    next
  }
  
  # Reading vertex vectors
  if ($0 ~ /vertex_vectors/) {
    is_reading_vertices = 1
    next
  }

  # Reading face indices
  if ($0 ~ /face_indices/) {
    is_reading_faces = 1
    next
  }

  if (is_reading_vertices == 1 && NF == 1) {
    num_vertices = $0
    next
  }

  if (is_reading_faces == 1 && NF == 1) {
    num_faces = $0
    next
  }

  if (is_reading_vertices == 1 && NF > 1) {
    gsub(/[<>]/,"")
    vertices[vertex_index++] = $0
  }

  if (is_reading_faces == 1 && NF > 1) {
    gsub(/[<>]/,"")
    faces[face_index++] = $0
  }
}

END {
  print "0\nSECTION\n2\nENTITIES"
  for (i = 0; i < face_index; i++) {
    split(faces[i], face_vertices, ",")
    print "0\n3DFACE"
    for (j = 1; j <= 3; j++) {
      split(vertices[face_vertices[j - 1]], vertex_coordinates, ",")
      printf "1%d\n%s\n2%d\n%s\n3%d\n%s\n", j, vertex_coordinates[1], j, vertex_coordinates[2], j, vertex_coordinates[3]
    }
    print "14\n0.0\n24\n0.0\n34\n0.0"
    print "0"
  }
  print "ENDSEC\n0\nEOF"
}
