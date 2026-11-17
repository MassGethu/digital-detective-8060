# Mission 4 — How programs run

## 1. Task / objective

Run a Python script and compare a compiler with an interpreter.

## 2. Work completed

### Task 4.1 — Run the script

Inside this mission folder, `python3 hello.py` printed:

```text
Hello from Python
```

### Task 4.2 — Compare the two approaches

| Point | Compiler | Interpreter |
| --- | --- | --- |
| When translation / execution happens | Translates the input before that translated program runs. | Carries out instructions during execution. |
| Typical output | A translated artifact such as machine code, object code or bytecode. | The program’s visible result or effects, such as text printed to the terminal. |
| One example | Clang compiling C source. | The CPython virtual machine executing Python bytecode. |
| One advantage | The compiler can optimise code before it runs. | Running edited code directly makes small experiments quick to try. |

## 3. Commands / tools used

`python3 hello.py` ran the script. Python’s `print()` wrote a line of text to the terminal.

## 4. My understanding

A compiler translates source code into a different representation, such as object code. An interpreter carries out instructions while the program runs, so the output can appear immediately in the terminal. The approaches can work together, as in CPython, which compiles Python source to bytecode and executes that bytecode in its virtual machine.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[hello.py](hello.py) and the observed output above.

## 8. Commit details

Commit message: `Compare compilers and interpreters`. See the repository’s commit history for this checkpoint.
