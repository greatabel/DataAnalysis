#  ./i2transfer.ps1 -input_povray_file "input_povray_file.pov" > output_dxf_file2.dxf

param (
    [Parameter(Mandatory=$true)]
    [string]$input_povray_file
)

$is_reading_vertices = $false
$is_reading_faces = $false
$vertex_index = 0
$face_index = 0
$vertices = @()
$faces = @()

$lines = Get-Content $input_povray_file

for ($i=0; $i -lt $lines.Count; $i++) {
    $_ = $lines[$i].Trim()

    if ($_ -match "^//|^\$|^\{|^\}") {
        continue
    }

    if ($_ -match "vertex_vectors") {
        $is_reading_vertices = $true
        $i += 2 # skip the next line containing the number of vertices
        continue
    }

    if ($_ -match "face_indices") {
        $is_reading_faces = $true
        $i += 2 # skip the next line containing the number of faces
        continue
    }

    if ($is_reading_vertices -and $_ -match "^<[^>]+>$") {
        $_ -replace "[<>]",""
        $vertices += ,($_ -split ",")
        $vertex_index++
        continue
    }

    if ($is_reading_faces -and $_ -match "^<[^>]+>$") {
        $_ -replace "[<>]",""
        $faces += ,($_ -split ",")
        $face_index++
        continue
    }
}

echo "0`nSECTION`n2`nENTITIES"
for ($i = 0; $i -lt $face_index; $i++) {
    $face_vertices = $faces[$i]
    echo "0`n3DFACE"
    for ($j = 0; $j -le 3; $j++) {
        $vertex_coordinates = $vertices[$face_vertices[$j]]
        echo ("1{0}`n{1}`n2{0}`n{2}`n3{0}`n{3}" -f ($j+1), $vertex_coordinates[0], $vertex_coordinates[1], $vertex_coordinates[2])
    }
    echo "14`n0.0`n24`n0.0`n34`n0.0`n0"
}
echo "ENDSEC`n0`nEOF"
