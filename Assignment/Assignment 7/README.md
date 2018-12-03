Most distributions carry rsyslog in their repository. So you usually just need  
to use the package manager to install it. Note that on non-systemd systems (most
notably Ubuntu), rsyslog usually is already installed.  

## Installation of rsyslog from source
1. Download the rsyslog tar file from the following link [rsyslog download](http://www.rsyslog.com/downloads).
2. Extract the software with `tar xvzf nameofdownloadrsyslog`. This will create a new subdirectory rsyslog-version in the current working directory. 
- Type `cd` to move  into extracted directory 
3. Install librsyslog file
4. Run  `./configure --enable-rsyslogd --enable-rsyslogrt`
5. Compile the configure file by typing `sudo make`.If an error message comes up, most probably a part of your build environment is not installed. 
6. `sudo make install` to copy relevant file and man directories to respective directory. For more information, refer to installation link[rsyslog source installation](https://www.rsyslog.com/doc/v8-stable/installation/install_from_source.html)


In Arch Linux, syslog is not required, it is equivalent to having journal. Type `journalctl` to check contents of log file.
