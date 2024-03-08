listener "tcp" {
  address     = "0.0.0.0:8000"
  tls_disable = 1
}

storage "file" {
  path = "/vault/data"
}

disable_mlock = true
api_addr = "https://127.0.0.1:8000"
