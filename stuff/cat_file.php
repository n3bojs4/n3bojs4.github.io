<?php
$file=$_GET["file"];
include("php://filter/convert.base64-encode/resource=$file") ;

?>
