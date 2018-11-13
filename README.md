# pi-reboot-button-kiosk

Reboot Button script based on the script by Barry Hubbard http://www.barryhubbard.com/raspberry-pi/howto-raspberry-pi-raspbian-power-on-off-gpio-button/

Chromium is set to autostart, screensaver is disabled. 




From Scratch...
1. Install base Raspbian OS with Desktop
2. Set localizations, update, enable SSH and VNC, hostname (see below...)
   Set static IP (see static_ip_config.txt...), 
   Disable screensaver (see disable_screensaver.txt...) etc
3. Copy the button script from Github (https://github.com/jeff89179/pi-reboot-button-kiosk)
4. Setup lxsession to autostart Chromium (see chromium_autostart.txt...)
5. Setup rc.local to autostart the shutdown_pi.py script (see reboot_button_autostart.txt...)
6. Run "python /home/pi/shutdown_pi.py" to run and test the button
7. Test the button again
8. Add Tab Carousel or Tab Revolver extension to Chrome
  Tab Revolver https://chrome.google.com/webstore/detail/revolver-tabs/dlknooajieciikpedpldejhhijacnbda?hl=en
  Tab Carousel https://chrome.google.com/webstore/detail/tabcarousel/ddldimidiliclngjipajmjjiakhbcohn?hl=en

===================================================================

Setting localizations, enabling SSH, VNC, changing hostname, update...
1. Localizations and Updates can be handled upon first boot (as of the October 2018 Raspbian image). 
2. Enabling SSH, VNC can be done with "sudo raspi-config" and going under "Interfacing Options".
3. Changing hostname can be done with "sudo raspi-config" and going under "Network Options".

===================================================================
