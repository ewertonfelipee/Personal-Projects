param($ip)

if(!$ip){
  echo "Ping Sweep"
  echo "Usage: .\scriptname.ps1 target_ip"
}
else{
  foreach($i in 1..254){
    try{
      $resp = ping -n 1 "$ip.i" | select-string "bytes=32"
      $resp.Line.split('')[2] -replace ":",""
    }catch{}
  }
}
