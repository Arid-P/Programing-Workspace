# ==============================================
# Flask: app.run() Arguments Notes
# ==============================================

# Basic usage:
# app.run(debug=True)
# Starts the Flask development server

# ==============================================
# 1️⃣ host
# ----------------------------------------------
# Specifies the hostname to listen on
# Default: '127.0.0.1' (localhost) → accessible only from your machine
# Example: 
# app.run(host="0.0.0.0")
# - Binds to all IP addresses on the machine
# - Makes server accessible from other devices on the network
# Caution: Don't use 0.0.0.0 in production without proper firewall/security

# ==============================================
# 2️⃣ port
# ----------------------------------------------
# TCP port to listen on
# Default: 5000
# Example:
# app.run(port=8080)
# Access URL → http://127.0.0.1:8080
# Useful when you need multiple Flask apps or port conflicts

# ==============================================
# 3️⃣ debug
# ----------------------------------------------
# Enables debug mode (True / False)
# Default: False
# debug=True does 2 things:
# 1. Shows detailed error pages with stack trace in browser
# 2. Auto reloads server when code changes (hot reload)
# Example:
# app.run(debug=True)

# ==============================================
# 4️⃣ use_reloader
# ----------------------------------------------
# Determines whether Flask should auto-reload on code changes
# Default: True when debug=True
# If you set debug=True but use_reloader=False, code changes won't trigger reload
# Example:
# app.run(debug=True, use_reloader=False)

# ==============================================
# 5️⃣ use_debugger
# ----------------------------------------------
# Enables Werkzeug debugger
# Default: True when debug=True
# Shows interactive debugger in browser on error
# Example:
# app.run(debug=True, use_debugger=True)

# ==============================================
# 6️⃣ threaded
# ----------------------------------------------
# Enables handling requests in separate threads
# Default: False
# True allows multiple clients to be served simultaneously
# Example:
# app.run(threaded=True)
# Note: Development server is not optimized for production

# ==============================================
# 7️⃣ processes
# ----------------------------------------------
# Number of processes to handle requests
# Default: 1
# If >1, Flask uses multiple OS processes (like forking)
# Example:
# app.run(processes=3)
# Rarely used in development, more for testing multi-process behavior

# ==============================================
# 8️⃣ ssl_context
# ----------------------------------------------
# Enable HTTPS (SSL/TLS)
# Can be:
#  - 'adhoc' → generates temporary self-signed certificate
#  - Tuple (cert_file, key_file)
# Example:
# app.run(ssl_context='adhoc')
# Access URL → https://127.0.0.1:5000
# Useful for testing HTTPS locally

# ==============================================
# 9️⃣ extra notes / good practices
# ----------------------------------------------
# - Development server is single-threaded by default → slow for multiple clients
# - Never use app.run() for production; use WSGI server (Gunicorn, uWSGI)
# - Common combination in dev:
#     app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
# - Arguments can be combined as needed:
#     app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)