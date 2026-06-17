resource "azurerm_resource_group" "data_platform_rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "data_platform_storage" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.data_platform_rg.name
  location                 = azurerm_resource_group.data_platform_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "processed_data" {
  name                  = var.container_name
  storage_account_id    = azurerm_storage_account.data_platform_storage.id
  container_access_type = "private"
}