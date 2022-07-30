Dim scriptPath, currentCommand
set WshShell = CreateObject("WScript.Shell")
    scriptPath = WshShell.ExpandEnvironmentStrings("%USERPROFILE%") & "\bin\automate-files.pyw"
    currentCommand = scriptPath
    WshShell.run currentCommand
set WshShell = Nothing