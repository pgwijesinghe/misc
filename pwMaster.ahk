;-----------------------------------------------------------------------------
;######################### Contents ##########################################
;-----------------------------------------------------------------------------

; KeyBindings
; Google Quick Search (Ctrl + Alt + S)
; Horizontal Scrolling (MB4 + Scroll)
; Quickly gather text to a Notepad (Alt + C)
; SearchBoxes (Google and YouTube) (Alt + G, Alt + y)
; Always on top (Win + Space)
; Hide/Unhide Desktop Icons (F12)
; Copy to one note (Alt + V)
; Jump to folder (Alt + J)

;--------------------------------------------------------------------------------
;######################### KeyBindings ##########################################
;--------------------------------------------------------------------------------

Capslock & h::SendInput {Blind}^{Left}
Capslock & j::SendInput {Blind}{Left} 
Capslock & k::SendInput {Blind}{Down}
Capslock & i::SendInput {Blind}{Up}
Capslock & l::SendInput {Blind}{Right}
Capslock & SC027::SendInput {Blind}^{right}
Capslock & o::SendInput {Backspace}
^!t::Run wt.exe			   

;---------------------------------------------------------------------------------------------------------
;######################### Google Quick Search (inside browser) ##########################################
;---------------------------------------------------------------------------------------------------------

^!s::
  Send ^c
  Send ^t
  Send ^v
  Send {Enter}
Return

;-----------------------------------------------------------------------------------------
;######################### Horizontal Scrolling ##########################################
;-----------------------------------------------------------------------------------------

; Default solution (for all other programs)
; XButton1 + Wheel for horizontal scrolling
XButton1 & WheelDown::WheelRight
XButton1 & WheelUp::WheelLeft

; MS Excel
#IfWinActive, ahk_exe EXCEL.EXE

; XButton1 + Wheel for horizontal scrolling (left)
~XButton1 & WheelUp::
    {
        SetScrollLockState, on
        send,{left}
        SetScrollLockState, off
    }
return

; Shift + Wheel for horizontal scrolling (right)
~XButton1 & WheelDown:: 
    {
        SetScrollLockState, on
        send,{right}
        SetScrollLockState, off
    }
return

#IfWinActive

;-----------------------------------------------------------------------------------------
;######################### Double Click ##########################################
;-----------------------------------------------------------------------------------------
XButton2:: Send, {click 2}

;--------------------------------------------------------------------------------------------------------
;######################### Quickly gather text to a Notepad #############################################
;--------------------------------------------------------------------------------------------------------

; Copying text to Notepad for future reference
!c::
    OldClipboard := ClipboardAll
    Clipboard := ""
    Send, ^c
    ClipWait 1 ;pause for Clipboard data
    If ErrorLevel
    {
        MsgBox, No text selected!
    }
    
    IfWinNotExist, Untitled - Notepad
    {
        Run, Notepad
        WinWaitActive, Untitled - Notepad
    }
    
    ; Control, EditPaste used rather than ControlSend for much greater speed of execution
    
    Control, EditPaste, % Clipboard . chr(13) . chr(10) . chr(13) . chr(10) , , Untitled - Notepad
    Clipboard := OldClipboard
Return


;--------------------------------------------------------------------------------------------------------
;######################### Quickly gather text to OneNote #############################################
;--------------------------------------------------------------------------------------------------------
!v::
  ; Copy the highlighted text to the clipboard
  Clipboard := ""
  SendInput, ^c
  ClipWait, 1

  ; Send the text to OneNote
  if (Clipboard != "")
  {
    Run, onenote:..\Notebook_Local#base-path=C:\Users\pubud\Documents
    Sleep, 1500
    SendInput, ^v
    Sleep, 100
    Send, {Enter}
    MsgBox, Note saved to OneNote.
  }
return


;--------------------------------------------------------------------------------
;######################### SearchBoxes ##########################################
;--------------------------------------------------------------------------------

!g::
    InputBox, Search, Google Search, , , 400, 100
    if not ErrorLevel ; when cancel is not pressed
    {
        run C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe https://www.google.com/search?q="%Search%" 
    }
return

!b::
    InputBox, Search, Bing AI, , , 400, 100
	Clipboard = %Search%
    if not ErrorLevel ; when cancel is not pressed
    {
        run C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe https://www.bing.com/search?q=test&showconv=1
		Sleep,3000
		SendInput, ^v
		Send, {Tab}
		Send, {Enter}
	}
return

!y::
    InputBox, Search, YouTube Search, , , 400, 100
    if not ErrorLevel ; when cancel is not pressed
    {
        run C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe https://www.youtube.com/results?search_query="%Search%"
    }
return


;----------------------------------------------------------------------------------
;######################### Always on top ##########################################
;----------------------------------------------------------------------------------

#SPACE::  Winset, Alwaysontop, , A


;----------------------------------------------------------------------------------------------
;######################### Hide/Unhide Desktop Icons ##########################################
;----------------------------------------------------------------------------------------------

F12::
ControlGet, HWND, Hwnd,, SysListView321, ahk_class Progman
If HWND =
ControlGet, HWND, Hwnd,, SysListView321, ahk_class WorkerW
If DllCall("IsWindowVisible", UInt, HWND)
WinHide, ahk_id %HWND%
Else
WinShow, ahk_id %HWND%
Return

;----------------------------------------------------------------------------------------------
;######################### JumpToFolder Hotkey ##########################################
;----------------------------------------------------------------------------------------------
!j::Run D:\apps\JumpToFolder_1.0.8_x64\JumpToFolder.lnk


;----------------------------------------------------------------------------------------------
;######################### Google Voice Search(Normal and Direct) #############################
;----------------------------------------------------------------------------------------------
^+g::
Run, https://www.google.com
Sleep, 1000
Send, {Tab}
Send, {Enter}
Return

^+b::
Run, https://www.bing.com
Sleep, 1000
Send, {Tab}
Send, {Enter}
Return

^+u::
Run, https://www.google.com
Sleep, 1000
Send, {Tab}
Send, {Enter}
Sleep, 5000
Send, {Tab}
Send, {Enter}
Send, {Enter}
Return

;----------------------------------------------------------------------------------------------
;######################### Control Mouse Scroll Speed #############################
;----------------------------------------------------------------------------------------------
; Assign the "Ctrl + Alt + Up Arrow" key combination to increase the scroll speed
^!Up::WheelSpeed(1)

; Assign the "Ctrl + Alt + Down Arrow" key combination to decrease the scroll speed
^!Down::WheelSpeed(-1)

WheelSpeed(amount)
{
  ; Get the current scroll speed
  VarSetCapacity(info, 8)
  DllCall("SystemParametersInfo", "UInt", 104, "UInt", 0, "UInt", &info, "UInt", 0)
  WheelScrollLines := NumGet(info, 0, "Int")

  ; Increase or decrease the scroll speed by the specified amount
  WheelScrollLines += amount

  ; Set the new scroll speed
  DllCall("SystemParametersInfo", "UInt", 105, "UInt", WheelScrollLines, "UInt", 0, "UInt", 0)
}

::]sum::Give me a summary of
::]d::
FormatTime, CurrentDateTime,, yyMMdd
SendInput %CurrentDateTime%
return 