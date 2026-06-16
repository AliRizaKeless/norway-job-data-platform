variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
  default     = "rg-norway-job-data-platform"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "westeurope"
}