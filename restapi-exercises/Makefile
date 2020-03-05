OS := '$(shell uname)'
MAC := 'Darwin'
LINUX := 'Linux'

startserver:
ifeq ($(OS),$(MAC))
   echo 'Invoke MAC'
else
	echo "nope"
endif

define mac_terminal
   osascript -e 'tell application "Terminal" to do script "cd $(PWD); $1"'
endef

define linux_terminal
   xterm -e "cd $(PWD); $1"
endef

install:
	pip install -r requirements.txt

startserver1:
	osascript -e 'tell application "Terminal" to do shell script "python server.py"'
	sleep 3

demo: startserver 
	@echo "OS is $(OS) == $(MAC)"
	#endif
	@echo "=================================="
	sleep 3
	@echo "Get the Info"
	@echo "=================================="
	curl http://localhost:8080/cloudmesh/cpu
	@echo
	@echo "=================================="
