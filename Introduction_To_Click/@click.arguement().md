# Click `@click.argument()` --- Complete Notes

## Definition

`@click.argument()` is a decorator in the Click library used to define
**positional arguments** for a CLI command.

Unlike `@click.option()`: - Arguments do NOT use `--` - Order matters -
They are required by default

Arguments represent the core input to a command.

------------------------------------------------------------------------

# Basic Example

``` python
import click

@click.command()
@click.argument("name")
def hello(name):
    click.echo(f"Hello {name}")

if __name__ == "__main__":
    hello()
```

Usage:

``` bash
python app.py Kavya
```

------------------------------------------------------------------------

# Difference Between option() and argument()

  Feature               option()        argument()
  --------------------- --------------- ------------
  Uses `--`             Yes             No
  Order matters         No              Yes
  Required by default   No              Yes
  Best for              Configuration   Core input

------------------------------------------------------------------------

# Full Signature (Simplified)

``` python
@click.argument(
    param_decls,
    type=None,
    required=None,
    nargs=None,
    default=None,
    metavar=None,
    expose_value=True,
    callback=None,
    envvar=None
)
```

------------------------------------------------------------------------

# All Parameters Explained

## 1️⃣ param_decls

**Type:** str\
Defines the argument name.

Example:

``` python
@click.argument("filename")
```

------------------------------------------------------------------------

## 2️⃣ type

**Type:** Python type or Click type\
Defines expected input type.

Common Types:

  Type                    Description
  ----------------------- ------------------------
  int                     Integer
  float                   Decimal
  str                     Default string
  click.Path()            File or directory path
  click.File()            File object
  click.Choice(\[...\])   Restrict values

Example:

``` python
@click.argument("count", type=int)
```

------------------------------------------------------------------------

## 3️⃣ required

**Type:** bool\
Arguments are required by default.

------------------------------------------------------------------------

## 4️⃣ nargs

Defines number of values accepted.

### Single value (default)

``` python
@click.argument("name")
```

### Fixed multiple values

``` python
@click.argument("coords", nargs=2, type=float)
```

### Unlimited values

``` python
@click.argument("files", nargs=-1)
```

Returns tuple of values.

------------------------------------------------------------------------

## 5️⃣ default

**Type:** Any\
Provides default value (rarely used).

------------------------------------------------------------------------

## 6️⃣ metavar

**Type:** str\
Custom name displayed in help output.

------------------------------------------------------------------------

## 7️⃣ expose_value

**Type:** bool\
Controls whether value is passed to function.

------------------------------------------------------------------------

## 8️⃣ callback

**Type:** function\
Used for custom validation.

Example:

``` python
def validate(ctx, param, value):
    if not value.endswith(".txt"):
        raise click.BadParameter("Must be .txt file")
    return value

@click.argument("file", callback=validate)
```

------------------------------------------------------------------------

## 9️⃣ envvar

**Type:** str\
Reads argument value from environment variable.

------------------------------------------------------------------------

# Advanced Example

``` python
import click

@click.command()
@click.argument("source", type=click.Path(exists=True))
@click.argument("destination", type=click.Path())
def copy(source, destination):
    click.echo(f"Copying {source} to {destination}")
```

Usage:

``` bash
python app.py file1.txt file2.txt
```

------------------------------------------------------------------------

# Functional Classification

## Input Control

-   type
-   nargs
-   required

## Validation

-   callback
-   envvar

## Help Customization

-   metavar

------------------------------------------------------------------------

# Summary

`@click.argument()` allows you to:

-   Define positional inputs
-   Enforce order-sensitive parameters
-   Validate input types
-   Accept multiple values
-   Build git/docker-style CLI tools

------------------------------------------------------------------------

End of Notes
