MinGWBuild - Sublime Text 2 Plugin
==========

MinGWBuild lets you build complete C++ projects automatically using MinGW(g++) without having 
to manually add each .cpp file to the build file using Sublime Text 2.  By default it's only
functionality is running the "g++ currentfile.cpp [optional] -o currentfile.exe <link options>"
the [optional] reads every .cpp file in your project folder (and unlimited sub folders).  There's
plugin settings in __Prefences -> Package Settings__ which allows you to change the hotkey to your
liking, disable the project option (compile just the current .cpp file) and add linker options.
Which is then directly executed using __CTRL + ALT + B__ by default.


Installation
------------

1. Copy this folder to your 'Sublime Text 2\Packages' folder.
	(Should be located on windows: C:\Users\...\AppData\Roaming\Sublime Text 2\Packages)

Usage
-----

Create your project folder and add your .cpp files and sub folders and header files.  Then hit the hotkey
to build your project.  Not you will need to update your linker options.  By default it's setup
to use SFML 2.0.

-DSFML_STATIC 		allows me to not have to define the SFML_STATIC definition
-mwindows 			disables the SFML window
-static-libgcc  	allows us to staticly link the g++ into the exe
-static-libstdc++   .... ^^^^^^^^^^ ....