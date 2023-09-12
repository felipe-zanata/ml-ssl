$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://meuip.com.br');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
curl_setopt($ch, CURLOPT_HEADER, 1);
curl_setopt($ch, CURLOPT_ENCODING, 'gzip, deflate');
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'Host: meuip.com.br',
    'Connection: keep-alive',
    'User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AplleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept: text/html, application/xhtml_xml, applcation/xml;q=0.9, iamge/avif, image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_SSL_VERYPEER, false);
$meuip = curl_exec($ch);
$meuip = getStr($meuip, 'Meu ip é', '<');