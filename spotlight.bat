ECHO off
ECHO Hello world
set images_folder=C:\Users\itsbu\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
set rough_folder=C:\Users\itsbu\Pictures\Wallpapers\Rough

xcopy /s %images_folder% %rough_folder%

cd %rough_folder%
ren * *.jpg