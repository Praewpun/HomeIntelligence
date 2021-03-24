#  Check if host already exist: .exists() before create or delete
import socket 

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

