$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$urls = @(
    "https://generativelanguage.googleapis.com",
    "https://huggingface.co",
    "https://civitai.com",
    "https://api.replicate.com",
    "https://api.openai.com"
)

foreach ($url in $urls) {
    try {
        $r = Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 10
        Write-Output "$url => $($r.StatusCode) OK"
    } catch {
        $code = $_.Exception.Response.StatusCode.value__
        if ($code) {
            Write-Output "$url => $code (responded)"
        } else {
            Write-Output "$url => BLOCKED: $($_.Exception.Message.Split(':')[0])"
        }
    }
}
