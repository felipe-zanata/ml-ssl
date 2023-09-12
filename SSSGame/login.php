$data = json_encode(array(
    "username" => "$userpass",
    "password" => "$userpass",
    "confirmPassword" => "$userpass",
    "realName" => "",
    "mobile" => "celularsimsms",
    "spreaderId" => "$convite",
    "verifyCode" => "$captchaAnswer",
    "bithday" => "2023-07-19",
    "email" => "",
    "fistNAme" => "",
    "lastName" => "",
    "areaCode" => "55",
    "mobileCode" => "$codigosms",
    "emailCode" => "",
    "uuid" => "$tokensms",
    "verficationCode" => "$codecap",
    "identificationType" => "CPF",
    "identificationNumber" => "",
    "identificationCode" => 4,
    "timestamp" => $timestamp
));

$ch = curl_init('https://www.sssgame.com/api/member/register');
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_PROXY, 'pr.pyproxy.com:16666');
curl_setopt($ch, CURLOPT_PROXYUSERPWD, 'TropaZ01-zone-resi-region-br:102030Paz');
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'Host: www.sssgame.com',
    'Connection: keep-alive',
    'sec-ch-ua: "Not.A/Brand";v="8", "Chormium;v="114", Google Chrome";v="114",
    'language: pt',
    'sec-ch-ua mobile: ?0',
    'User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AplleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Context-Type: application/json;charset-UTF-8',
    'Accept: application/json, text/plain, */*,
    'device: Pc'
    'sign: c2294354d3494b319f73ca333d293a4a',
    'sec-ch-ua-plataform: "Windowns',
    'Origin: https://www.sssgame.com',
    'Sec-Fetch-Site: same-orgin',
    'Sec-Fetch-Mode: cors',
    'Sec-Fetch-Dest: empty',
    'Referer: https://www.sssgame.com/',
    'Cookie: '
));
$r2 = curl_exec($ch);
$msgfinal = getStr($r2, 'msg" : "','*');