build : shutdown.py
	pyinstaller --onefile --noconsole shutdown.py

qtcompile : Graphical/QtCountdownWindow.ui Graphical/QtMainWindow.ui
	pyuic6 -o QtMainWindow.py Graphical/QtMainWindow.ui
	pyuic6 -o QtCountdownWindow.py Graphical/QtCountdownWindow.ui