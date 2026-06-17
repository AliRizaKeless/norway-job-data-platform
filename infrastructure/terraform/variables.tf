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

variable "storage_account_name" {
  description = "Name of the Azure Storage Account"
  type        = string
  default     = "norwayjobdataplatform01"
}

variable "container_name" {
  description = "Name of the Blob Storage container"
  type        = string
  default     = "processed-data"
}