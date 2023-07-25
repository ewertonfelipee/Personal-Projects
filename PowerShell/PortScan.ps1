param($ip)

if(!$ip){
  echo "Port Scan"
  echo "Example: .\script_name.ps1 target"
}
else{
  $topports = 21,22,25,80,443,3306,8080
  try{
    foreach($ip in $topports){
      if(Test-NetConnection $ip -Port $topports -WarningAction SilentContinue -InformationLevel Quiet){
        echo "Open port: $port"
      }
    }
    else{
      echo "Closed Port: $porta"
    }
  }
  catch{}
}
