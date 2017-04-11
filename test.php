<?php
	
 include 'meta-rank.php';
	//ini_set('memory_limit','1024M');
	$l1 = array(array("Volvo",22,4,2),array("BMW",15,3,3),array("Saab",5,4,2),array("Land Rover",17,5,9));
	$l2 = array(array("Volvo",22,3,2),array("BmmW",15,3,3),array("Saab",5,2,2),array("Lanover",17,5,9));
	$l3 = array();

	print_r(re_rank($l1,$l2,$l3));
?>
