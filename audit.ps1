$users = Get-LocalUser

$admins = Get-LocalGroupMember Administrators

$enabled = ($users | Where-Object Enabled -eq $true).Count

$disabled = ($users | Where-Object Enabled -eq $false).Count

Write-Host "=== USER ACCOUNT AUDIT ==="

$users | Select-Object Name, Enabled
Write-Host "`nTotal Users: $($users.Count)"
Write-Host "Enabled Users: $enabled"
Write-Host "Disabled Users: $disabled"

Write-Host "=== SYSTEM INFO ==="

Write-Host "Local Users: $($users.Count)"
Write-Host "Admin Members: $($admins.Count)"

Write-Host "=== ADMINISTRATOR ACCOUNTS ==="


$admins | Select-Object Name

