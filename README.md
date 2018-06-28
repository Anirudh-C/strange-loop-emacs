# fiddler-emacs
This repository contains my emacs configuration within the <kbd>config.org</kbd> file.

## Install
1. Install Emacs (obviously)
2. Make yourself a <kbd>.emacs.d/</kbd> directory, if Emacs didn't make one for you

   ``` shell
   $ mkdir .emacs.d/
   ```
3. Change into <kbd>.emacs.d/</kbd> and clone this repo there.

   ``` shell
   $ cd .emacs.d/
   $ git clone https://github.com/Anirudh-C/fiddler-emacs.git
   ```
4. And you're done. Start Emacs (make sure you have a working internet connection) and wait for it to install all the packages.

## Adding More Config
If you have a look at the <kbd>init.el</kbd> file, you will see just a couple of lines.

The first line tells Emacs to load Org-Mode before anything else. The next line tells Emacs to load the <kbd>config.org</kbd> file using
org-babel which is Org mode's system to execute active source code embedded in source code blocks in Emacs.

Babel takes all the Emacs-lisp in the <kbd>config.org</kbd> and creates a file called <kbd>config.el</kbd> in the same directory. Now
that file is loaded and interpreted like a usual elisp file.

So adding more config with documentation is simple. Just add some documentation around a source code block embedding Emacs-lisp and reload
Emacs. Emacs will regenerate <kbd>config.el</kbd> and run it again.

**NOTE:**

- You might be wondering what the <kbd>custom.el</kbd> file is for. It is a file that is populated by the Customize option of Emacs. If you don't
  have that file Emacs will throw some angry text at you. Just remove the line that separates my custom options from the <kbd>config.org</kbd> file
  and Emacs will dump all of it in the <kbd>init.el</kbd> file.
- There might be some compile-time *Warnings* when Emacs compiles these configurations for the first time. Let me know, if you know what they signify.
     