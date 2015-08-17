---
layout: page
title: RAM Disk
---

## Installing RAM disk

1. Install ImDisk
Install ImDisk Virtual Disk Driver from here: http://www.ltr-data.se/opencode.html/#ImDisk

2. Set-up ImDisk to run on Windows startup
    After successfully completing the installation, open a command prompt as Administrator and run the next line:

    `schtasks /create /ru System /tn "ImDisk Ram Disk" /tr "imdisk -a -s 512M -m X: -p \"/fs:ntfs /q /y\"" /sc onstart`

    `schtasks /run /tn "ImDisk Ram Disk"`

    Command line parameters explained:

    `-a: initializes the virtual disk`

    `-s: size of virtual disk (512M is the size = 512 MegaBytes) (The full choices are b, k, m, g, t, K, M, G, or T)`

    `-m X: sets up the mount point a.k.a. the drive letter, X:`

    `-p "fs:ntfs /q /y" formats the drive in ntfs format (other options are fat (FAT16) or fat32 (FAT32))`


3. Configure IIS server to log on the Ram Disk
From the IIS Manager select Logging and set the directory on the Ram drive, i.e. `x:\LogFiles\`

## Clean-up log files

1. Create a script for cleaning up the log files, script contents:
    {% highlight vbnet %}
Set colArgs = WScript.Arguments.Named
If colArgs.Exists("path") Then
sLogFolder = colArgs.Item("path")
Else  
    sLogFolder =  "x:\LogFiles"
End If
iMaxAge = 1   'in days
Set objFSO = CreateObject("Scripting.FileSystemObject")
set colFolder = objFSO.GetFolder(sLogFolder)
For Each colSubfolder in colFolder.SubFolders
        Set objFolder = objFSO.GetFolder(colSubfolder.Path)
        Set colFiles = objFolder.Files
        For Each objFile in colFiles
                iFileAge = now-objFile.DateCreated
                if iFileAge > (iMaxAge+1)  then
                        objFSO.deletefile objFile, True
                end if
        Next
Next
    {% endhighlight %}

2. Schedule the clean-up script
    Create a new task (submit the correct path to the script):

    `schtasks /create /ru System /sc DAILY /tn "IIS Log Cleaner" /tr "c:\log_cleaner.vbs" /ST 09:00`



## Uninstall

1. Delete the tasks

    `SchTasks /Delete /TN "ImDisk Ram Disk"`

    `SchTasks /Delete /TN "IIS Log Cleaner"`

2. Delete ram disk:
    We can delete a Ram disk with one of the following commands:
    `imdisk -d -m X:`
    or
    `imdisk -D -m X:` (to force a removal)
