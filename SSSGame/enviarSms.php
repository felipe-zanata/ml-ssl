$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://simsms.org/reg-sms.api.php?type=get_number&country_id=BR&operator=Total_BR&service=opt19&id=1&redirectphone=0');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'Host: simsms.org',
    'Connection: keep-alive',
    'Accept: */*',
    'X-Requested-With: XMLHttpRequest',
    'User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AplleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Cookie: _ym_uid=1689721572528725105'; _ym_d=1689721572; _ym_isad=1; supportOnlineTalkID=1pDDRDN1540gQMssPcTScTFXyL0H1JzM; PHPSESSID=jc055av4vcmkj5vlrlqp05udh; dle_user_id=319631; dle_password=82ce70275707c7cccb0310923aeff296; dle_newpm=0; _ym_visorc=w'
    ));
curl_setopt($ch, CURLOPT_HEADER, 1);

$final = curl_exec($ch);
$celularsimsms = getStr($final, 'ok~', '~');
$idsms = getStr($final, '.$celularsimsms.'~', '~'');

if(strpos($final, 'error')) {
    echoAndFlush("Ocorreu algum erro ao gerar seu número na plataforma, provavelmente seu token expirou.<br>");
}

$numeber = 1689788237022;
$min = 10 ** (strlen($number) - 1);
$max = (10 ** strlen($number) -1);
$timestamp = rand($min, $max);

$url = "https://www.sssgame.com/api/member/sendCode";
$data = json_encode(array(
    "email" => "",
    "areaCode" => "+55",
    "mobile" =>celularsimsms,
    "item" => 1,
    "timestamp" => $timestamp
))

$url = "https://www.sssgame.com/api/member/sendCode";
$data = json_encode(array(
    "email" => "",
    "areaCode" => "+55",
    "mobile" =>celularsimsms,
    "item" => 1,
    "timestamp" => $timestamp
))

$ch = curl_init('https://www.sssgame.com/api/member/register');
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'Host: www.sssgame.com',
    'Connection: keep-alive',
    'language: pt',
    'User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AplleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Context-Type: application/json;charset-UTF-8',
    'Accept: application/json, text/plain, */*,
    'device: Pc'
    'sign: ',
    'Cookie: '
));

$sucessMessage = "Código de verificação enviado com sucesso";
$maxAttempts = 3;
$attempts = 0;

for($attempts = 1; $attempts <= $maxAttempts; $attempts++){
    $response = curl_exec($ch);
    $msgsms = getStr($response, 'msg" : "','*');
    $tokensms = getStr($response, 'data" : "','*');

    if(strpos($response, $sucessMessage) !== false) {
        echoAndFlush("SMS enviado com sucesso, script em execução. Aguardando 60 segundos para verificar se o SMS chegou.");

        sleep(60);

        $ch = curl_init();

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, 'https://simsms.org/reg-sms.api.php?type=get_sms&country_id=BR&operator=Total_BR&service=opt19&id='.$idsms.'&redirectphone=0');
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
        curl_setopt($ch, CURLOPT_HTTPHEADER, array(
            'Host: simsms.org',
            'Connection: keep-alive',
            'Accept: */*',
            'X-Requested-With: XMLHttpRequest',
            'User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AplleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Cookie: _ym_uid=1689721572528725105'; _ym_d=1689721572; _ym_isad=1; supportOnlineTalkID=1pDDRDN1540gQMssPcTScTFXyL0H1JzM; PHPSESSID=jc055av4vcmkj5vlrlqp05udh; dle_user_id=319631; dle_password=82ce70275707c7cccb0310923aeff296; dle_newpm=0; _ym_visorc=w'
            ));
        curl_setopt($ch, CURLOPT_HEADER, 1);

        $end = curl_exec($ch);
        $codigosms = getStr($end, 'Your verification code is ', ')');
        if(empty($codigosms)) {
            echoAndFlush("SMS não encontrado.<BR>");exit;
        }
        if(!empty($codigosms)){
            echoAndFlush("SMS encontrado, continuando processo...<BR>".);
        }
    }
}
