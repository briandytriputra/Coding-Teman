<?php
// perulangan while
echo "Mencetak Nama dan Umur Teman dengan While <br>";
$nama = array("Irpan", "Agung", "Silvi");
$umur = array("20", "19", "19");
$idx  = 0;
while ($idx<count($nama)) {
	echo "$nama[$idx] ($umur[$idx] Tahun)<br>";
	$idx++;
}

echo "<br>Mencetak Nama dan Umur Teman dengan For Each<br>";
$nama = array(19=>"Silvi", 23=>"Ahkam", ); // Umur tidak boleh sama.
foreach ($nama as $umur => $gabung) {
	echo "$gabung ($umur Tahun)<br>";
}
?>
