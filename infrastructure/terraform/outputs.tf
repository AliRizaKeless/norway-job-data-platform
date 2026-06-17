output "resource_group_name" {
  value = azurerm_resource_group.data_platform_rg.name
}

output "resource_group_location" {
  value = azurerm_resource_group.data_platform_rg.location
}

output "storage_account_name" {
  value = azurerm_storage_account.data_platform_storage.name
}

output "blob_container_name" {
  value = azurerm_storage_container.processed_data.name
}