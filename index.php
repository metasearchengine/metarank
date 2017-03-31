include 'client.php';
include 'mongo-query.php';
include 'config-project.php';
include 'meta-rank.php';

$input_query = $argv[1];
$list = array();
$list_g = array();
$list_b = array();
$list_y = array();

function generate_output_list($query){
	insert_into_querylog($query);
	$list_g= get_response_google($query);
	$list_b= get_response_bing($query);
	$list_y=get_response_yahoo($query);
	
	/*[{ url: "", text:"", rank: ""}] */

	$list= re_rank($list_g,$list_b,$list_y);
	
return $list;
} 
