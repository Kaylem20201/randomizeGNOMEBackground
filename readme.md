# GNOME Background Randomizer
This python script is designed to select a random GNOME background from a specified folder. If you wish to use this script, make sure the directory you want to use is correct under the get_background_paths function.
## Scheduling
This script is best used with an automated schedule, to randomize at certain intervals. The easiest way to do this on Linux is with [crontab](https://www.man7.org/linux/man-pages/man5/crontab.5.html).
"crontab -e" will prompt you to open the crontab file in the editor of your choice. Then, add a line for running "randomBackground.py". For example, if you wanted to randomize the background every 30 minutes:
```
*/30 * * * * python3 [scriptDirectory]/randomBackground.py
```
When you exit the editor, if the syntax was all right, you should see 'installing new crontab', otherwise it will ask you to fix it.