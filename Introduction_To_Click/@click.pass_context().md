# Click `@click.pass_context` --- Complete Notes

## Definition

`@click.pass_context` is a decorator in the Click library that passes
the **Click Context object (`ctx`)** to a command function.

The Context object contains runtime execution information and allows
sharing data between commands in structured CLI applications.

It is essential for building professional, multi-command CLI tools.

------------------------------------------------------------------------

# Basic Example

``` python
import click

@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = True

@cli.command()
@click.pass_context
def hello(ctx):
    if ctx.obj["DEBUG"]:
        click.echo("Debug mode ON")
    click.echo("Hello")
```

------------------------------------------------------------------------

# What is `ctx`?

`ctx` is an instance of:

    click.Context

It stores:

-   Current command information
-   Parent command reference
-   Parsed parameters
-   Shared object storage
-   Invocation metadata

------------------------------------------------------------------------

# Important Attributes of `ctx`

  Attribute                Description
  ------------------------ --------------------------------------
  ctx.obj                  Shared data storage between commands
  ctx.params               Parsed parameters dictionary
  ctx.invoked_subcommand   Name of invoked subcommand
  ctx.command              Current command object
  ctx.parent               Parent context
  ctx.args                 Extra arguments
  ctx.info_name            Command name used in CLI

------------------------------------------------------------------------

# Using `ctx.obj` for Shared State

``` python
@click.group()
@click.option("--config", type=str)
@click.pass_context
def cli(ctx, config):
    ctx.ensure_object(dict)
    ctx.obj["CONFIG_FILE"] = config
```

Subcommands can access:

``` python
ctx.obj["CONFIG_FILE"]
```

------------------------------------------------------------------------

# ctx.ensure_object()

Ensures that `ctx.obj` exists and is of a given type.

``` python
ctx.ensure_object(dict)
```

If not initialized, it creates the object.

------------------------------------------------------------------------

# Context Hierarchy

When using groups:

Main Group Context\
→ Subcommand Context\
→ Nested Subcommand Context

Each command has its own context but can access parent context via:

``` python
ctx.parent
```

------------------------------------------------------------------------

# ctx.invoked_subcommand

Used with `invoke_without_command=True`.

``` python
@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo("No command provided")
```

------------------------------------------------------------------------

# ctx.params

Contains parsed parameters as a dictionary.

``` python
click.echo(ctx.params)
```

------------------------------------------------------------------------

# ctx.exit()

Exit the CLI manually.

``` python
ctx.exit(1)
```

------------------------------------------------------------------------

# ctx.forward()

Forward parameters to another command.

``` python
ctx.forward(other_command)
```

------------------------------------------------------------------------

# ctx.invoke()

Invoke another command manually with arguments.

``` python
ctx.invoke(other_command, arg1="value")
```

------------------------------------------------------------------------

# pass_context vs pass_obj

There is also:

``` python
@click.pass_obj
```

-   `pass_context` → passes full context object
-   `pass_obj` → passes only `ctx.obj`

Example:

``` python
@click.pass_obj
def command(config):
    ...
```

------------------------------------------------------------------------

# Functional Classification

## State Sharing

-   ctx.obj
-   ctx.ensure_object()

## Execution Control

-   ctx.invoked_subcommand
-   ctx.exit()

## Advanced Command Flow

-   ctx.forward()
-   ctx.invoke()

------------------------------------------------------------------------

# Summary

`@click.pass_context` allows you to:

-   Access runtime execution context
-   Share global configuration
-   Build structured CLI applications
-   Implement DevOps-style command systems
-   Mimic professional tools like git, docker, airflow

------------------------------------------------------------------------

End of Notes
