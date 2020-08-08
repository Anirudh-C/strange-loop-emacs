# strange-loop-emacs
This repository contains my emacs configuration within the <kbd>config.org</kbd> file.

## Install
1. Install Emacs
2. Clone this repo (make sure to remove the <kbd>.emacs.d/</kbd> folder if it already exists)

   ``` shell
   $ git clone https://github.com/Anirudh-C/strange-loop-emacs.git ~/.emacs.d
   ```
3. Clone org-mode
   ``` shell
   $ cd ~/.emacs.d
   $ git submodule update --init
   ```
4. And you're done. Start Emacs (make sure you have a working internet connection) and wait for it to install all the packages.

*Note*: In order to update the dependencies for <kbd>pdf-tools</kbd> you will be prompted to enter the root password.
