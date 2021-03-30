<?php
$nama='Rizky Ramadhani';
$golongan = 'A';

switch ($golongan) {
	case 'A':
		$gaji = '6500000';
		break;

	case 'B':
		$gaji = '5500000';
		break;

	case 'C':
		$gaji = '4500000';
		break;

	case 'D':
		$gaji = '3500000';
		break;
	
	default:
		echo "Coba Lagi";
		break;
}

$jeniskelamin = 'Laki';
$status = 'Menikah';
if ($jeniskelamin = 'Laki-Laki' and $status = 'Menikah') {
	$tunjang = 'Tunjangan: 10%';
} else {
	$tunjang = 'Tidak Mendapatkan Tunjangan!';
}

$tunjangan = $gaji*10/100;
$total = $tunjangan + $gaji;

echo "-----------------------------------<br>";
echo "Nama: $nama<br>";
echo "Golongan: $golongan<br>";
echo "Jenis Kelamin: $jeniskelamin<br>";
echo "Status: $status<br>";
echo "Gaji Anda: $gaji<br>";
echo "$tunjang<br>";
echo "Total Gaji Anda: $total<br>";
echo "-----------------------------------<br>";

?>
