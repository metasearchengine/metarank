<?php
include 'client.php';
include 'mongo-query.php';
include 'config-project.php';
include 'meta-rank.php';

$input_query = $argv[1];
$list = array();
$list_g = array(array());
$list_b = array(array());
$list_y = array(array());

function generate_output_list($query){
	$time_now=time();
	insert_into_querylog($query,$time_now);
	$list_g= get_response_google($query);
	$list_b= get_response_bing($query);
	$list_y=get_response_yahoo($query);
	
	/*[{ url: "", text:"", rank: ""}] */

	$list= re_rank($list_g,$list_b,$list_y);
	
return $list;
} 

$list_res=generate_output_list($input_query);

for($i=0;$i<count($list_res);$i++){
	//iterate over the results to show on webpage
	$list_res[$i].PHP_EOL;
}

?>
