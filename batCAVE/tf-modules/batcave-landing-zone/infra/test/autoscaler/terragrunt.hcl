locals {
  common = read_terragrunt_config(find_in_parent_folders("common.hcl")).locals
}

include "parent" {
  path = find_in_parent_folders()
}

include "vpc-dependency" {
  path = "../../base/vpc/dependency.hcl"
}

include "eks-cluster-dependency" {
  path = "../../base/eks-cluster/dependency.hcl"
}

include "autoscaler" {
  path   = "../../base/autoscaler/terragrunt.hcl"
}

inputs = {
  ## Environment specific config
  #rotate_nodes_after_eniconfig_creation = true

  cpu_limits = "50m"
  cpu_requests = "10m"
  memory_limits = "150Mi"
  memory_requests = "89.7Mi"
}
