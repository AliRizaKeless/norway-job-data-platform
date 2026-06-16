resource "azurerm_resource_group" "data_platform_rg" {
  name     = var.resource_group_name
  location = var.location
}