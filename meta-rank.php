<?php
include 'config-project.php';

function sort_elements($list){
	for($i=0;$i<count($list);$i++)
		for($j=0;$j<$i;$j++){
			if($list[$i][2] > $list[$j][2]){
				$temp = $list[$i];
				$list[$i]=$list[$j];
				$list[$j]=$temp;
			}
	}
	return $list;	
}

function is_present($val, $l1){
 	for($i=0;$i<count($l1);$i++){
		if(strcmp($val,$l1[$i][0]) == 0)
			return $i;
	}
	return -1;
}

function re_rank($l1, $l2, $l3){
	$list = array(array());
	/*alpha majority code*/
	
	$list=$l1;
        for($i=0;$i<count($l2);$i++){
		$pos=is_present($l2[$i][0],$l1);
		echo $pos.PHP_EOL;          
	if($pos!=-1){
		$list[$pos][2] += $l2[$i][2];
		$list[$pos][2] /= 2;
		}else{
			array_push($list,array($l2[$i][0],$l2[$i][1],2.5,$l2[$i][3]));
		}
         }
		
	return sort_elements($list);
}
     /*$l1 = array(array("Volvo",22,4,2),array("BMW",15,3,3),array("Saab",5,4,2),array("Land Rover",17,5,9));
	$l2 = array(array("Volvo",22,3,2),array("BmmW",15,3,3),array("Saab",5,2,2),array("Lanover",17,5,9));
	$l3 = array();
	
	print_r(sort_elements(re_rank($l1,$l2,$l3)));
	*/
?>
