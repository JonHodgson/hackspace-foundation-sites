<?php

    require_once( $_SERVER['DOCUMENT_ROOT'] . '/../lib/init.php');

    $subscribers = $db->translatedQuery( 'SELECT COUNT(id) AS num FROM users WHERE subscribed=true' )->fetchRow();
    $pending = $db->translatedQuery( 'SELECT COUNT(id) AS num FROM users WHERE subscribed=false' )->fetchRow();
    $last = $db->query('select EXTRACT(epoch FROM max(timestamp)) AS num from lhspayments_payment')->fetchRow();
 
if($_GET['format'] == "json") { 
    ?>{"subscribed": <?php print($subscribers['num']); ?>}<?php
} else { 
    print "subscribed:{$subscribers['num']} pending:{$pending['num']} last:{$last['num']}";
}
