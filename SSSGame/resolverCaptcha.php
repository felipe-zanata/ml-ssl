$captchaImageData = base64_encode($data);

$apiKey = 'e1e76d914d7c894f0d8e18da28de642a'

$ch = curl_init('https://2captcha.com/in.php');
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query(array(
    'key' => $apiKey,
    'method' => 'base64',
    'body' => $captchaImageData
)));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$serverOutput = curl_exec($ch);

list(, $captchaId) = explode('|', $serverOutput);

$captchaAnswer = null;
for($i = 0; $i < 5; $i++){
    sleep(5);

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://2captcha.com/res.php?key=$apiKey&action=get&id=$captchaId');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $serverOutput = curl_exec($ch);
    curl_close($ch);

    if(substr($serverOutput, 0, 3) == 'OK'){
        $captchaAnswer = substr($serverOutput, 3);
        break;
    }
}