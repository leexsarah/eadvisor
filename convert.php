<?php
	include('class.pdf2text.php');
	$dir = "uploaded/";
	$fi = $dir . basename($_FILES["upload"]["name"]);
	$type = pathinfo($fi,PATHINFO_EXTENSION);
	if($type != "pdf") 
	{
    		echo "Error. Please upload a PDF file.";
    	}
	else
	{
		move_uploaded_file($_FILES["upload"]["tmp_name"], $fi);
		$a = new PDF2Text();
		$a->setFilename($fi);
		$a->decodePDF();
		$f = fopen("tda.txt", "w"); 
		fwrite($f, $a->output()); 
		fclose($f);
		echo "Upload is complete!";
	}
?>