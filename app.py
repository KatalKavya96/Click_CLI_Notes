import click

@click.command()
@click.option("--count",prompt="Count",default=1,help="Number of greetings")
@click.option("--name",prompt="Your Name",help="Enter your Name")

def hello(count,name):
    
    """Hello this is a function which greets you count times"""

    for i in range(count):
        
        click.echo(f'Hello,{name}!')
        
if __name__ == "__main__" :
    
    hello()
    
# Docstring
# I can write comment with triple quotes inside my function which will show up as a help message on running --help

# click.command() is converts python function to click command object which tells click that this funciton can have name,
# help text,arguements,options,knows how to execute

# The main guard code if __name__==__main__ tells cli what to do when the file is run directly
# If we do not write this main guard code it will automatically run the file whereever the file is imported

# raise SystemExit("Do not run app.py directly. Run test.py instead.") helps raise exit error