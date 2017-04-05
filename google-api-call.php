<?php
include 'config-project.php';

function call_google($query,$list){	
	$ch = curl_init();
	for($i=0;$i<$number_of_requests;$i++){
		$count=10;
		$start_Index=1+$i*10;
		$url= "https://www.googleapis.com/customsearch/v1?key=".$api_key_google."&cx=".$custom_searchengine_id."&q=".$query."&start=".$start_Index."&num=".$count;
	}
	curl_setopt($ch, CURLOPT_URL, $url);
	$result = curl_exec($ch);
	curl_close($ch);

	echo $result.PHP_EOL;
	//need to convert the result to array of three attributes.
	return $list;	
}
?>
