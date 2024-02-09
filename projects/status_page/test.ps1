$headers = @{ "Content-Type" = "application/json" }
$body = @{
    event = "Sample Event"
    detail = "This is a sample event created for testing purposes."
    status = "Open"
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri 'http://localhost:8000/create_event/' -Method POST -Headers $headers -Body $body
if ($response.StatusCode -eq 200) {
    Write-Host "Event created successfully!"
    Write-Host "Event details:" $response.Content
} else {
    Write-Host "Failed to create event. Status code:" $response.StatusCode
    Write-Host "Response:" $response.Content
}
