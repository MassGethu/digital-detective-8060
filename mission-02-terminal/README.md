# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective

Use Terminal to manage files, compare listing flags, try a pipe and inspect Homebrew.

## 2. Work completed

### Task 2.1 — Basic operations

| Operation / command | What it does | What I observed |
| --- | --- | --- |
| Current-directory display, `pwd` | Prints the absolute working path. | It showed the mission folder as the current directory. |
| Directory listing, `ls` | Lists ordinary visible entries. | The mission README appeared. |
| Detailed listing, `ls -l` | Shows metadata such as permissions and sizes. | It included a permissions column and a size column. |
| Change directory, `cd ..` | Moves up one level. | From the mission folder it moved to the repository root. |
| Create directory, `mkdir terminal-practice` | Creates a new directory. | The practice folder appeared inside the mission folder. |
| Create empty file, `touch notes.txt` | Creates a zero-byte file if it does not exist. | The new file had a size of zero bytes. |
| Copy file, `cp notes.txt notes-copy.txt` | Makes a duplicate under a new name. | Both files existed. |
| Rename file, `mv notes-copy.txt old-copy.txt` | Renames or relocates a file. | The copy appeared under the new name. |
| Display contents, `cat notes.txt` | Prints the file contents to the terminal. | The empty file printed no text. |

### Task 2.2 — Safe file changes

Wrote the first line with `printf ... > notes.txt`, then added the second with `printf ... >> notes.txt`. Copied the result to `notes-copy.txt`, renamed the copy to `notes-backup.txt`, and used `cmp` to verify the two files matched. The final `cat notes.txt` output was:

```text
First line: terminal practice.
Second line: appended text.
```

- `>` replaces a file’s contents, while `>>` adds text at the end and preserves earlier lines.
- Copying creates another file and keeps the original. Moving or renaming changes where the same file is found.
- `pwd` gives the full path of the directory where relative commands start.
- `ls` helps confirm that files are in the expected directory and that copies or renames worked.

### Task 2.3 — Flags and pipes

`ls` listed the two visible files. `ls -lah` additionally showed detailed metadata (`-l`), dot entries including the temporary `.practice-marker` (`-a`), and size formatting that can use units like K and M (`-h`). The sample files were small enough to display in bytes.

In `ls -lah | head -n 3`, the pipe sends the directory listing to the input of `head`. The left command produces the listing, and the right command prints just its first three lines.

### Task 2.4 — Package managers

`brew --version` reported Homebrew 7.0.13. `brew list --formula` showed installed formulae, including `abseil`, `ada-url` and `brotli`. A package manager handles installation, updates and removal in one place. It can install dependencies required by another program and track what is installed. This exercise only inspected the existing installation.

## 3. Commands / tools used

`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, `printf`, `cmp`, `head`, `rm` and `brew` were used for the operations described above. `rm` removed the temporary file and marker created for this exercise.

## 4. My understanding

The working directory controls where relative file commands act. I can confirm the result of an operation with a listing, a content check or a comparison. Pipes let one command consume another command’s output.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[Original notes](terminal-practice/notes.txt) and [renamed backup](terminal-practice/notes-backup.txt).

## 8. Commit details

Commit message: `Complete Terminal and file management mission`. See the repository’s commit history for this checkpoint.
