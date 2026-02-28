# Click `@click.option()` --- Complete Notes

## Definition

`@click.option()` is a decorator used in the Click library to define
command-line options (flags) for CLI applications.\
It allows you to:

-   Accept user input from terminal flags
-   Define default values
-   Validate input types
-   Prompt interactively
-   Read environment variables
-   Add help documentation automatically

------------------------------------------------------------------------

# Basic Example

``` python
import click

@click.command()
@click.option("--count", type=int, default=1, help="Number of greetings")
@click.option("--name", prompt="Your Name", help="Enter your name")
def hello(count, name):
    for _ in range(count):
        click.echo(f"Hello {name}!")

if __name__ == "__main__":
    hello()
```

------------------------------------------------------------------------

# Full Signature (Simplified)

``` python
@click.option(
    param_decls,
    type=None,
    default=None,
    required=False,
    prompt=False,
    confirmation_prompt=False,
    hide_input=False,
    is_flag=None,
    flag_value=None,
    multiple=False,
    count=False,
    allow_from_autoenv=True,
    help=None,
    show_default=False,
    show_envvar=False,
    envvar=None,
    callback=None,
    nargs=None,
    metavar=None,
    expose_value=True,
    is_eager=False,
    shell_complete=None
)
```

------------------------------------------------------------------------

# All Parameters Explained

## 1️⃣ param_decls

**Type:** str or tuple of str\
Defines CLI flag names.

Example:

``` python
@click.option("-c", "--count")
```

------------------------------------------------------------------------

## 2️⃣ type

**Type:** Data type or Click type\
Defines expected input type.

Common Types:

  Type                    Description
  ----------------------- -------------------------
  int                     Integer values
  float                   Decimal numbers
  str                     Default string
  bool                    Boolean
  click.Choice(\[...\])   Restrict allowed values
  click.Path()            File or directory path
  click.File()            File object

Example:

``` python
@click.option("--count", type=int)
```

------------------------------------------------------------------------

## 3️⃣ default

**Type:** Any\
Default value if option not provided.

------------------------------------------------------------------------

## 4️⃣ required

**Type:** bool\
If True → user must provide value.

------------------------------------------------------------------------

## 5️⃣ prompt

**Type:** bool or str\
Prompts user interactively if not provided.

------------------------------------------------------------------------

## 6️⃣ confirmation_prompt

**Type:** bool\
Used for password confirmation.

------------------------------------------------------------------------

## 7️⃣ hide_input

**Type:** bool\
Hides input while typing (for passwords).

------------------------------------------------------------------------

## 8️⃣ is_flag

**Type:** bool\
Creates boolean flag.

Example:

``` python
@click.option("--debug", is_flag=True)
```

------------------------------------------------------------------------

## 9️⃣ flag_value

**Type:** Any\
Value assigned when flag is used.

------------------------------------------------------------------------

## 🔟 multiple

**Type:** bool\
Allows multiple values for same option.

Returns tuple.

------------------------------------------------------------------------

## 1️⃣1️⃣ count

**Type:** bool\
Counts how many times flag is used.

Example:

``` bash
-vvv
```

Returns `3`

------------------------------------------------------------------------

## 1️⃣2️⃣ envvar

**Type:** str\
Reads value from environment variable.

------------------------------------------------------------------------

## 1️⃣3️⃣ show_default

**Type:** bool\
Shows default value in help message.

------------------------------------------------------------------------

## 1️⃣4️⃣ help

**Type:** str\
Help description for option.

------------------------------------------------------------------------

## 1️⃣5️⃣ callback

**Type:** function\
Used for custom validation.

Example:

``` python
def validate(ctx, param, value):
    if value < 0:
        raise click.BadParameter("Must be positive")
    return value
```

------------------------------------------------------------------------

## 1️⃣6️⃣ nargs

**Type:** int\
Number of arguments expected.

Example:

``` python
@click.option("--coords", nargs=2, type=float)
```

------------------------------------------------------------------------

## 1️⃣7️⃣ metavar

**Type:** str\
Custom name shown in help.

------------------------------------------------------------------------

## 1️⃣8️⃣ expose_value

**Type:** bool\
Controls whether value is passed to function.

------------------------------------------------------------------------

## 1️⃣9️⃣ is_eager

**Type:** bool\
Executes option before others (used for --version).

------------------------------------------------------------------------

## 2️⃣0️⃣ shell_complete

**Type:** function\
Custom shell auto-completion logic.

------------------------------------------------------------------------

# Functional Classification

## Input Control

-   type
-   nargs
-   multiple
-   required

## UX Enhancement

-   prompt
-   hide_input
-   confirmation_prompt
-   help
-   show_default
-   metavar

## Behavior Control

-   is_flag
-   flag_value
-   count
-   envvar
-   callback
-   is_eager

------------------------------------------------------------------------

# Summary

`@click.option()` allows you to:

-   Define CLI flags
-   Validate types
-   Prompt users interactively
-   Read environment variables
-   Auto-generate help documentation
-   Build production-level CLI tools cleanly

------------------------------------------------------------------------

End of Notes
