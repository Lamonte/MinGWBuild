"""
************************************************************************************************
* MINGW_Build																			   *
* Automatically add projects to your source and run the command through MinGW(g++) on windows  *
* @Copyright 	Lamonte Harris 2013 														   *
************************************************************************************************
"""

import sublime, sublime_plugin, os, subprocess

cpp_file_list 	= [] 	#array of .cpp files
command_line 	= "" 	#cmd commands

#Setup our code to look for the proper source
def mingwbuild_init(self):
	global cpp_file_list

	#make sure the current file is .cpp before doing anything else
	filename = self.view.file_name()
	filedata = filename.split(".")

	if(len(filedata) == 2):
		if(filedata[1] != 'cpp'):
			print("[Error: Invalid File type: " + filedata[1])
			return False
	else:
		print("[Error: File doesn't have an extension]")
		return False

	#load link commands from settings
	settings = sublime.load_settings("mingw_build.sublime-settings")
	commands = settings.get("mingwbuild_commands")
	
	#get the current path of the current file
	cur_path = os.path.dirname(os.path.realpath(filename))
	
	#find all .cpp files and store them in an array
	if(settings.get("mingwbuild_dont_add_cpp_files") == False):
		mingwbuild_loop_through_folder(cur_path)

	#make sure cpp file list isn't empty before adding other files to project
	project_files 	= ""

	#loop through cpp file and remove the current file from list
	_cpp_file_list = []

	for _cpp_file in cpp_file_list:
		if(_cpp_file != filename):
			_cpp_file_list.append(_cpp_file)

	cpp_file_list = _cpp_file_list

	if(len(cpp_file_list) > 0):
		project_files = ' "' + '" "'.join(cpp_file_list) + '"'

	command_line 	= "g++ \"" + filename + "\"" + project_files + " -o " + "\"" + filedata[0] + ".exe\" " + commands;
	
	#output the command generated for debugging purposes
	if(settings.get("mingbuild_debug") == True):
		print "----------- DEBUG START -----------"
		print "command: " + command_line + "\n\n"
		print "cpp_array: ", cpp_file_list, "\n\n"
		print "------------ END DEBUG ----------- "

	#run command through command line
	#subprocess.Popen(['cmd', '/K', command_line])
	#subprocess.Popen("cmd /K " + command_line, shell=True)
	#subprocess.call(command_line)
	os.system(command_line + " & pause")

#Loop through folders
def mingwbuild_loop_through_folder(_dir):
	global cpp_file_list
	for file_or_folder in os.listdir(_dir):
		if(os.path.isdir(_dir + "\\" + file_or_folder)):
			mingwbuild_loop_through_folder(_dir + "\\" + file_or_folder)
		else:
			file_data = file_or_folder.split(".")
			if(len(file_data) == 2 and file_data[1] == 'cpp'):

				#we need to stop adding duplicate files to the array
				found = False

				for _cpp_file in cpp_file_list:
					if _dir + "\\" + file_or_folder == _cpp_file:
						found = True

				if found == False:
					cpp_file_list.append(_dir + "\\" + file_or_folder)


#Let sublime do the hard work
class MingwBuildCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		mingwbuild_init(self)

