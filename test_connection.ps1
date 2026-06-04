[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
try {
    $r = Invoke-WebRequest -Uri 'https://huggingface.co' -UseBasicParsing -TimeoutSec 15
    Write-Output "Status: $($r.StatusCode)"
} catch {
    Write-Output "Error: $($_.Exception.Message)"
}
