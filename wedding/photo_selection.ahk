F7::
Send ^l ; Goto Chrome address bar and select URL
Sleep, 10
Send ^c ; Copy URL
NeedleRegEx := "(?<=preview=)(.*)(?=.jpg)"
str := RegExMatch(clipboard, NeedleRegEx, out_var)
FileAppend, %out_var%`n , C:\Users\pubud\Desktop\selected.txt
return