<?php
function penjumlahan ($bil1, $bil2 = 15)
{
	$total = $bil1 + $bil2;
	return $total;
}
echo "Penjumlahan (Bilangan Default = 15)";
echo "<br>";
echo "10 + 10 = ".penjumlahan(10,10);
echo "<br>";
echo "15 + Bilangan Default = ".penjumlahan(15);
echo "<br><br>";

function perkalian ($bil1, $bil2 = 20)
{
	$total = $bil1 * $bil2;
	return $total;
}
echo "Perkalian(Bilangan Default = 20)";
echo "<br>";
echo "10 + 10 = ".perkalian(10,10);
echo "<br>";
echo "15 + Bilangan Default = ".perkalian(15);
echo "<br><br>";

function pembagian ($bil1, $bil2 = 10)
{
	$total = $bil1 / $bil2;
	return $total;
}
echo "Pembagian(Bilangan Default = 10)";
echo "<br>";
echo "10 + 10 = ".pembagian(10,10);
echo "<br>";
echo "15 + Bilangan Default = ".pembagian(15);
echo "<br><br>";
?>
