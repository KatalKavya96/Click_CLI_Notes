# Click Command -- Complete Notes

## What is `@click.command()`?

`@click.command()` converts a normal Python function into a Click
Command object.

This tells Click that the function:

-   Has a command name
-   Has help text
-   Can have arguments
-   Can have options
-   Knows how to execute when called from CLI

Internally, Click wraps the function and replaces it with a `Command`
object.

------------------------------------------------------------------------

## What Does "Decorator Wraps Function" Mean?

When we write:

``` python
@click.command()
def hello():
    ...
```

Python internally does:

``` python
hello = click.command()(hello)
```

So the original function is replaced with a Click Command object.

After decoration:

``` python
type(hello)
# <class 'click.core.Command'>
```

------------------------------------------------------------------------

## Docstring in Click

We can write a docstring using triple quotes inside the function:

``` python
def hello():
    """This is help text"""
```

Rules: - Must be the first statement inside the function - Automatically
appears when running `--help`

Example:

``` bash
python app.py --help
```

------------------------------------------------------------------------

## Parameters of `click.command()`

### 1️⃣ name

Override command name.

``` python
@click.command(name="greet-user")
```

Default: function name

------------------------------------------------------------------------

### 2️⃣ help

Override docstring help text.

``` python
@click.command(help="Custom help message")
```

------------------------------------------------------------------------

### 3️⃣ short_help

Short description shown in grouped commands.

``` python
@click.command(short_help="Greets user")
```

------------------------------------------------------------------------

### 4️⃣ epilog

Extra text shown at bottom of help page.

``` python
@click.command(epilog="Example: app.py --name Kavya")
```

------------------------------------------------------------------------

### 5️⃣ context_settings

Advanced configuration for parser behavior.

``` python
@click.command(context_settings=dict(ignore_unknown_options=True))
```

------------------------------------------------------------------------

### 6️⃣ options_metavar

Changes `[OPTIONS]` label in Usage line.

``` python
@click.command(options_metavar="[MY_OPTIONS]")
```

------------------------------------------------------------------------

### 7️⃣ add_help_option

Enable/disable automatic `--help`.

``` python
@click.command(add_help_option=False)
```

Default: True

------------------------------------------------------------------------

### 8️⃣ no_args_is_help

Shows help if no arguments are provided.

``` python
@click.command(no_args_is_help=True)
```

------------------------------------------------------------------------

### 9️⃣ hidden

Hides command from help listing.

``` python
@click.command(hidden=True)
```

------------------------------------------------------------------------

### 🔟 deprecated

Marks command as deprecated.

``` python
@click.command(deprecated=True)
```

------------------------------------------------------------------------

### 1️⃣1️⃣ cls

Allows custom Command class (advanced usage).

``` python
@click.command(cls=CustomCommandClass)
```

------------------------------------------------------------------------

## Main Guard

``` python
if __name__ == "__main__":
    hello()
```

This ensures: - Code runs only when file is executed directly - Does NOT
run when imported as a module

------------------------------------------------------------------------

## `raise SystemExit(...)`

``` python
raise SystemExit("Do not run app.py directly.")
```

Purpose: - Immediately stops execution - Prevents running file
directly - Equivalent to `sys.exit()`

------------------------------------------------------------------------

## Execution Flow of Click Command

Terminal\
↓\
Shell starts Python\
↓\
Python loads file\
↓\
Decorators wrap function\
↓\
Function becomes Click Command object\
↓\
Command is called\
↓\
Click parses sys.argv\
↓\
Prompts for missing values\
↓\
Validates types\
↓\
Calls original function\
↓\
Executes logic\
↓\
Output printed

------------------------------------------------------------------------

## Summary

-   `@click.command()` converts a function into a CLI command
-   Docstring becomes help message
-   Options and arguments are parsed automatically
-   Main guard controls direct execution
-   `SystemExit` stops program immediately
