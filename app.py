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
    
    