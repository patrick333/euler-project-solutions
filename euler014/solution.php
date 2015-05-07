<?php
//Longest Collatz sequence
$max=1;
$iMax=1;
$maxN=1000000;
#$maxN=30;
for($i=1;$i<$maxN;$i++){
	$j=$i;
	$len=1;
	while($j!==1){
		if($j%2===0)
			$j/=2;
		else
			$j=3*$j+1;
		$len+=1;	
	}
	if($len>$max){
	  $max=$len;
      $iMax=$i;
	}
	echo $iMax, "" "",$max, ""\n"";
}
#echo $iMax, $max;
//too slow to produce the result in 3 minutes
