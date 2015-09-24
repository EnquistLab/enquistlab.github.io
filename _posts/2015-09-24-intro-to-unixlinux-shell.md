---
layout: post
title: "Intro to UNIX/Linux Shell"
description: ""
category: UNIX-Linux 
tags: [unix,linux]
---
{% include JB/setup %}

# What is UNIX?

Unix (all-caps UNIX for the trademark) is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, developed in the 1970s at the Bell Labs research center by Ken Thompson, Dennis Ritchie, and others.

# What is Linux?

Linux is a Unix-like operating system (OS) assembled under the model of free and open-source software development and distribution. The defining component of Linux is the Linux kernel, an operating system kernel first released on 5 October 1991 by Linus Torvalds.

# What's the difference?

Linux is free, UNIX is not.

Mac OSX is UNIX. There are many different flavors of Linux distributions (distros for short), most common distro is Ubuntu. Each distro is customized for specific needs. Kali Linux is designed for penetration testing and "ethical" hacking. 

<a href="https://en.wikipedia.org/wiki/Linux_distribution#/media/File:Linux_Distribution_Timeline_with_Android.svg" target="_blank">Here's and image of the timeline representing the development of various Linux distributions.</a>

---

## Accessing the shell

**Linux:**

```
ALT+CTRL+t
```

**Mac:**

```
ALT+spacebar & search "terminal"
```

![Ubuntu terminal]({{ASSET_PATH}}/images/terminal.png)

## Naviagtion

The following commands are used for navigation through your filesystem.

**List files in current directory:**

```
$ ls
```

**List all files in current directory:**

```
$ ls -al
```

**Change directories**

```
$ cd <dir_name>
```

**Change to directory "project" within your current directory**

```
$ cd project/
```

**Change to directory not within current directory**

```
$ cd /home/username/blogs/enquistlab.github.io
```

Pressing TAB will autocomplete the file path or directory, rather than typing to full path yourself.

Understanding your filesystem will help you navigate. In the example above, notice the backslash before `home`. This is called `root`, where your filesystem begins. If you executed `$ rm -rf /*` then you'll delete your entire filesystem. Don't try this at home. We'll cover the `rm` tool and flags/switches later.

## Creating a file

```
$ touch /path/to/file
```

## Removing (deleting) a file

```
$ rm /path/to/file
```

## Opening a file

UNIX and Linux allow you to open any file type using command line text editors. Open an image and see what it looks like.

Common command line text editors:

1. Vim
1. Vi
1. Nano

Sure, there are more out there but these are most common.

**Open a file:**

```
$ vim /path/to/file
```

Creating a file then opening it is redundant. `$ vim /path/to/file` will create then open the file. Be sure to save before exiting.

#### Command line text editor vs. Word, etc:

Word and Excel will run out of memory very quickly with large files. 

##  Viewing (printing) files to the standard output (stdout)

#### What is stdout?

Standard output, sometimes abbreviated stdout, refers to the standardized streams of data that are produced by command line programs.

**View file in stdout:**

```
$ cat /path/to/file
```

**View head of file:**

```
$ head /path/to/file
```

**View tail of file:**

```
$ tail /path/to/file
```


## Viewing Help and Man pages:

How do I use this command line tool?

Below are the easiest method to viewing help and man pages (manual):

**Help:**

```
$ head --help
```

**Man pages:**

```
$ man head
```

These are basically the same but each show the different parameters or flags/switches for different options. The following line will print the first 10 lines of a given file, rather than just the header or head of the file.

```
$ head -n 10 /path/to/file
```

---

Reading material and sources:

1. <a href="http://www.ee.surrey.ac.uk/Teaching/Unix/" target="_blank">UNIX Tuforial for Beginners</a>
1. <a href="http://www.tldp.org/guides.html" target="_blank">The Linux Documentation Project</a>
1. <a href="https://en.wikipedia.org/wiki/Linux" target="_blank">Wiki: Linux</a>
1. <a href="https://en.wikipedia.org/wiki/Unix" target="_blank">Wiki: Unix</a>
1. <a href="http://www.linfo.org/index.html" target="_blank">The Linux Information Project</a>

PDF Books

1. <a href="http://vic.gedris.org/Manual-ShellIntro/1.2/ShellIntro.pdf" target="_blank">An Introduction to the Linux Command Shell For Beginners</a>
1. <a href="http://rcsg-gsir.imsb-dsgi.nrc-cnrc.gc.ca/documents/basic.pdf" target="_blank">Basic Introduction to UNIX/Linux</a>

