<?php
//require '';

$json=  file_get_contents('./servers.json');
$data= json_decode($json,TRUE);

//echo( $data['logger']['host']);
$host=$data['logger']['host'];
$port=$data['logger']['port'];
//print_r($data);


$m=new MongoClient("10.17.250.220:27017");
//$m=new MongoClient("$host:$port");

//$m = new MongoDB\Driver\Manager ("$host:$port");
/**
 * @author Indrasekhar
 * 
 * class containing the logging functions which on call, will log details to mongodb
 * 
 *
*/

class logger {
	// mail
	
        // mongo
        const DB="metasearch_response_log_db";
        const LOG_GOOGLE_RESPONSE="Response_Google";
        const LOG_USAGE="Response_Bing";
       
        
        // $m=new MongoClient();

        /**
	 * log google response
	 *
	
	 */
        public static function log_google_response($link, $title, $ratingvalue, $ratingcount, $genre, $client_ip) 
           {
              //$m=new MongoClient();
              global $m;//, $doc;
              $col_google_response=$m->selectCollection(logger::DB, logger::LOG_MAIL);
              $doc_log_mail = array( 
                "link" => $link,//"MongoDB", 
                "title" =>$type, // "database", 
                //"user_id" =>$user_id ,//100,
                "ratingvalue"=>$ratingvalue,
                "ratingcount"=>$ratingvalue,
              		"genre"=>$genre,
                //"user_id"=>$user_id,
                "current_timestamp"=> new MongoDate(),
                "client_ip"=> $client_ip
                //"by", "tutorials point"

       );
              $col_log_mail->insert($col_google_response);
              echo 'Google Response logged!!' . PHP_EOL;
                    return true;

            }
	/**
	 * log bing response
         * 
	 
	 */
public static function log_bing_response($answertypes, $links, $rank, $genre, $client_ip) 
           {
              //$m=new MongoClient();
              global $m;//, $doc;
              $col_bing_response=$m->selectCollection(logger::DB, logger::LOG_MAIL);
              $doc_log_mail = array( 
                "answertypes" => $answertypes,//"MongoDB", 
                "link" =>$links, // "database", 
                //"user_id" =>$user_id ,//100,
                "rank"=>$rank,
                "genre"=>$genre,
              		
                //"user_id"=>$user_id,
                "current_timestamp"=> new MongoDate(),
                "client_ip"=> $client_ip
                //"by", "tutorials point"

       );
              $col_log_mail->insert($col_google_response);
              echo 'Google Response logged!!' . PHP_EOL;
                    return true;

            }
	/**
         * log all the errors
	 *
	 * @param string $type        	
	 * @param string $request_param        	
	 * @param string $request_header        	
	 * @param string $user_id 
         * @param string $client_ip        	
	 * @return boolean status
	 */
	
}
?>