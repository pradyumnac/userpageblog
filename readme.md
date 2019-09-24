---  
permalink: /index.html  
---  
# Pradyumna Chatterjee's Blog 
A Blog where I note my thoughts 


## Whats all this code?
TLDR: Well This is where I blog
Long Version:
This is a jupyter notebook based blogging system using Pelican on Python Language. This is a static site generator what is compiled and HTML files created in local machine



## How to Use
- Please note that this is setup with a python Windows machine in mind. You dont need much. A lpatop will do too

### Instal instructions
- Clone this repository using git
```git clone git@github.com:pradyumnac/pradyumnac.github.io.git```
- Rename folder accordingly and  and Switch to the folder
- Open terminal in this folder 
    - The shell.bat will launch you into a windows shell with python Virtualenv activated and ready for future
    - I use windows shell "Cmder.exe" avaialble at [cmder.net](https://cmder.net/)
        - Very Feature rich
    - You may use the vanilla windows prompt
         Just replace the line Cmder with cmd in file `shell.bat`
- Run install.bat
    - This installs all required python libraries and sets up a virtual env in `wenv` folder inside current folder
        - Virtual environment ensures that you system wide python installation is untouched
    - **#prerequisite** Make sure you have Python 3.7 installed from [python.org](https://www.python.org/downloads/)
    - **#prerequisite** Make sure you have git installed and accessible in path [Git for Windows](https://git-scm.com/downloads)
    - **#prerequisite** Pip is also required. Its generally insluded with the latest python distriibution
- Change Git remote to your git repo
    
    - Delete .git folder
    - Open a shell in side the folder
    - Type `Git init`
    - type `git remote add github <your repo ssh url>`
- The code resides in the master branch of this repor
- The blog files generated are stoired in the output folder which is linked to your gh-pages branch 
- Write your article in content
- Double click `pelgen.bat` to generate html files in output folder
- Double click `pelserve.bat` to start a ocal server to [preview your site ](http://localhost:8000)
- To sync your code to git repo
- Double click `update_git.bat` to sync your code to github
    - Type in a message to identify your code checkin
- Double click `pelpub.bat` to upload your generated site into github pages
    - Ensure you have enabled github pages for gh-pages branch [Described here](https://help.github.com/en/articles/configuring-a-publishing-source-for-github-pages)
    - Check out this link for a [Getting Started](https://guides.github.com/features/pages/)
