# Mission 3 — Understand the operating system

## 1. Task / objective

Observe macOS, processes, storage, paths and permissions, then explain OS responsibilities.

## 2. Work completed

### Task 3.1 — System observations

| Information explored | What it tells you | Privacy-safe observation |
| --- | --- | --- |
| Operating system and system details | Identifies the OS release and machine architecture. | macOS 26.6.2 on arm64. |
| Current account identity | Identifies the account running the shell command. | `whoami` returned `[redacted]`. |
| Available and used storage | Shows how much of the macOS Data volume is used and available. | Used 167Gi, available 733Gi, usage 19% in the `df -h` output. |
| System activity snapshot | Shows system activity at the time of measurement. | `top` reported 492 processes in one snapshot. |

### Task 3.2 — Processes

A process is a running instance of a program with its own execution state. The PID is the operating system’s numeric process identifier. Google Chrome and Finder appeared in the filtered process list.

### Task 3.3 — Paths and permissions

From the repository root, going to `mission-02-terminal/terminal-practice` added those two directories to the end of the path printed by `pwd`. An absolute path begins at the filesystem root, for example `/Users/[redacted]/…/digital-detective-8060/mission-02-terminal/terminal-practice/notes.txt` (private directories omitted). A relative path is interpreted from the current directory. From the repository root, it is `mission-02-terminal/terminal-practice/notes.txt`.

The mode string for `notes.txt` was `-rw-r--r--`. The owner’s three positions are `rw-`: reading and writing are allowed, and execution is disabled. The observation used the existing file permissions.

### Task 3.4 — Operating-system responsibilities

| Responsibility | Explanation | Example |
| --- | --- | --- |
| Process management | Keeps track of running processes and schedules CPU time. | Chrome and Finder can both respond while they are open. |
| Memory management | Assigns memory to processes and protects their address spaces. | The editor can hold a document in RAM while Chrome uses separate memory. |
| Device management | Coordinates hardware access through device drivers. | Trackpad movement is delivered to an application as pointer input. |
| File management | Organises files into directories and handles reading and writing. | Saving notes creates a file inside the practice directory. |
| User interface / shell | Provides graphical controls and a way to issue commands. | Finder opens folders and the shell runs `ls`. |
| Security and permissions | Checks whether an account or process may access a resource. | The practice file’s owner can read and edit it. |

## 3. Commands / tools used

`sw_vers` displayed the macOS release. `uname -m` identified the architecture. `whoami` identified the current account. `df -h` checked storage. `top -l 1 -n 0` gave one activity snapshot and `ps -axo pid=,comm=` supplied process names. `pwd`, `ls -l` and `stat -f %Sp` were used for paths and file permissions.

## 4. My understanding

The OS shares resources across active processes and checks permissions on files. Its shell makes it possible to inspect both kinds of information directly.

## 5. Difficulties faced

The first shell session restricted process inspection.

## 6. How I resolved them

A separately approved read-only check captured two application names and the aggregate process count.

## 7. Evidence / files

Selected results are in the tables. The permission example uses [the terminal practice file](../mission-02-terminal/terminal-practice/notes.txt).

## 8. Commit details

Commit message: `Document operating system and file management`. See the repository’s commit history for this checkpoint.
