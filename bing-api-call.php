<?php
include 'config-project.php';
require_once 'HTTP/Request2.php';

function call_bing($query,$list){
	$request = new Http_Request2('https://api.cognitive.microsoft.com/bing/v5.0/search');
	$url = $request->getUrl();

	$headers = array(
    	'Ocp-Apim-Subscription-Key' => '{$api_key_bing}',
	);
	$request->setHeader($headers);
	$parameters = array(
    		'q' => $query,
    		'count' => '10',
    		'offset' => '0',
    		'mkt' => 'en-us',
    		'safesearch' => 'Moderate',
	);

	$url->setQueryVariables($parameters);
	$request->setMethod(HTTP_Request2::METHOD_GET);

	$request->setBody("{body}");
	try{
    		$response = $request->send();
    		$result= $response->getBody()
	
	}catch (HttpException $ex){
    		echo $ex;
	}
	echo $result.PHP_EOL;
	//need to convert the result to array of three attributes.
	return $list;
}
?>
