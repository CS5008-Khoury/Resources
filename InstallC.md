# Options for C

For this course, we will be defaulting to `gcc -Wall` for all our C code [GCC, The GNU Compiler](https://gcc.gnu.org/).  The struggle is that C varies greatly between systems, and so you will have to be careful what you install and run. Even the same compiler can have issues between systems.

Right now, our autograder runs on Ubuntu, so we will be using that as our default.  Your code needs to work on that system! Thankfully, you will have multiple submission attempts so you can work out any errors between systems. Beyond that, we recommend getting `gcc` working on your personal computer. Here are some options based on your operating system.


## Linux

If you already have linux installed / running linux, you are good to go! GCC should be on there by default, but if it isn't, you can look at adding it via your package manager.  For example, on Ubuntu, you can install it using `sudo apt install gcc`. 


## Mac OS X
For some Mac OS systems, gcc is already installed.  You can check if it is installed by running `gcc --version`.  If it is not installed, you can install it using `brew install gcc`.  You can find instructions for installing `brew` [here](https://brew.sh/).

## Windows

### Windows Subsystem for Linux (WSL)
Windows is a bit more complicated. We recommend using the Windows Subsystem for Linux (WSL).  You can find instructions for installing it [here](https://learn.microsoft.com/en-us/windows/wsl/install). For windows 11, you can install Ubuntu from the Microsoft Store, then then run `wsl` from the command line.  Once you have it installed, you can log into your linux subsystem via the terminal app using `wsl` command. Once inside linux, check your gcc default by typing `gcc --version`.  If it is not installed, you can install it using `sudo apt install gcc`.

### MinGW with VS Code
MinGW allows installing the GCC compiler for windows and running the GDB in windows directly.  You will need to install the [VS Code C/C++ extensions](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) from Microsoft, and we suggest fulling this [walk through on setting up VSCode and GCC](https://code.visualstudio.com/docs/cpp/config-mingw). You will still want to
eventually run `gcc -Wall` from the WSL, but this can be a good way to mostly develop in windows and then double check it all works still in linux. Please note, the walk through on the Microsoft page has an older command for the Pacman command. You will want to use the one on the MinGW page modifying it to add toolchain at the end. As of writing this resource (double check, it changes) that command was `pacman -S mingw-w64-ucrt-x86_64-toolchain`. This may also vary based on your OS version.


### Other Option: Visual Studio
You can find instructions for installing it on Windows [here](https://clang.llvm.org/get_started.html).  Admittedly, this path requires a number of local tools installed. Some of which you will install anyway, but the path can be complicated. 


## Khoury Servers
The khoury servers have everything you need to work installed. You will find resources for working with them throughout the canvas modules including VIM. You can log into the khoury servers either directly via SSH (`ssh username@login.khoury.northeastern.edu`) or via remote-connection extensions in various IDEs.   



## IDE Solutions

### Visual Studio Code
[Visual Studio Code](https://code.visualstudio.com/) is very common for students to use. This works best on MacOS, Linux, or using the WSL on Windows. You do not need to launch VS code from the WSL. Instead, you run it in windows, and then compile from the terminal by typing `wsl` to go into linux before compiling. Some students find using the [remote-ssh](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extension plus access to the khoury servers to be helpful. However, you have to make sure you close your remote connections or you can run into a lot of common issues.

### CLion
Developed by [Jet Brains](https://www.jetbrains.com/), [CLion](https://www.jetbrains.com/clion/) is a popular IDE that can use cmake cross platform.  We recommend you setup your [free student account](https://www.jetbrains.com/community/education/#students/), and then installing the [Toolbox App](https://www.jetbrains.com/toolbox-app/). You can then manage all your various JetBrains IDEs such as PyCharm, CLion, and IntelliJ (which is used for CS 5004). 

A common mistake with CLion is since it is using cmake files, you don't end up putting in the `-Wall` command line options. You will want to make sure to add that to the CMakeLists.txt file that gets generated with every new project. Here is an example of a modified file. Notice the `set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall")` line. 

```cmake
cmake_minimum_required(VERSION 3.24)
project(hw1 C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall")
add_executable(hw1 main.c)
```

Also, you will want to create a separate C executable project for each of your homeworks (instead of trying to keep them all in one project. While doable, it can be a difficult to manage). The nice thing is you can do "new from version control" and then just point it to your github repo. If you do that, you may need to generate the CMakeLists.txt file manually.

### Other IDEs

#### VIM 
A common command line editor, that the canvas shell will have videos about. It is installed on the khoury servers by default.

#### Emacs
Another common command line editor. You can find instructions for installing it [here](https://www.gnu.org/software/emacs/), and it is install on the khoury servers by default. 


## Support?
Please note, the TAs or instructors are not experts in every IDE, nor are they experts in your personal system. While we can help debug issues, any issues that come up are your responsibility as every system is different. In the end, if it isn't working, we may recommend you just SSH into the khoury servers and use VIM or Emacs. 