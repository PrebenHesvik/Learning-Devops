#### Different Linux OS
- Ubuntu
- CentOS
- Debian
- Kali
- Fedora

<br>

#### Where to find things:
- `/home/[user]` ==> home directory for user
- `~` ==> home directory
- `/` ==> root directory


#### Linux Kernel
- Responsibilities
  - Memory management
    - kernel space  (a process in the kernel space has unrestricted access to the underlying hardware)
      - kernel
      - kernel extentions
      - device drivers
    - user space
      - applications/programs
  - Process management
  - Device drivers
  - System calls and security
- kernel version
  - `uname` ==> kernel version
  - `uname -r` ==> specific kernel version
  - `uname -a` ==> prints all the system information
  - `uname -s` ==> prints the kernel name
  - `uname -n` ==> prints the system's node hostname

<br>

#### Shell types
- Bourne Shell (Sh Shell)
- C Shell (csh or tcsh)
- Z Shell (zsh)
- Bourne again Shell (bash)

<br>

#### Command types
- Internal commands (built-in commands)
  - About 30 built-in commands
  - `echo`, `cd`, `pwd`, etc
- External commands
  - `mv`, `date`, `uptime`, `cp`
- To determine if a command is built-in or external, use `type`
  - `type echo` ==> "echo is a shell built-in"

<br>

#### "hardware commands"
- `lscpu` ==> cpu info
- `lsmem --summary` ==> memory information
- `free -m` ==> memory information
- `lshw` ==> detailed info on hardware configuration
- `neofetch` ==> display similar information (has to be installed)

<br>

#### Shell commands

- `alias` ==> replace a command or a series of commands with a single word
  - `alias ls="ls --color=auto"` ==> set `ls` to mean `ls --color=auto`
  - `unalias ls` ==> remove the alias ls


<br>


`cat` ==> lets you create, view, and concatenate files directly from the terminal.
  - It’s mainly used to preview a file without opening a graphical text editor
  - `cat new_file.txt` ==> displays the content of the file
  - `cat > new_file.txt` ==> will create a promt for text input to the file
    - `"this is some example text" + CTRL+D` ==> will insert text into the file
  - `cat filename1.txt filename2.txt > filename3.txt ` ==> merges filename1.txt and filename2.txt and stores the output in filename3.txt.
  - `tac filename.txt` ==> displays content in reverse order


<br>


- `cd` ==> change directory
  - `cd ..` ==> move up one directory
  - `cd -` ==> return to previous directory
  - `cd` ==> change directory to home directory
  - `cd ~[username]` ==> goes to another user's home directory
  - Relative path
    - If the directory structure looks like `home/michael/Asia` and your current directory is `home` but want to go to `Asia` you can just type `cd Asia`.


<br>


- `chmod` ==> change the mode of a file
  - r (read), w (write), x (execute)
  - One of the most common use cases for chmod is to make a file executable by the user. To do this, type chmod and the flag +x, followed by the file you want to modify permissions on:
  - `chmod +x script.py`

<br>


- `comm [file1] [file2]` ==> compare two sorted files line by line and write to standard output; the lines that are common and the lines that are unique.

<br>


- `cp` ==> copy
  - `cp [old-path | filename] [new-path | new-filename]`
  - `cp my_file.txt my_new_filename.txt` ==> copy file and giving it a new name
  - `cp -r my_dir1 /tmp/my_dir1` ==> copy directory (recursive operation)
  - `cp file1.txt file2.txt file3.txt /home/username/Documents` ==> copy three files to documents folder

<br>


- `diff` ==> compares two contents of a file line by line and display the parts that do not match.
  - `diff [option] file1 file2`
    - `-c` ==> displays the difference between two files in a context form
    - `-u` ==> displays the output without redundant information.
    - `-i` ==> makes the diff command case insensitive.


<br>


- `echo` ==> print variable to screen
  - `echo Hello` ==> prints 'Hello'
  - `echo $SHELL` ==> displays the type of shell we are in
  - `echo "this is some file content" >> my_file.txt` ==> write text to file
  - flags:
    `-n` ==> print without using a newline afterwards.

<br>


- `find` ==> search for a file in a directory based on a regex expression
  - `find [flags] [path] -name [expression]`
  - `find ./ -name "long.txt" # ./long.txt ` ==> search for a file named long.txt in the current directory
  - `find ./ -type f -name "*.py"` ==> search for python files in current directory
  - `find ./ -type d -name directoryname` ==> look for a directory


<br>


- `grep` ==> searches for lines that match a regular expression and print them:
  - `grep "linux" my_file.txt`
  - You can count the number of times the pattern repeats by using the -c flag:
    - `grep -c "linux" long.txt`
  - grep stands for Global Regular Expression Print


<br>


- `less [filename]` ==> inspect a file backward (pager)
  - [up-arrow] ==> scrolls up the display one line
  - [down-arrow] ==> scrolls down the display one line
  - [/] ==> search text


<br>


- `locate` ==> find a file in a database system
  - `-i` ==> adding the -i argument will turn off case sensitivity
  - `locate -i school*note` ==> searc h for files that contain words school and note


<br>


- `ls` ==> list files & folders
  - `ls -a` ==> list files & folders including hidden files
  - `ls -R` ==> lists all the files in the sub-directories
  - `ls -lh` ==> shows the file sizes in easiy readable formats
  - `ls -l` ==> provide more details about the files
  - `ls -lt` ==> list files in order of creation date
  - `ls -ltr` ==> list files in reversed order of creation date
  - `ls --help` ==> show all flags that can be used with ls
  - `ls /etc/*release*` ==> show all filenames containing word "release" inside the etc-folder
  - `ls -ld` ==> display file information


<br>


- `mkdir` ==> create folder/file
- `mkdir python javascript` ==> create folder for both python and javascript
  - Instead of writing the following:
    - `mkdir /tmp/asia`
    - `mkdir /tmp/asia/india`
    - `mkdir /tmp/asia/india/bangalore`
  - We can write:
    - `mkdir -p /tmp/asia/india/bangalore`
  - `mkdir -m777 new_folder` ==> creates directory with full read write, execute permissions
  - `mkdir -v [folder/sub_folder]` ==> prints a message for each created directory

<br>


- `more [filename]` ==> inspect a file forward (pagers)
  - [space] ==> scroll the display, one screenful of data at a time
  - [enter] ==> scrolls the display one line
  - [b] ==> scrolls the display backwards one screenful of data
  - [/] ==> search text


<br>


- `mv` ==> move/rename folder/file
  - `mv [old-path] [new-path]` ==> Move/rename file
    - `mv my_file.txt my_new_filename.txt`
    - `mv old_path/filename.txt new_path/filename.txt`


<br>


- `pushd` | `popd`
  - `pushd [options] [directory]` ==> add directory to directory stack
    - use `-n` flag to not cd into the new directory
  - `dirs` ==> print contents of directory stack
    - `pushd +2` => cd into the third directory in the directory stack
  - `popd` ==> removes the top directory from the directory stack
  - `popd -n` ==> removes the second directory
  - `popd +2` ==> removes the third directory


<br>


- `pwd` ==> print present working directory
- `pwd -L or pwd -logical` ==> prints environment variable content, including symbolic links.
- `pwd -P or pwd –physical` ==> prints the actual path of the current directory

<br>


- `rm` ==> remove directory/file
  - `rm -r /tmp/my_dir1` ==> remove directory
    - `-r` stands for recursive operation
  - `rm my_file.txt` ==> remove file
  - `-i` ==> -i prompts system confirmation before deleting a file.
  - `-f` ==> -f allows the system to remove without a confirmation.
  - `-r` ==> -r deletes files and directories recursively.


<br>


-`rmdir` ==> remove directory
  - `rmdir -p my_dir/personal1` ==> remove empty sub-directory and its main folder


<br>


- `sort [filename]` ==> sorted output of the file content


<br>


- `touch` ==> most often used to create new file
  - `touch new_file.txt` ==> create new file without content
  - `cat > new_file.txt` ==> will create a promt for text input to the file
  - `"this is some example text" + CTRL+D` ==> will insert text into the file
  - `cat new_file.txt` ==> displays the content of the file
  - `touch -m my_file.txt` ==> changes the modification date to the current date


<br>




- `tail -n 5` ==> print the last 5 lines of a file
- `head -n 5` ==> print the first 5 lines of a file




<br>


- `tar` ==> arcive multiple files into a **TAR** file
- `tar [options] [archive_filename] [file or directory to be archived]`
- `tar -cvf newarchive.tar /home/user/Documents`
- flags
  - `-x` ==> extracts a file.
  - `-t` ==> lists the content of a file.
  - `-u` ==> archives and adds to an existing archive file.
  - `-c` ==> create a new archive
  - `-f` ==> Archive file name
  - `-t -list` ==> list the contents of an archive
  - `-x –extract, –get` ==>  extract files from an archive
  - `-d, –diff, –compare` ==>  find differences between archive and file system
  - `–delete` ==> Delete from the archive.
  - `-r, –append` ==> append files to the end of an archive
  - `-v` ==> Verbose output
  - `-u, –update` ==> only append files newer than copy in archive
  - `-X, –exclude-from=file` ==> exclude patterns listed in file
  - `-C, –directory=DIR` ==> Change to DIR before performing any operations.
  - `-j, –bzip2` ==> Compress and extract archive through bzip2
  - `-J, –xz` ==> Compress and extrach the archive through xz
  - `-z, –gzip` ==> Compress and extract the archive through gzip


<br>


- `user commands:`
  - `useradd [new_user]` ==> adds new user

  - `userdel [username]` ==> removes user

  - `usermod` ==> modify existing users
    - `usermod JournalDev -a -G sudo, audio, mysql`

  - `passwd` ==> change password for your account


<br>



- `zip [options] [zipfile.zip] file.txt` ==> zip a file
- `unzip [ziplfile.zip]` ==> unzip a file


<br>



- `jobs` ==> displays al the running processes along with their status
  - `jobs [flags] [jobID]`
  - flags
    - `-i` ==> lists process IDs along with their information
    - `-n` ==> lists jobs whose statuses have changed since the last notification.
    - `-p` ==> lists process IDs only.


<br>


- `du` ==> Check how much disk space is used by a directory
  - `du /home/user/Documents` ==> returns disk space used by that directory

- `./` ==> lets your shell run an executable file with any intrepreter installed

- `exit` ==> end the shell session and automatically close the terminal

- `top` ==> displays all running processes

- `kill` ==> kill a process
  - `kill [signal_option] pid`
  - To kill a program, you must know its process identification number (PID). If you don’t know the PID, run the following command
    - `ps ux`
  - `kill firefox`
  - Signal-options
    - `SIGTERM` requests a program to stop running and gives it some time to save all of its progress. The system will use this by default if you don’t specify the signal when entering the kill command.
    - `SIGKILL` forces programs to stop, and you will lose unsaved progress.

- `history` ==> displays an enumerated list with the commands you've used in the past





- `whatis` ==> prints a single-line description of any command
  - `whatis python`

- `apropos [command]` ==> search for a command

- `wc` ==> word count
  - `wc my_file.txt` ==> count numbers of words in file

- `man [command_name]` ==> provides a user manual of any commands or utilities you can run in Terminal, including the name, description, and options.


<br>


- `PATH`
  - `export PATH=$PATH;/opt/obs/bin` ==> include path to obs-studio in path
  - `which obs-studio`

- `echo $PS1`
  - `W ==> present working directory
  - $ ==> prompt symbol

- Multiple commands at once
  - `cd new_directory; mkdir www; pwd` ==> multiple commands (pwd stands for print working directory)

- `whoami` ==> returns user account
- `env` ==> list of environment variables
  - `export OFFICE=caleston` ==> set a variable named OFFICE to equal caleston
- `id` ==> returns more info on user account
- `file [file or complete path]` ==> display file information
- `su <new_user>` ==> switch to new user account (su = switch user)
- `curl https://www.some-site.com/some-file.txt -O` ==> download file
- `wget https://www.some-site.com/some-file.txt -O some-file.txt` == download file
- `traceroute` ==> Trace all the network hops to reach the destination
- `ifconfig` - Display network interfaces and IP addresses
- `ln -s [source_path] [link_name]` ==> create a link to another file

#### Linux package managers
- RPM (Red Hat Package Manager)
  - `rpm -i <package-name>` ==> install package
  - `rpm -e <package-name>` ==> uninstall package
  - `rpm -q <package-name>` ==> query package
  **rpm does not install dependencies, so we use `yum` instead**

  - `yum install <package-name>` ==> install package and all dependencies
  - `yum repolist` ==> see the list of repositories available on a system
  - `ls /etc/yum.repos.d/` ==> see where the repos are configured
  - `cat /etc/yum.repos.d/CentOS-Base.repo` ==> look inside a repo file
  - `yum list ansible` ==> see a list of installed/available packages
  - `yum remove <package-name>` ==> remove package
  - `yum --showduplicates <package-name>` ==> show duplicates of package
- APT (Advanced Package Tool)
  - `apt-get [package-name]`
  - `apt-get update` ==> synchronizes the package files from their sources.
  - `apt-get upgrade` ==> installs the latest version of all installed packages.
  - `apt-get check` ==> updates the package cache and checks broken dependencies.


#### Services
- `service httpd start` ==> start service (apache web server)
- `systemctl start httpd` ==> start service
- `systemctl stop httpd` ==> stop service
- `systemctl status httpd` ==> check service status
- `systemctl enable httpd` ==> configure HTTPD to start at startup
- `systemctl disable httpd` ==> configure HTTPD to not start at startup
![img](../../images/services.PNG)

#### Networking
- `ip link` ==> list and modify interfaces on the host
- `ip addr` ==> to see the ip addresses assigned to an interface
- `ip addr add` ==> set ip addresses to an interface
- `ping` ==>
- `ip route` ==> view the routing table
- `ip route add` ==> add entry to the routing table
- `cat proc/sys/net/ipv4/ip_forward` ==> check if ip forwarding is enabled on a host
- ufw - Firewall command
- iptables - Base firewall for all other firewall utilities to interface with



#### Tips/links
- https://www.makeuseof.com/most-linux-pager/