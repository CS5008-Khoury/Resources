# Resources

The following resources are a *starting* point for resources. These often change, and students are encouraged to submit updates and changes. 

- [Resources](#resources)
  - [Course Text Books](#course-text-books)
  - [O'Reilly Online: Books and Videos](#oreilly-online-books-and-videos)
  - [Algorithms Resources](#algorithms-resources)
    - [Advanced Resources that you may wish to consult as you prepare for CS 5800](#advanced-resources-that-you-may-wish-to-consult-as-you-prepare-for-cs-5800)
  - [C Programming Resources](#c-programming-resources)
    - [Popular Linkedln Learning Courses](#popular-linkedln-learning-courses)
  - [Git Resources](#git-resources)
  - [SSH Resources](#ssh-resources)
    - [SSH Key](#ssh-key)
    - [Adding SSH Public Key to Remote Server](#adding-ssh-public-key-to-remote-server)
      - [Windows Upload Command](#windows-upload-command)
      - [Linux and Mac Upload Command](#linux-and-mac-upload-command)
    - [Command Line Editors](#command-line-editors)
  - [Module Specific Resources](#module-specific-resources)
    - [Hello Linux, Hello C](#hello-linux-hello-c)
    - [C and the Memory Stack](#c-and-the-memory-stack)


## Course Text Books

As stated in the syllabus, while there is no required textbook for this course, there are two strongly, strongly recommended textbooks, both of which are available freely online. 

Grokking Algorithms, 1st Edition by Aditya Bhargava is friendly guide on for learning algorithms as they apply to practical problems faced by programmers on a regular basis.
Available here: https://learning.oreilly.com/library/view/grokking-algorithms/9781617292231/. See instructions that follow for how to access it for free using your Northeastern University account. 

[Dive Into Systems](https://diveintosystems.org/book/preface.html), by Suzanne J. Matthews, Tia Newhall, and Kevin C. Webb. A free, online textbook on computer systems and C.
Be sure to have these resources available and handy, we'll be using referencing them throughout the semester. The additional resources below should be used if you find you don't understand some element of the course, or if you want to dig deeper into these topics. As always, you can ask which of these resources would be best if you have specific questions. 

## O'Reilly Online: Books and Videos
As an NU student, you have access to a phenomenal resource through the NU Library: O'Reilly Online. 
1. Go to the NU library page here https://subjectguides.lib.neu.edu/compsci to an external site. 
2. Click on "Connect to O'Reilly" in the lower left hand corner
3. For institution, select "Not listed"
4. Put in your northeastern.edu email and continue with authentication
5. You may need to confirm your email with a notification email you receive in your inbox
6. Search for the books or videos you're looking for and add them to a playlist with this course name (for convenience, not required)

## Algorithms Resources

* [Visualizing Algorithms](https://visualgo.net/en). provides free interactive demos for learning Algorithms.
* [Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html). provides more free interactive demos for learning Algorithms.


### Advanced Resources that you may wish to consult as you prepare for CS 5800

* (Advanced) Introduction to Algorithms 4th edition, often used as a textbook for CS 5800 Algorithms course. Named "CLRS" for the initials of its 4 authors. 
* (Advanced) [The Algorithm Design Manual](https://www.algorist.com/), 3rd edition, by Steven Skiena. Like CLRS, a textbook that could be used for an algorithms class. 


## C Programming Resources

* [Head First C by David Griffiths and Dawn Griffiths](https://www.amazon.com/Head-First-C-Brain-Friendly-Guide/dp/1449399916/) is a brain-friendly book guide to the C programming language. Available on O'Reilly here: https://learning.oreilly.com/library/view/head-first-c/9781449335649/
* [C Programming Language by Brian W. Kernighan and Dennis M. Ritchie](https://www.amazon.com/Programming-Language-2nd-Brian-Kernighan/dp/0131103628) is a complete book guide and great reference for the programming language we will be using in this course. 
* [Effective C (oreilly.com)](https://learning.oreilly.com/library/view/effective-c/9781098125677/) - is a popular C programming book that I often use. It is available on O'Reilly for free (note they sometimes rotate their offerings.)

### Popular Linkedln Learning Courses
As a reminder, Northeastern students have access to linkedln learning. The following courses are popular among students.

* [Learning C](https://www.linkedin.com/learning/learning-c-5/). is a tutorial on C in LinkedIn Learning
* [Essential C](https://www.linkedin.com/learning/c-essential-training/). is another tutorial on C in LinkedIn Learning. 
  
## Git Resources
* [Git Essential Training](https://www.linkedin.com/learning/git-essential-training-the-basics/use-git-version-control-software-to-manage-project-code) - a LinkedIn Learning guide
* [MIT's Missing Semester of your CS Education lecture and text explainer on git](https://missing.csail.mit.edu/2020/version-control/)
* [Head First Git](https://learning.oreilly.com/library/view/head-first-git/9781492092506/), book: Available on O'Reilly
* [Github Basics](https://guides.github.com/introduction/git-handbook/), a guide for learning GitHub
* [Visualizing Git](http://git-school.github.io/visualizing-git/) is useful for learners who want to know what is going on behind the scenes

## SSH Resources
`ssh` is a program you can use to log into the khoury servers. It is possible to setup a secure key instead of using your password to login. While this is an advanced technique, we wanted to provide the resources here in case you were interested in exploring access.

### SSH Key
* [What are SSH Keys](https://www.w3docs.com/learn-git/ssh-key.html)
  * Note: the line about windows is incorrect since windows 10. You can run ssh-keygen directly via powershell (see below)
* [How To Generate SSH Keys on Windows 10+](https://www.howtogeek.com/762863/how-to-generate-ssh-keys-in-windows-10-and-windows-11/)

### Adding SSH Public Key to Remote Server

* [Linux/Mac: How to add public SSH key on a remote server](https://www.howtogeek.com/168147/add-public-ssh-key-to-remote-server-in-a-single-command/)

#### Windows Upload Command
There are multiple ways to upload your public key to your remote server. The easiest simply being logging into the server and cutting and pasting the key into authorized_keys. However, the following command line will do that for you (make sure to make changes)

```console
> ssh USERNAME@login.khoury.northeastern.edu "umask 077; test -d .ssh || mkdir .ssh ; cat >> .ssh/authorized_keys2 || exit 1" < PATH-ON-WINDOWS\id_rsa.pub
```

The PATH-ON-WINDOWS is the path to your public key. Often it will be C:\Users\YOUR_WINDOWS_USER_NAME\.ssh\id_rsa.pub as that is the default location when you run keygen. 

#### Linux and Mac Upload Command
There is also a program you can install with app-get or brew. `ssh-copy-id`

```console
> ssh-copy-id USERNAME@login.khoury.northeastern.edu
```


### Command Line Editors
* Vim - use `vimtutor` via the command line on the Khoury servers
* [Vim School](https://vimschool.netlify.app/)
* [Very basic emacs](http://ocean.stanford.edu/research/quick_emacs.html)
* [Emacs](https://www.gnu.org/software/emacs/tour/)
* Emacs has a built in tutorial
   * type emacs on the command line emacs   
   * then type control-h followed by t
* [Redhat Beginning Guide to Emacs](https://www.redhat.com/sysadmin/beginners-guide-emacs)
* [Guide to Nano](https://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/)
  


## Module Specific Resources

The following resources are copies of the links provided in each of the modules. 

### Hello Linux, Hello C
* [Windows Subsystem For Linux](https://github.com/CS5008-Khoury/Resources/blob/main/InstallC.md#windows-subsystem-for-linux-wsl)
* [Dive Into Systems: Using Unix](https://diveintosystems.org/book/Appendix2/index.html)
* [The Linux Command Line](https://learning.oreilly.com/library/view/the-linux-command/9781492071235/)
* [Windows 10 - enabling ssh](https://www.howtogeek.com/336775/how-to-enable-and-use-windows-10s-built-in-ssh-commands/)
* [By the C, by the C, by the Beautiful C](https://diveintosystems.org/book/C1-C_intro/index.html)
* [Effective C](https://learning.oreilly.com/library/view/effective-c-2nd/9781098182496/)
* [C Programming for Dummies](https://learning.oreilly.com/library/view/c-programming-for/9781119740247/)
  

### C and the Memory Stack

* Dive into Systems
  * [Part of Program Memory and Scope](https://diveintosystems.org/book/C2-C_depth/scope_memory.html)
  * [Binary Data and Representation](https://diveintosystems.org/book/C4-Binary/index.html)
  * [C Pointers](https://diveintosystems.org/book/C2-C_depth/pointers.html)
  * [Pointers and Functions](https://diveintosystems.org/book/C2-C_depth/pointers_functions.html)
  * [Arrays and Strings](https://diveintosystems.org/book/C1-C_intro/arrays_strings.html)
  * [Structs](https://diveintosystems.org/book/C1-C_intro/structs.html)

### C, The Heap, and Executables

* 
* [Compiler Explorer](https://godbolt.org/#g:!((g:!((g:!((h:codeEditor,i:(filename:'1',fontScale:14,fontUsePx:'0',j:1,lang:___c,selection:(endColumn:1,endLineNumber:5,positionColumn:1,positionLineNumber:5,selectionStartColumn:1,selectionStartLineNumber:5,startColumn:1,startLineNumber:5),source:'/*+Type+your+code+here,+or+load+an+example.+*/%0Aint+square(int+num)+%7B%0A++++return+num+*+num%3B%0A%7D%0A'),l:'5',n:'0',o:'C+source+%231',t:'0')),k:50,l:'4',n:'0',o:'',s:0,t:'0'),(g:!((h:compiler,i:(compiler:cg151,filters:(b:'0',binary:'1',binaryObject:'1',commentOnly:'0',debugCalls:'1',demangle:'0',directives:'0',execute:'1',intel:'0',libraryCode:'0',trim:'1',verboseDemangling:'0'),flagsViewOpen:'1',fontScale:14,fontUsePx:'0',j:1,lang:___c,libs:!(),options:'',overrides:!(),selection:(endColumn:1,endLineNumber:1,positionColumn:1,positionLineNumber:1,selectionStartColumn:1,selectionStartLineNumber:1,startColumn:1,startLineNumber:1),source:1),l:'5',n:'0',o:'+x86-64+gcc+15.1+(Editor+%231)',t:'0')),k:50,l:'4',n:'0',o:'',s:0,t:'0')),l:'2',n:'0',o:'',t:'0')),version:4)