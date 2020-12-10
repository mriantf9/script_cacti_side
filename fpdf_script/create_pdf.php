<?php

$DIR = ("/home/mriantf/script_skripsi");
$DT_RP = ($DIR . "/DATA_REPORT/Daily");
$WORKDIR = ($DIR . "/script");
$SCRIPTDIR = getCwd();
$OUTPUT = ($DIR . "/OUTPUT_PDF");

require('$SCRIPTDIR/fpdf.php');

// intance object dan memberikan pengaturan halaman PDF
$pdf = new FPDF('P', 'mm', 'A4');

// membuat halaman baru
$pdf->AddPage();

// setting jenis font yang akan digunakan
$pdf->SetFont('Arial', 'B', 16);

// mencetak string 
$pdf->Cell(0, 15, 'Graphic Pemakaian', '0', 1, 'C');
$pdf->Output();
