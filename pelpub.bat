call wenv\scripts\activate
pelican content -s publishconf.py -t D:/Projects/Blogs/Pelican/themes/octopress
ghp-import output && git push githubsite gh-pages:master
set /p message="Press any key to exit.."