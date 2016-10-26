try{
 var shellapp = new ActiveXObject("Shell.Application");
 shellapp.ShellExecute("python", "switchNet.py 1",null, "runas", 1);
}
catch(e){
 WScript.Echo("Something wrong: " + e.description);
}