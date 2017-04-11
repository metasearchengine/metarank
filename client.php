<?php
include 'bing-api-call.php';
include 'google-api-call.php';
include 'yahoo-api-call.php';
include 'config-project.php';

function get_response_google($query){
	$list= array(array());
	$list = call_google($query,$list);
return $list;
}

function get_response_yahoo($query){
	$list= array(array());
	$list = call_yahoo($query,$list);
return $list;
}

function get_response_bing($query){
	$list= array(array());
	$list = call_bing($query,$list);
return $list;
}

?>
