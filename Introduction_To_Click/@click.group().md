# Click `@click.group()` --- Complete Notes

## Definition

`@click.group()` is a decorator in the Click library used to create a
**command group**, which allows multiple subcommands under a single CLI
entry point.

It is used to build structured, multi-command CLI applications similar
to:

-   git add
-   docker run
-   airflow dags list

If `@click.command()` creates a single command,\
then `@click.group()` creates a CLI application.

------------------------------------------------------------------------

# Basic Example

``` python
import click

@click.group()
def cli():
    """Main CLI group"""
    pass

@cli.command()
def hello():
    click.echo("Hello World")

@cli.command()
def bye():
    click.echo("Goodbye")

if __name__ == "__main__":
    cli()
```

------------------------------------------------------------------------

# Command Structure

    cli
     ├── hello
     └── bye

Usage:

``` bash
python app.py hello
python app.py bye
```

------------------------------------------------------------------------

# Full Signature (Simplified)

``` python
@click.group(
    name=None,
    commands=None,
    invoke_without_command=False,
    no_args_is_help=None,
    subcommand_metavar=None,
    chain=False,
    result_callback=None,
    context_settings=None,
    help=None,
    short_help=None,
    options_metavar=None,
    add_help_option=True,
    hidden=False,
    deprecated=False
)
```

------------------------------------------------------------------------

# All Parameters Explained

## 1️⃣ name

**Type:** str\
Overrides the CLI group name.

------------------------------------------------------------------------

## 2️⃣ commands

**Type:** dict\
Manually register commands instead of using decorators.

------------------------------------------------------------------------

## 3️⃣ invoke_without_command

**Type:** bool\
If True → group runs even without subcommand.

------------------------------------------------------------------------

## 4️⃣ no_args_is_help

**Type:** bool\
If True → automatically shows help when no arguments are provided.

------------------------------------------------------------------------

## 5️⃣ subcommand_metavar

**Type:** str\
Custom display name for subcommands in help output.

------------------------------------------------------------------------

## 6️⃣ chain

**Type:** bool\
Allows multiple subcommands in one execution.

Example:

``` bash
python app.py cmd1 cmd2 cmd3
```

------------------------------------------------------------------------

## 7️⃣ result_callback

**Type:** function\
Runs after all subcommands finish (useful with chain=True).

------------------------------------------------------------------------

## 8️⃣ context_settings

**Type:** dict\
Customize CLI behavior.

Common keys:

  Key                      Description
  ------------------------ -------------------------
  help_option_names        Customize help flags
  max_content_width        Control help formatting
  ignore_unknown_options   Allow unknown options
  allow_extra_args         Allow extra args

------------------------------------------------------------------------

## 9️⃣ help

**Type:** str\
Long help description.

------------------------------------------------------------------------

## 🔟 short_help

**Type:** str\
Short description shown in parent command list.

------------------------------------------------------------------------

## 1️⃣1️⃣ options_metavar

**Type:** str\
Customize options display text in help.

------------------------------------------------------------------------

## 1️⃣2️⃣ add_help_option

**Type:** bool\
Enable or disable automatic `--help` option.

------------------------------------------------------------------------

## 1️⃣3️⃣ hidden

**Type:** bool\
Hide group from help output.

------------------------------------------------------------------------

## 1️⃣4️⃣ deprecated

**Type:** bool or str\
Mark group as deprecated.

------------------------------------------------------------------------

# Inheritance Note

`@click.group()` internally extends:

Group → MultiCommand → Command

This means it inherits many behaviors from `@click.command()`.

------------------------------------------------------------------------

# Functional Classification

## Execution Control

-   invoke_without_command
-   chain
-   result_callback

## UX & Help Control

-   help
-   short_help
-   subcommand_metavar
-   options_metavar
-   no_args_is_help

## Internal Behavior

-   commands
-   context_settings
-   add_help_option
-   hidden
-   deprecated

------------------------------------------------------------------------

# Production Example

``` python
import click

@click.group(
    invoke_without_command=True,
    no_args_is_help=True,
    context_settings={"help_option_names": ["-h", "--help"]},
    help="Mini DevOps CLI"
)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo("Welcome to DevOps CLI")
```

------------------------------------------------------------------------

# Summary

`@click.group()` allows you to:

-   Build structured CLI applications
-   Organize commands hierarchically
-   Share global configuration via context
-   Create professional DevOps-style tools
-   Mimic real-world tools like git, docker, airflow

------------------------------------------------------------------------

End of Notes
