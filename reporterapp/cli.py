import click

from .api import ReporterApp

reporter_app = ReporterApp()


@click.group()
def cli():
    pass


@click.command()
def questions():
    for question in reporter_app.questions:
        click.secho(question.prompt, fg='green')


@click.command()
def snapshots():
    for snapshot in reporter_app.snapshots:
        date = snapshot.date.strftime('%d %b, %Y')
        click.secho(date, fg='green')
        click.echo(snapshot.batteryDisplay)


cli.add_command(questions)
cli.add_command(snapshots)
