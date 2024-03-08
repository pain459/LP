FROM vault:1.13.3

# Expose the port
EXPOSE 8000

# Set resource limits
RUN ulimit -n 65536

# Copy initialization script
COPY init_vault.sh /usr/local/bin/init_vault.sh

# Make initialization script executable
RUN chmod +x /usr/local/bin/init_vault.sh

# Copy configuration file
COPY config.hcl /vault/config/config.hcl

# Start Vault server with configuration file
CMD ["vault", "server", "-config=/vault/config/config.hcl"]

# Set resource limits
CMD ["vault", "server", "-dev", "-dev-listen-address=0.0.0.0:8000", "-dev-root-token-id=root", "-config=/vault/config/config.hcl"]